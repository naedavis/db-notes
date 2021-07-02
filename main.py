# DDL - Data Definition Language
# DDL Statements or Commands are used to define and modify
# the database Structure of your tables or schema.
# DDL Statement, it takes effect immediately.

# DDL COMMANDS ARE :
# CREATE – to create table (objects) in the database
#   CREATE database Hospitals;

# ALTER – alters the structure of the database

# DROP – delete table from the database
#   drop database Hospitals;

# TRUNCATE – remove all records from a table,
# including all spaces allocated for the records are removed

# COMMENT – add comments to the data dictionary

# RENAME – rename a table


#################################################################################
# COMMANDS FOR WHEN INSIDE OF A DATABASE CREATED

# use - to get into the database
#   use Hospitals;

# create table - creating a table while in a specific database
#   (creating table then in brackets, creating the fields inside the table)
#   create table Dentists(Dentist_code varchar(25) not null,
#                           Dentist_namse varchar(25) not null,
#                           Dentist_surname varchar(30) not null,
#                           Dentist_contactNo varchar(10) not null,
#                           Dentist_practiceNo int not null,
#                           primary key (Dentist_code));

# auto_increment - (if we want each person in the record to have unique id then
#                   every time we add a new record the id will be increased by 1
#                   the default for auto_increment is 1)
#                   id int unsigned not null auto_increment
#                   (if you want the id to start from a different digit then)
#                   auto_increment = 100;


# show - to display the table created in the Hospitals database
#   show tables;
#   show databases;

# describe - to display the fields created in the table Dentists
#   describe Dentists;
#   describe Hospital.Dentists;

# Alter - to rename a field in the Dentists table
#   Alter table Dentists change Dentist_namse Dentist_names varchar(25);

##################################################################################
# DML - DATA MANIPULATION LANGUAGE

# INSERT– is used to insert data into a table.
#   (code to add first record)
#   INSERT into Dentists values
#   -> ("BNF450002", "Boniface", "Dr Simons", "0123456789","100526788");
# UPDATE– is used to update existing data within a table.
#   UPDATE Dentists SET Dentist_contactNo="0987654321";
# DELETE– is used to delete records from a database table.
#   DELETE FROM Dentists;
# SELECT– is used to retrieve data from the a database. (SOMETIMES GROUPED IN DQL)
#   (to see if a record now exists, we use select statement)
#   select * from Dentists


#################################################################################################
# TYPES OF COMMENTS

# 1
#####
# "# This comment continues to the end of line"

# 2
#####
# "-- This comment continues to the end of line"

# 3
#####
# "/* This is an in-line comment*/"

# 4
#####
# "/*
#   This is a multi-line
#   comment
# */"

##########################################################################################