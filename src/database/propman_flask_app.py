from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from propman_session import DBSession
from propman_db_model import Consult_letter, Consult_letter_revision, Assessment_form, Assessment_form_revision, Employee, Library_form, Library_form_revision, Proposal, Sponsor, Supporting_document, Supporting_document_revision, Program_guide, Program_guide_revision
from sqlalchemy import and_

app = Flask(__name__)
session = DBSession()
bp = Blueprint('propman', __name__, template_folder='templates', static_folder='static')

temp_path = './propman'

@app.route('/')
@bp.route('/')
def propman():
	return render_template('%s/propman.html' % temp_path)

