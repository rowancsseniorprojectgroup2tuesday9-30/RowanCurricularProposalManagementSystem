# Using Database Schema

## Installation

1) Create a new empty database:

```
CREATE DATABASE db;
```

2) Import schema

```
mysql -u username -p database_name < db.sql
```

## Tables and Attributes

### User

* user_id
* first_name
* middle_name
* last_name
* user_email

### Proposal

* proposal_id
* proposal_parent_id
* proposal_name
* cover_sheet
* template
* library_form
* consult_letter
* author
* date
* accepted
* need_library_form
* cover_type
* template_type

### Cover Sheet

* cover_id
* cover_file_path
* cover_parent_id

### Template

* template_id
* template_file_path

### Library Form

* library_form_id
* library_form_file_path

### Consult Letter

* consult_letter_id
* consult_letter_file_path
* consult_letter_parent_id
