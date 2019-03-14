import os
import subprocess
from flask import Flask, request, redirect, url_for, send_from_directory
from flaskext.mysql import MySQL
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/upload'
ALLOWED_EXTENSIONS = set(['pdf', 'docx'])

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'senior'
app.config['MYSQL_DATABASE_DB'] = 'curricular_management'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()

cursor.execute("SELECT * from proposal")
data = cursor.fetchone()

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            if filename.endswith('.pdf'):
                uname = "Kubach"
                doctype = "-s"
                cmd = "./archiver.sh -n " + uname + " -f " + filename + " " + doctype
                subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                cursor.execute("INSERT INTO assessement_form_revision (assessement_form_id, assessement_form_file_path, assessement_form_datetime) values (1, 'test', NOW())")
                res = cursor.fetchall()

                for x in res:
                    print(x)


            if filename.endswith('.docx'):
                conv = "soffice --convert-to pdf /tmp/" + filename + " --outdir " + UPLOAD_FOLDER + " --headless"
                subprocess.call(conv, shell=True)
                uname = "Kubach"
                doctype = "-s"
                cmd = "./archiver.sh -n " + uname + " -f " + filename.replace(".docx",".pdf") + " " + doctype
                subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            

            if filename.endswith('png'):
                conv = "convert" + filename + " --path " + UPLOAD_FOLDER + " --headless"
                subprocess.call(conv, shell=True)
                

            return redirect(url_for('index'))
    return """
    <!doctype html>
    <title>Upload Cover Sheet</title>
    <h1>Upload Cover Sheet</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    <p>%s</p>
    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
