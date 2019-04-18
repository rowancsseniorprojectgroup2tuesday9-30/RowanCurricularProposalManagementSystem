"""
=============================================================================
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
 this is connecting the backend to frontend via the controler flask
 Last edit: 4/18/19
 =============================================================================
"""
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.inspection import inspect

engine = create_engine('mysql+pymysql://cs_user:happy29july@localhost/propman', isolation_level='READ_COMMITTED')
Base = automap_base()
Base.prepare(engine, reflect=True)

#Mapped classes
Consult_letter = Base.classes.consult_letter
Consult_letter_revision = Base.classes.consult_letter_revision
Assessement_form = Base.classes.assessment_form
Assessement_form_Revision = Base.classes.assessement_form_revision
Employee = Base.classes.employee
Library_form = Base.classes.library_form
Library_form_revision = Base.classes.library_form_revision
Proposal = Base.classes.proposal
Sponsor = Base.classes.sponsor
Supporting_document = Base.classes.supporting_document
Supporting_document_revision = Base.classes.supporting_document_revision
Program_guide = Base.classes.program_guide
Program_guide_revision = Base.classes.program_guide_revision

#Check mapped relationships
'''
classes = [Consult_letter, Consult_letter_revision, Assessment_form, Assessment_form_revision, Employee, Library_form, Library_form_revision, Proposal, Sponsor, Supporting_document, Supporting_document_revision, Program_guide, Program_guide_revision]

for c in classes:
    print('Relationships for %s' % str(c))
    print(inspect(c).relationships.items())
'''
