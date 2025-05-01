# Leetcode_python_clone
the basic structure of this project was to see if I could replicate a problem solving platform 
the idea was that you login and register like any platform, then you select the question and it will open up 
a txt file stored in the database where YOU WRITE YOUR SOLUTION IN THE TXT file then it would parse it and check 
if the test cases are valid or not.
This could still be a work in progress if I could add a frontend but I guess I am too lazy.

CleanCode - Coding Challenge Platform
Overview
CleanCode is a Python-based coding challenge platform that allows users to:

Register and login to the system

Attempt coding problems with various input types

View their submission history

Get immediate feedback on their solutions

Features
User Management
Registration with username and password

Login functionality

Automatic username suffix addition to ensure uniqueness

Problem Solving
9 different coding problems covering various concepts

Problems categorized by input type:

Integer and list arguments (Problems 1-2)

String arguments (Problems 3, 4, 8)

List-only arguments (Problems 5-7, 9)

Random problem selection option

Detailed problem descriptions provided in text files

Submission System
Code submission and automatic testing

Test case verification with immediate feedback

Status tracking (accepted/rejected)

Solution history storage

Database Structure
The system uses MySQL with the following main tables:

users: Stores user credentials (username, password)

quests: Contains problem information (question number, test cases, answers)

Individual user tables: Store each user's attempts (question number, attempted answer, status)

How to Use
Prerequisites
Python 3.x

MySQL server

mysql-connector-python package

Setup
Create a MySQL database named "Questions"

Configure database connection in db_config dictionary

Ensure the quests table exists with appropriate columns

Running the Application
Execute the Python script

Choose to register or login

After successful authentication, access the main menu

Main Menu Options
Questions: View and attempt coding problems

Select by question number or choose random (0)

Problem description opens in a text file

Write your solution in the file

Submit for evaluation

Attempted Questions: View your submission history

See which problems you've attempted

View your last solution for any problem

Exit: Leave the application

Problem Types
Integer and List Arguments (Problems 1-2):

Functions take an integer and a list as arguments

Example: Two Sum, First and Last Position in Sorted Array

String Arguments (Problems 3, 4, 8):

Functions take string inputs

Example: Palindrome Check, Anagram Check, String Rotation

List-only Arguments (Problems 5-7, 9):

Functions take lists as input

Example: Find Duplicate, First Missing Positive, Fibonacci

Notes
When registering, your username will automatically get a random suffix

Always write your solutions in the provided text files with proper Python indentation

The system preserves your submission history for review

Test cases are automatically verified against expected outputs

Troubleshooting
Ensure MySQL server is running

Verify database connection parameters

Check that required tables exist with correct schema

Make sure you have write permissions for text file creation

Enjoy solving coding challenges with CleanCode!
