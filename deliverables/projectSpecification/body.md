# Project Summary

The purpose of this system is to aid the faculty & staff members involved in 
curricular proposals. The system will store and keep revisions of the files 
used in constructing a proposal. The system will also allow users to email 
their complete proposals to other users for review.

# Project Goals

The goals of this project are as follows:

1) Streamline the process of creating, editing, and completing a proposal.
2) Collect all required documents of a proposal into one central database.
2) Provide version control for each proposal and its separate documents.

# Product Features

1) **System**: The system will be set up on a Linux server.
2) **User accounts**: Users will log in with their Rowan email and a password.
3) **Database**: A database to contain the locations of files, as well as relationships 
between files. 
    * Database will also store any other relevant information (version, author, etc).
4) **Curricular Proposals**: 
    * Create / modify curricular proposals.
    * Upload and store relevant 'parts' to a given proposal:
        * Cover sheet
        * Template
        * Library form (optional)
        * Consult letter(s)
    * Approve / Deny curricular proposals.
    * Browse through and search for existing proposals.
    * Keep version numbers and revision notes of proposals.
5) **Interface**: Interaction with system via a web front-end.
6) **Email**: Composition and sending of emails via SMTP.

# Limitations

1) A proposal may have been updated by the time someone reviews the version sent to them.
2) A document must be edited in a program such as Word. There is no integrated editor.

# Stretch Goals

1) Google OAuth integration for login.
2) Integration with open source workflow creation tools.
3) Automatically convert from multiple formats (.doc, .docx) to .pdf.
4) Automatically notify relevant users of a proposal change.
5) Auto generate cover sheets using database fields. (title, department, etc.).
6) Integration with Rowan’s new curriculum system.
