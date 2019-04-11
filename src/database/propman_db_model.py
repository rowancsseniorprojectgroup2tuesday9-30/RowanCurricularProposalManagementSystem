from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.inspection import inspect

engine = create_engine('mysql+pymysql://cs_user:happy29july@localhost/propman', isolation_level='READ_COMMITTED')
Base = automap_base()
Base.prepare(engine, reflect=True)

#Mapped classes
Consult_Letter = Base.classes.consult_letter
Consult_Letter_Revision = Base.classes.consult_letter_revision
Assessement_Form = Base.classes.assessment_form
Assessement_Form_Revision = Base.classes.assessement_form_revision
Employee = Base.classes.employee
Library_Form = Base.classes.library_form
Library_Form_Revision = Base.classes.library_form_revision
Proposal = Base.classes.proposal
Sponsor = Base.classes.sponsor
Supporting_Document = Base.classes.supporting_document
Supporting_Document_Revision = Base.classes.supporting_document_revision
Program_Guide = Base.classes.program_guide
Program_Guide_Revision = Base.classes.program_guide_revision

#Check mapped relationships
'''
classes = [Consult_Letter, Consult_Letter_Revision, Assessment_Form, Assessment_Form_Revision, Employee, Library_Form, Library_Form_Revision, Proposal, Sponsor, Supporting_Document, Supporting_Document_Revision, Program_Guide, Program_Guide_Revision]
for c in classes:
    print('Relationships for %s' % str(c))
    print(inspect(c).relationships.items())
'''
