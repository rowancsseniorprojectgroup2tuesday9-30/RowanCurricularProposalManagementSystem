<?xml version="1.0"?>
<mysqldump xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<database name="senior_project">
	<table_structure name="consult_letter">
		<field Field="consult_letter_id" Type="smallint(5) unsigned" Null="NO" Key="PRI" Extra="auto_increment" Comment="" />
		<field Field="consult_letter_file_path" Type="varchar(255)" Null="NO" Key="" Extra="" Comment="" />
		<field Field="consult_letter_parent" Type="smallint(5) unsigned" Null="YES" Key="" Default="NULL" Extra="" Comment="" />
		<key Table="consult_letter" Non_unique="0" Key_name="PRIMARY" Seq_in_index="1" Column_name="consult_letter_id" Collation="A" Cardinality="0" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<options Name="consult_letter" Engine="InnoDB" Version="10" Row_format="Dynamic" Rows="0" Avg_row_length="0" Data_length="16384" Max_data_length="0" Index_length="0" Data_free="0" Auto_increment="2" Create_time="2019-02-12 02:00:29" Update_time="2019-02-12 02:00:29" Collation="utf8mb4_unicode_ci" Create_options="" Comment="" Max_index_length="0" Temporary="N" />
	</table_structure>
	<table_structure name="cover_sheet">
		<field Field="cover_id" Type="smallint(5) unsigned" Null="NO" Key="PRI" Extra="auto_increment" Comment="" />
		<field Field="cover_file_path" Type="varchar(255)" Null="NO" Key="" Extra="" Comment="" />
		<field Field="cover_parent" Type="smallint(5) unsigned" Null="YES" Key="" Default="NULL" Extra="" Comment="" />
		<key Table="cover_sheet" Non_unique="0" Key_name="PRIMARY" Seq_in_index="1" Column_name="cover_id" Collation="A" Cardinality="0" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<options Name="cover_sheet" Engine="InnoDB" Version="10" Row_format="Dynamic" Rows="0" Avg_row_length="0" Data_length="16384" Max_data_length="0" Index_length="0" Data_free="0" Auto_increment="2" Create_time="2019-02-12 02:00:02" Update_time="2019-02-12 02:00:02" Collation="utf8mb4_unicode_ci" Create_options="" Comment="" Max_index_length="0" Temporary="N" />
	</table_structure>
	<table_structure name="library_form">
		<field Field="library_form_id" Type="smallint(5) unsigned" Null="NO" Key="PRI" Extra="auto_increment" Comment="" />
		<field Field="library_form_file_path" Type="varchar(255)" Null="NO" Key="" Extra="" Comment="" />
		<key Table="library_form" Non_unique="0" Key_name="PRIMARY" Seq_in_index="1" Column_name="library_form_id" Collation="A" Cardinality="1" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<options Name="library_form" Engine="InnoDB" Version="10" Row_format="Dynamic" Rows="1" Avg_row_length="16384" Data_length="16384" Max_data_length="0" Index_length="0" Data_free="0" Auto_increment="2" Create_time="2019-02-10 23:36:22" Update_time="2019-02-11 00:11:41" Collation="utf8mb4_unicode_ci" Create_options="" Comment="" Max_index_length="0" Temporary="N" />
	</table_structure>
	<table_structure name="proposal">
		<field Field="proposal_id" Type="smallint(5) unsigned" Null="NO" Key="PRI" Extra="auto_increment" Comment="" />
		<field Field="parent_proposal" Type="smallint(5) unsigned" Null="YES" Key="" Default="NULL" Extra="" Comment="" />
		<field Field="proposal_name" Type="varchar(50)" Null="NO" Key="" Extra="" Comment="" />
		<field Field="cover_sheet" Type="smallint(5) unsigned" Null="NO" Key="MUL" Extra="" Comment="" />
		<field Field="template" Type="smallint(5) unsigned" Null="NO" Key="MUL" Extra="" Comment="" />
		<field Field="library_form" Type="smallint(5) unsigned" Null="NO" Key="MUL" Extra="" Comment="" />
		<field Field="consult_letter" Type="smallint(5) unsigned" Null="NO" Key="MUL" Extra="" Comment="" />
		<field Field="author" Type="smallint(5) unsigned" Null="NO" Key="MUL" Extra="" Comment="" />
		<field Field="date" Type="datetime" Null="NO" Key="" Extra="" Comment="" />
		<field Field="accepted" Type="tinyint(4)" Null="NO" Key="" Default="0" Extra="" Comment="" />
		<field Field="need_library_form" Type="tinyint(4)" Null="NO" Key="" Extra="" Comment="" />
		<field Field="cover_type" Type="char(1)" Null="NO" Key="" Extra="" Comment="" />
		<field Field="template_type" Type="char(1)" Null="NO" Key="" Extra="" Comment="" />
		<key Table="proposal" Non_unique="0" Key_name="PRIMARY" Seq_in_index="1" Column_name="proposal_id" Collation="A" Cardinality="1" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<key Table="proposal" Non_unique="1" Key_name="fk_cover_sheet" Seq_in_index="1" Column_name="cover_sheet" Collation="A" Cardinality="1" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<key Table="proposal" Non_unique="1" Key_name="fk_template" Seq_in_index="1" Column_name="template" Collation="A" Cardinality="1" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<key Table="proposal" Non_unique="1" Key_name="fk_library_form" Seq_in_index="1" Column_name="library_form" Collation="A" Cardinality="1" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<key Table="proposal" Non_unique="1" Key_name="fk_consult_letter" Seq_in_index="1" Column_name="consult_letter" Collation="A" Cardinality="1" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<key Table="proposal" Non_unique="1" Key_name="fk_author" Seq_in_index="1" Column_name="author" Collation="A" Cardinality="1" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<options Name="proposal" Engine="InnoDB" Version="10" Row_format="Dynamic" Rows="1" Avg_row_length="16384" Data_length="16384" Max_data_length="0" Index_length="81920" Data_free="0" Auto_increment="2" Create_time="2019-02-11 01:03:55" Collation="utf8mb4_unicode_ci" Create_options="" Comment="" Max_index_length="0" Temporary="N" />
	</table_structure>
	<table_structure name="template">
		<field Field="template_id" Type="smallint(5) unsigned" Null="NO" Key="PRI" Extra="auto_increment" Comment="" />
		<field Field="template_file_path" Type="varchar(255)" Null="NO" Key="" Extra="" Comment="" />
		<key Table="template" Non_unique="0" Key_name="PRIMARY" Seq_in_index="1" Column_name="template_id" Collation="A" Cardinality="1" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<options Name="template" Engine="InnoDB" Version="10" Row_format="Dynamic" Rows="1" Avg_row_length="16384" Data_length="16384" Max_data_length="0" Index_length="0" Data_free="0" Auto_increment="2" Create_time="2019-02-10 23:35:40" Update_time="2019-02-11 00:10:58" Collation="utf8mb4_unicode_ci" Create_options="" Comment="" Max_index_length="0" Temporary="N" />
	</table_structure>
	<table_structure name="user">
		<field Field="user_id" Type="smallint(5) unsigned" Null="NO" Key="PRI" Extra="auto_increment" Comment="" />
		<field Field="first_name" Type="varchar(20)" Null="NO" Key="" Extra="" Comment="" />
		<field Field="middle_name" Type="varchar(20)" Null="YES" Key="" Default="NULL" Extra="" Comment="" />
		<field Field="last_name" Type="varchar(20)" Null="NO" Key="" Extra="" Comment="" />
		<field Field="email" Type="varchar(30)" Null="NO" Key="" Extra="" Comment="" />
		<key Table="user" Non_unique="0" Key_name="PRIMARY" Seq_in_index="1" Column_name="user_id" Collation="A" Cardinality="1" Null="" Index_type="BTREE" Comment="" Index_comment="" />
		<options Name="user" Engine="InnoDB" Version="10" Row_format="Dynamic" Rows="1" Avg_row_length="16384" Data_length="16384" Max_data_length="0" Index_length="0" Data_free="0" Auto_increment="2" Create_time="2019-02-10 22:52:38" Update_time="2019-02-11 00:15:41" Collation="utf8mb4_unicode_ci" Create_options="" Comment="" Max_index_length="0" Temporary="N" />
	</table_structure>
</database>
</mysqldump>
