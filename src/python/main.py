import os
import subprocess
from flask import Flask, request, redirect, url_for, send_from_directory
#from flaskext.mysql import MySQL
from werkzeug import secure_filename

UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = set(['pdf', 'docx'])

app = Flask(__name__)
#mysql = MySQL()
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'senior'
#app.config['MYSQL_DATABASE_DB'] = 'curricular_management'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)

#conn = mysql.connect()
#cursor =conn.cursor()

#cursor.execute("SELECT * from proposal")
#data = cursor.fetchone()

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
                #cmd = "./archiver.sh -n " + uname + " -f " + filename + " " + doctype
                #subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                #cursor.execute("INSERT INTO assessement_form_revision (assessement_form_id, assessement_form_file_path, assessement_form_datetime) values (1, 'test', NOW())")
                #res = cursor.fetchall()

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
    <!DOCTYPE html>
<html>
<head></head>

<body>

<button class="tablink" onclick="openPage('Home', this, '#57150B')" id="defaultOpen">Home</button>
<button class="tablink" onclick="openPage('Upload', this, '#57150B')">Upload</button>
<button class="tablink" onclick="openPage('Download', this, '#57150B')">Download</button>
<button class="tablink" onclick="openPage('Status', this, '#57150B')">Status</button>

<!––The Home page––> 
<div id="Home" class="tabcontent">
	<center>
	<h1>Rowan Curricular Proposal Management System</h1>	
	
	<img src="Rowan_University_seal.svg.png" alt="Rowan University">
	</center>
</div>

<!––The Download page––> 
<div id="Download" class="tabcontent">
	<center>
	<h1>Download Page</h1>
	</center>

	<h3>Proposal</h3>

	<select>
		<option value="p1">Proposal 1</option>
		<option value="p2">Proposal 2</option>
		<option value="p3">Proposal 3</option>
		<option value="p4">Proposal 4</option>
	</select>

	<h3>Cover Sheet</h3>

	<select>
		<option value="v1">Version 1</option>
		<option value="v2">Version 2</option>
	</select>

	<h3>Library Form</h3>

	<select>
		<option value="v1">Version 1</option>
		<option value="v2">Version 2</option>
	</select>

	<h3>Template</h3>

	<select>
		<option value="v1">Version 1</option>
		<option value="v2">Version 2</option>
	</select>

	<h3>Supporting Documents</h3>

	<select>
		<option value="v1">Version 1</option>
		<option value="v2">Version 2</option>
	</select>

	<h3>Program Guide</h3>

	<select>
		<option value="v1">Version 1</option>
		<option value="v2">Version 2</option>
	</select>

	<h1>
		<a href="#" class="button">Download</a>
	</h1>
</div>

<!––The Upload page––> 
<div id="Upload" class="tabcontent">
	<center>
	<h1>Upload Page</h1>
	</center>

	<h3>Proposal</h3>

	<select>
		<option value="p1">Proposal 1</option>
		<option value="p2">Proposal 2</option>
		<option value="p3">Proposal 3</option>
		<option value="p4">Proposal 4</option>
	</select>

	<form>
		<h3>Document Name</h3>
		<input type="text" name="document_name"><br>
	</form>

	<h3>Document Type</h3>

	<select>
		<option value="cover_sheet">Cover Sheet</option>
		<option value="library_form">Library Form</option>
		<option value="template">Template</option>
		<option value="supporting_document">Supporting Document</option>
		<option value="program_guide">Program Guide</option>
	</select>

	<h3>Attach Files</h3>

	<form action="" method=post enctype=multipart/form-data>
		<p>
		<input type=file name=file>
		<input type=submit value=Upload>
		</p>
	</form>

	<form>
		<h3>Comments</h3>
		<textarea name="comments" cols="100" rows="10"></textarea><br>
	</form>
</div>


<!––The Status page––> 
<div id="Status" class="tabcontent">
	<center>
	<h1>Status Page</h1>
	</center>

	<h3>Proposal</h3>

	<select>
		<option value="p1">Proposal 1</option>
		<option value="p2">Proposal 2</option>
		<option value="p3">Proposal 3</option>
		<option value="p4">Proposal 4</option>
	</select>

	<h3>Cover Sheet</h3>

	<h3>Library Form</h3>

	<h3>Template</h3>

	<h3>Supporting Documents</h3>

	<h3>Program Guide</h3>
</div>
</body>

    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
