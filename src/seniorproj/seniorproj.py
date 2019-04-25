import logging
logging.basicConfig(level=logging.DEBUG)
import os
import subprocess
import img2pdf
from flask import Flask, request, redirect, url_for, send_from_directory, \
render_template, session, send_file
from flaskext.mysql import MySQL
from werkzeug import secure_filename
import sys

UPLOAD_FOLDER = '/tmp/upload'
ALLOWED_EXTENSIONS = set(['pdf', 'docx', 'png'])

app = Flask(__name__)
app.secret_key = 'test'

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'senior'
app.config['MYSQL_DATABASE_DB'] = 'curricular_management'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


conn = mysql.connect()
cursor =conn.cursor()

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def set_proposal_session(proposal_id):
    sql_query = """SELECT assessement_form_id, library_form_id, supporting_document_id, program_guide_id from proposal WHERE proposal_id = %s"""
    cursor.execute(sql_query, proposal_id)
    result = cursor.fetchone()
    print (result, file=sys.stdout)
    session['proposal'] = proposal_id
    session['assessement'] = result[0]
    session['library'] = result[1]
    session['support'] = result[2]
    session['program'] = result[3]

def get_max_index():
    cursor.execute("SELECT MAX(assessement_form_id) FROM assessement_form")
    assessement = cursor.fetchone()
    cursor.execute("SELECT MAX(library_form_id) FROM library_form")
    library = cursor.fetchone()
    cursor.execute("SELECT MAX(supporting_document_id) FROM supporting_document")
    support = cursor.fetchone()
    cursor.execute("SELECT MAX(program_guide_id) FROM program_guide")
    program = cursor.fetchone()
    max_id = [assessement, library, support, program]
    return max_id

@app.route("/", methods=['GET', 'POST', 'PUT'])
def index():
    if not session.get('department'):
        return redirect(url_for('login'))

    cursor.execute("SELECT proposal_id, proposal_title FROM proposal")
    if request.method == 'POST':
        prop_id = request.form['proposal']
        set_proposal_session(prop_id)
        return redirect(url_for('status'))
        
    return render_template('index.html', prop=cursor.fetchall())

