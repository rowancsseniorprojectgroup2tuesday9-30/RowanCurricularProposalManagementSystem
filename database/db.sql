DROP TABLE IF EXISTS `consult_letter`;

CREATE TABLE `consult_letter` (
  `consult_letter_id` smallint(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  `employee_id` smallint(6) UNSIGNED NOT NULL,
  `proposal_id` smallint(6) UNSIGNED NOT NULL,
  PRIMARY KEY (`consult_letter_id`),
  KEY `employee_id` (`employee_id`),
  KEY `proposal_id` (`proposal_id`),
  CONSTRAINT `consult_letter_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`),
  CONSTRAINT `consult_letter_ibfk_2` FOREIGN KEY (`proposal_id`) REFERENCES `proposal` (`proposal_id`)
);

DROP TABLE IF EXISTS `consult_letter_revision`;

CREATE TABLE `consult_letter_revision` (
  `consult_letter_id` smallint(6) UNSIGNED NOT NULL,
  `consult_letter_file_path` varchar(255) NOT NULL,
  `consult_letter_datetime` datetime NOT NULL,
  PRIMARY KEY (`consult_letter_id`, `consult_letter_datetime`),
  KEY `consult_letter_id` (`consult_letter_id`),
  CONSTRAINT `consult_letter_revision_ibfk_1` FOREIGN KEY (`consult_letter_id`) REFERENCES `consult_letter` (`consult_letter_id`)
);

DROP TABLE IF EXISTS `cover_sheet`;

CREATE TABLE `cover_sheet` (
  `cover_sheet_id` smallint(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`cover_sheet_id`)
);

DROP TABLE IF EXISTS `cover_sheet_revision`;

CREATE TABLE `cover_sheet_revision` (
  `cover_sheet_id` smallint(6) UNSIGNED NOT NULL,
  `cover_sheet_file_path` varchar(255) NOT NULL,
  `cover_sheet_datetime` datetime NOT NULL,
  PRIMARY KEY (`cover_sheet_id`, `cover_sheet_datetime`),
  KEY `cover_sheet_id` (`cover_sheet_id`),
  CONSTRAINT `cover_sheet_revision_ibfk_1` FOREIGN KEY (`cover_sheet_id`) REFERENCES `cover_sheet` (`cover_sheet_id`)
);

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `employee_id` smallint(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) NOT NULL,
  `middle_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `department` varchar(20) NOT NULL,
  `title` varchar(20) NOT NULL,
  `curricular_consultant` tinyint(4) UNSIGNED NOT NULL,
  PRIMARY KEY (`employee_id`)
);

DROP TABLE IF EXISTS `library_form`;

CREATE TABLE `library_form` (
  `library_form_id` smallint(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`library_form_id`)
);

DROP TABLE IF EXISTS `library_form_revision`;

CREATE TABLE `library_form_revision` (
  `library_form_id` smallint(6) UNSIGNED NOT NULL,
  `library_form_file_path` varchar(255) NOT NULL,
  `library_form_datetime` datetime NOT NULL,
  PRIMARY KEY (`library_form_id`, `library_form_datetime`),
  KEY `library_form_id` (`library_form_id`),
  CONSTRAINT `library_form_revision_ibfk_1` FOREIGN KEY (`library_form_id`) REFERENCES `library_form` (`library_form_id`)
);

DROP TABLE IF EXISTS `proposal`;

CREATE TABLE `proposal` (
  `proposal_id` smallint(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  `cover_sheet_id` smallint(6) UNSIGNED DEFAULT NULL,
  `library_form_id` smallint(6) UNSIGNED DEFAULT NULL,
  `template_id` smallint(6) UNSIGNED DEFAULT NULL,
  `program_guide_id` smallint(6) UNSIGNED DEFAULT NULL,
  `proposal_datetime` datetime NOT NULL,
  `revision_note` varchar(255) DEFAULT NULL,
  `proposal_title` varchar(50) NOT NULL,
  `proposal_description` varchar(255) DEFAULT NULL,
  `need_library_form` tinyint(4) UNSIGNED NOT NULL,
  `need_program_guide` tinyint(4) UNSIGNED NOT NULL,
  `cover_type` char(1) NOT NULL,
  `template_type` char(1) NOT NULL,
  PRIMARY KEY (`proposal_id`),
  KEY `cover_sheet_id` (`cover_sheet_id`),
  KEY `template_id` (`template_id`),
  KEY `library_form_id` (`library_form_id`),
  CONSTRAINT `proposal_ibfk_1` FOREIGN KEY (`cover_sheet_id`) REFERENCES `cover_sheet` (`cover_sheet_id`),
  CONSTRAINT `proposal_ibfk_2` FOREIGN KEY (`template_id`) REFERENCES `template` (`template_id`),
  CONSTRAINT `proposal_ibfk_3` FOREIGN KEY (`library_form_id`) REFERENCES `library_form` (`library_form_id`)
);

DROP TABLE IF EXISTS `sponsor`;

CREATE TABLE `sponsor` (
  `proposal_id` smallint(6) UNSIGNED NOT NULL,
  `employee_id` smallint(6) UNSIGNED NOT NULL,
  `is_author` tinyint(4) UNSIGNED NOT NULL,
  PRIMARY KEY (`proposal_id`, `employee_id`),
  KEY `proposal_id` (`proposal_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `sponsor_ibfk_1` FOREIGN KEY (`proposal_id`) REFERENCES `proposal` (`proposal_id`),
  CONSTRAINT `sponsor_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`)
);

DROP TABLE IF EXISTS `template`;

CREATE TABLE `template` (
  `template_id` smallint(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`template_id`)
);

DROP TABLE IF EXISTS `template_revision`;

CREATE TABLE `template_revision` (
  `template_id` smallint(6) UNSIGNED NOT NULL,
  `template_file_path` varchar(255) NOT NULL,
  `template_datetime` datetime NOT NULL,
  PRIMARY KEY (`template_id`, `template_datetime`),
  KEY `template_id` (`template_id`),
  CONSTRAINT `template_revision_ibfk_1` FOREIGN KEY (`template_id`) REFERENCES `template` (`template_id`)
);

DROP TABLE IF EXISTS `program_guide`;

CREATE TABLE `program_guide` (
  `program_guide_id` smallint(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`program_guide_id`)
);

DROP TABLE IF EXISTS `program_guide_revision`;

CREATE TABLE `program_guide_revision` (
  `program_guide_id` smallint(6) UNSIGNED NOT NULL,
  `program_guide_file_path` varchar(255) NOT NULL,
  `program_guide_datetime` datetime NOT NULL,
  PRIMARY KEY (`program_guide_id`, `program_guide_datetime`),
  KEY `program_guide_id` (`program_guide_id`),
  CONSTRAINT `program_guide_revision_ibfk_1` FOREIGN KEY (`program_guide_id`) REFERENCES `program_guide` (`program_guide_id`)
);
