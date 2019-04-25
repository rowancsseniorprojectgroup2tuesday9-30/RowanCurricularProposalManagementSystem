import logging
logging.basicConfig(level=logging.DEBUG)
import os
import subprocess
import img2pdf
from flask import Flask, request, redirect, url_for, send_from_directory, \
render_template, session
from flaskext.mysql import MySQL
from werkzeug import secure_filename
import sys

UPLOAD_FOLDER = '/tmp/upload'
ALLOWED_EXTENSIONS = set(['pdf', 'docx'])

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
    session['proposal'] = proposal_id
    session['assessement'] = result[0]
    session['library'] = result[1]
    session['support'] = result[2]
    session['program'] = result[3]


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

@app.route("/login", methods=['GET', 'POST'])
def login():
    cursor.execute("SELECT department_id, department_name FROM department")
    if request.method == 'POST':
        session['department'] = request.form['department']
        return redirect(url_for('index'))

    return render_template('login.html', dept=cursor.fetchall())

@app.route("/create")
def createProposal():
    return render_template('create.html')

@app.route("/upload", methods=['GET', 'POST'])
def uploadpage():
    if request.method == 'POST':
        file = request.files['file']
        doctype = request.form.get('doc_select') 
        uname = session['proposal']

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
            #doc_id = session['consult']
            sql_query = """INSERT INTO consult_letter_revision (consult_letter_id, consult_letter_file_path, consult_letter_datetime) values (%s, %s, NOW())"""

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # doctype = request.form.get('doc_select') 

            if filename.endswith('.pdf'):
                # doctype = "-s"
                cmd = "./archiver.sh -n " + uname + " -f " + filename + " " + doctype

            if filename.endswith('.docx'):
                conv = "soffice --convert-to pdf /tmp/" + filename + " --outdir " + UPLOAD_FOLDER + " --headless"
                subprocess.call(conv, shell=True)
                uname = "Kubach"
                # doctype = "-s"
                cmd = "./archiver.sh -n " + uname + " -f " + filename.replace(".docx",".pdf") + " " + doctype

            if filename.endswith('png'):
                conv = "convert" + filename + " --path " + UPLOAD_FOLDER + " --headless"
                subprocess.call(conv, shell=True)
                
            newFilename = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            cursor.execute(sql_query, newFilename.stdout.readlines()[0].strip())
            conn.commit()

            return redirect(url_for('uploadpage', doctype = doctype))
    return render_template('upload.html')

@app.route("/download", methods=['GET', 'POST'])
def downloadpage():
    if request.method == 'POST':
        document = request.form.get('document')

        if selectDoc == "-a":
            sql_query = """SELECT assessement_form_file_path FROM assessement_form_revision WHERE assessement_form_id = %s"""
        elif selectDoc == "-l":
            sql_query = """SELECT library_form_file_path FROM library_form_revision WHERE library_form_id = %s"""
        elif selectDoc == "-s":
            sql_query = """SELECT assessement_form_file_path FROM assessement_form_revision WHERE assessement_form_id = %s"""
        elif selectDoc == "-p":
            sql_query = """SELECT assessement_form_file_path FROM assessement_form_revision WHERE assessement_form_id = %s"""
        elif selectDoc == "-c":
            sql_query = """SELECT assessement_form_file_path FROM assessement_form_revision WHERE assessement_form_id = %s"""

    elif request.method == 'GET':
        selectVer = request.form.get('select_version')
        #uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
        #return send_file('/tmp/upload/Kubach_Assessement_Form_20190418040324.pdf',mimetype='application/pdf', as_attachment=True)
        return send_from_directory(directory='/tmp/upload', filename='Kubach_Assessement_Form_20190404151301.pdf', as_attachment=True)
        #return redirect(url_for('downloadpage', doctype = selectDoc))
    return send_file('/tmp/upload/Kubach_Assessement_Form_20190404151301.pdf', as_attachment=True)
    #return send_from_directory(directory=uploads, filename="Kubach_Assessement_Form_20190418040324.pdf", as_attachment=True)
    #return render_template('index.html')
    #return render_template('download.html')

@app.route("/status")
def status():
    return render_template('status.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