@app.route("/navbar", methods=['POST'])
def nav():
    if 'home' in request.form:
        return redirect(url_for('index'))
    if 'upload' in request.form:
        return redirect(url_for('uploadpage'))
    if 'download' in request.form:
        return redirect(url_for('downloadpage'))
    if 'status' in request.form:
        return redirect(url_for('status'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    cursor.execute("SELECT department_id, department_name FROM department")
    if request.method == 'POST':
        session['department'] = request.form['department']
        return redirect(url_for('index'))
    return render_template('login.html', dept=cursor.fetchall())

@app.route("/logout")
def logout():
    session.pop('department')
    if session.get('proposal'):
        session.pop('proposal')
        session.pop('assessement')
        session.pop('library')
        session.pop('support')
        session.pop('program')

    return redirect(url_for('login'))

@app.route("/create", methods=['GET', 'POST'])
def createProposal():
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('description')
        proposal_type = request.form.get('proposal_type')
        need_lib = 0
        need_program = 0
        if proposal_type == "form_A":
            proposal_type = 'A'
            need_lib = 1
            need_program = 1
        elif proposal_type == "form_B":
            proposal_type = 'B'
        elif proposal_type == "form_C":
            proposal_type = 'C'
            need_lib = 1
            need_program = 1
        elif proposal_type == "form_D":
            proposal_type = 'D'
            need_program = 1
        elif proposal_type == "form_E":
            proposal_type = 'E'
            need_program = 1
        elif proposal_type == "form_F":
            proposal_type = 'F'

        cursor.execute("""INSERT INTO assessement_form (assessement_form_id) VALUES (NULL)""")
        conn.commit()
        cursor.execute("""INSERT INTO library_form (library_form_id) VALUES (NULL)""")
        conn.commit()
        cursor.execute("""INSERT INTO supporting_document (supporting_document_id) VALUES (NULL)""")
        conn.commit()
        cursor.execute("""INSERT INTO program_guide (program_guide_id) VALUES (NULL)""")
        conn.commit()
        doc_id = get_max_index();
        create_proposal = """INSERT INTO proposal (assessement_form_id, library_form_id, supporting_document_id, program_guide_id, proposal_datetime, proposal_title, proposal_description, need_library_form, need_program_guide, proposal_type) VALUES (%s, %s, %s, %s, NOW(), %s, %s, %s, %s, %s)"""
        argu = [doc_id[0], doc_id[1], doc_id[2], doc_id[3], title, desc, need_lib, need_program, proposal_type]
        cursor.execute(create_proposal, argu)
        conn.commit

        return redirect(url_for('index'))

    get_dept = "SELECT department_name FROM department WHERE department_id = %s"
    cursor.execute(get_dept, session['department'])
    dept = cursor.fetchone()

    return render_template('create.html', dept = dept)

@app.route("/upload", methods=['GET', 'POST'])
def uploadpage():
    if request.method == 'POST':
        file = request.files['file']
        doctype = request.form.get('doc_select') 
        get_prop = """SELECT proposal_title FROM proposal WHERE proposal_id = %s"""
        cursor.execute(get_prop, session['proposal'])
        result = cursor.fetchone()
        uname = result[0].replace(" ", "_")


        if doctype == "-a":
            doc_id = session['assessement']
            sql_query = """INSERT INTO assessement_form_revision (assessement_form_id, assessement_form_file_path, assessement_form_datetime) values (%s, %s, NOW())"""
        elif doctype == "-l":
            doc_id = session['library']
            sql_query = """INSERT INTO library_form_revision (library_form_id, library_form_file_path, library_form_datetime) values (%s, %s, NOW())"""
        elif doctype == "-s":
            doc_id = session['support']
            sql_query = """INSERT INTO supporting_document_revision (supporting_document_id, supporting_document_file_path, supporting_document_datetime) values (%s, %s, NOW())"""
        elif doctype == "-p":
            doc_id = session['program']
            sql_query = """INSERT INTO program_guide_revision (program_guide_id, program_guide_file_path, program_guide_datetime) values (%s, %s, NOW())"""
        elif doctype == "-c":
            consult = ("INSERT INTO consult_letter (proposal_id) VALUES (%s)")
            cursor.execute(consult, session['proposal'])
            conn.commit
            cursor.execute("SELECT MAX(consult_letter_id) FROM consult_letter")
            result = cursor.fetchall()
            doc_id = result[0]
            sql_query = """INSERT INTO consult_letter_revision (consult_letter_id, consult_letter_file_path, consult_letter_datetime) values (%s, %s, NOW())"""

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            if filename.endswith('.pdf'):
                cmd = "./archiver.sh -n " + uname + " -f " + filename + " " + doctype

            if filename.endswith('.docx'):
                conv = "soffice --convert-to pdf /tmp/upload/" + filename + " --outdir " + "/tmp/upload/" + " --headless"
                subprocess.call(conv, shell=True)
                cmd = "./archiver.sh -n " + uname + " -f " + filename.replace(".docx",".pdf") + " " + doctype

            if filename.endswith('png'):
                pngfile = filename.replace(".png", ".pdf")
                conv = "convert /tmp/upload/" + filename + " /tmp/upload/" + pngfile
                subprocess.call(conv, shell=True)
                cmd = "./archiver.sh -n " + uname + " -f " + pngfile + " " + doctype
                
            newFilename = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            cursor.execute(sql_query, (doc_id, newFilename.stdout.readlines()[0].strip()))
            conn.commit()

            return redirect(url_for('uploadpage', doctype = doctype))
    return render_template('upload.html')
    #return ('', 204)

@app.route("/download", methods=['GET', 'POST'])
def downloadpage():
    if request.method == 'POST':
        doc = request.form.get('document')

        if doc == "-a":
            sql_query = """SELECT assessement_form_file_path FROM assessement_form_revision WHERE assessement_form_id = %s"""
            cursor.execute(sql_query, session['assessement'])
        elif doc == "-l":
            sql_query = """SELECT library_form_file_path FROM library_form_revision WHERE library_form_id = %s"""
            cursor.execute(sql_query, session['library'])
        elif doc == "-s":
            sql_query = """SELECT supporting_document_file_path FROM supporting_document_revision WHERE supporting_document_id = %s"""
            cursor.execute(sql_query, session['support'])
        elif doc == "-p":
            sql_query = """SELECT program_guide_file_path FROM program_guide_revision WHERE program_guide_id = %s"""
            cursor.execute(sql_query, session['program'])
        elif doc == "-c":
            sql_query = """SELECT consult_letter_file_path FROM consult_letter_revision WHERE consult_letter_id in (SELECT consult_letter_id FROM consult_letter where proposal_id = %s)"""
            cursor.execute(sql_query, session['proposal'])
        return render_template('download.html', revision = cursor.fetchall(), doc = doc)

    if 'revision' in request.args:
        rev = request.args.get('revision')
        return send_file("/tmp/upload/" + rev, as_attachment=True)
    return render_template('download.html')

@app.route("/status", methods=['GET'])
def status():
    if not session.get('program'):
        return redirect(url_for('index', program = "none"))

    sql= """SELECT * FROM program_guide_revision WHERE program_guide_id = %s""" 
    cursor.execute(sql, session['program'])
    program = cursor.rowcount

    sql= """SELECT * FROM assessement_form_revision WHERE assessement_form_id = %s"""
    cursor.execute(sql, session['assessement'])
    assessement = cursor.rowcount

    sql= """SELECT * FROM library_form_revision WHERE library_form_id = %s"""
    cursor.execute(sql, session['library'])
    library = cursor.rowcount

    sql= """SELECT * FROM consult_letter WHERE proposal_id = %s"""
    cursor.execute(sql, session['proposal'])
    consult = cursor.rowcount

    sql= """SELECT * FROM supporting_document_revision WHERE supporting_document_id = %s"""
    cursor.execute(sql, session['support'])
    support = cursor.rowcount

    doc = [program, assessement, library, support, consult]
    get_prop = """SELECT proposal_title, proposal_description FROM proposal WHERE proposal_id = %s"""
    cursor.execute(get_prop, session['proposal'])
    prop = cursor.fetchone()
    return render_template('status.html', doc = doc, prop = prop)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
