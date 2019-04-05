"""
-----------------------------------------------------------------------------

Rowan Computer Science Dept Spring 2019 Senior Project Team
Rowan Curricular Proposal Mangagement System for Jack Myers rowan

Senior Team Members:
Team Lead:  John Kubach
 Scrum Master:  Joshua Jackson
    Developer:  Alex Kulplin
    Developer:  Jeffrey Podwats
    Developer:  Alaina Smith
    Developer:  Kyle Butera

-----------------------------------------------------------------------------

Description:
 This is the code for uploading necessary images to web page

 Last edit: 4/3/19
-----------------------------------------------------------------------------
"""

#==========================imports===============================================
# Imports that are need will go in this box
import os
import subprocess
import img2pdf
#========================end=====================================================

#=================connection=====================================================
# This will connect the back front end to the database setting flask up box
from flask import Flask, request, redirect, url_for, send_from_directory, \
    render_template
from flaskext.mysql import MySQL
from werkzeug import secure_filename
#====================end==========================================================

#======================varibles for uploading=====================================
UPLOAD_FOLDER = '/tmp/upload'
ALLOWED_EXTENSIONS = set(['pdf', 'docx'])
#==========================end====================================================

#===================================================================================
app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'senior'
app.config['MYSQL_DATABASE_DB'] = 'curricular_management'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#===================end=============================================================

#=================Checks file to see if allowed=====================================
#
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#=======================end=========================================================

#=============================================================================
#

@app.route("/", methods=['GET', 'POST'])
def index():
    conn = mysql.connect()
    cursor = conn.cursor()
    if request.method == 'POST':
        file = request.files['file']
        doctype = request.form.get('doc_select')
        uname = "Kubach"

        if doctype == "-a":
            sql_query = """INSERT INTO assessement_form_revision (assessement_form_id, assessement_form_file_path, assessement_form_datetime) values (1, %s, NOW())"""
        elif doctype == "-l":
            sql_query = """INSERT INTO library_form_revision (library_form_id, library_form_file_path, library_form_datetime) values (1, %s, NOW())"""
        elif doctype == "-s":
            sql_query = """INSERT INTO supporting_document_revision (supporting_document_id, supporting_document_file_path, supporting_document_datetime) values (1, %s, NOW())"""
        elif doctype == "-p":
            sql_query = """INSERT INTO program_guide_revision (program_guide_id, program_guide_file_path, program_guide_datetime) values (1, %s, NOW())"""
        elif doctype == "-c":
            sql_query = """INSERT INTO consult_letter_revision (consult_letter_id, consult_letter_file_path, consult_letter_datetime) values (1, %s, NOW())"""

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            if filename.endswith('.pdf'):
                cmd = "./archiver.sh -n " + uname + " -f " + filename + " " + doctype

            if filename.endswith('.docx'):
                conv = "soffice --convert-to pdf /tmp/" + filename + " --outdir " + UPLOAD_FOLDER + " --headless"
                subprocess.call(conv, shell=True)
                cmd = "./archiver.sh -n " + uname + " -f " + filename.replace(".docx", ".pdf") + " " + doctype

            if filename.endswith('png'):
                conv = "convert" + filename + " --path " + UPLOAD_FOLDER + " --headless"
                subprocess.call(conv, shell=True)

            newFilename = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            cursor.execute(sql_query, newFilename.stdout.readlines()[0].strip())
            conn.commit()

            return redirect(url_for('index', doctype=doctype))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
#=============================================================================