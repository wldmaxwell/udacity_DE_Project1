<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.716 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β29
* Sun Mar 14 2021 17:49:05 GMT-0700 (PDT)
* Source doc: Udacity Project one Data Model PostgreSQL Readme
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 1.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


**Project One: Data Modelling with Postgres**



*   Create Postgres Database and Tables: **python create_tables.py**
    *   If tables already exist they will be dropped and new tables will be created
*   Insert data into tables: **python etl.py**
    *   Extracts and processes JSON data and then inserts processed data into Database
*   etl.py

 

**Overview**

This project builds an ETL pipeline for a music streaming service called Sparkify by fetching data from JSON files, processing the data, and inserting the data into a PostgreSQL Database. This project provides Sparkify with tools to analyze song and user data to answer questions like “What songs are our customers listening to?”

**Technologies used**



*   Python - automate the ETL process into DB
*   Jupyter Notebook
    *   Used to develop and test code for etl.py
    *   Etl.ipynb: Notebook used to develop and run code for etl.py
    *   Test.ipynb: Used to run test SQL queries on the Postgresql database
*   SQL 
    *   used to create database and tables. 
    *   Used to JOIN data to insert data into songplays table
    *   Used to run ad-hoc queries to discover insight about the data sets
*   Postgresql Database

**Insights taken from dataset: sql queries in test.ipynb**



*   ./data/song_data: 71 files : contains information on songs and artist tables
*   ./data/log_data: 30 files : contains information on time and user tables
*   Songplays table requires JOIN of data from /data/log_data and /data/song_data
*   Unique Users: 97
*   Songs: 71
*   Artists: 69
*   Songplays: 6820
*   Most Popular Day to Stream: Wednesday With a count of 1364
*   Least Popular Day to Stream: Sunday With a count of 396

    **Database**


    The Sparkify analytics database (SparkifyDB) is a Star Schema design. The star schema separates business process data into facts, which hold the measurable, quantitative data about a business, and dimensions which are descriptive attributes related to fact data. 


    **Entity Relationship Diagram (ERD)**


    

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")




#### **Fact Table**



1. **songplays** - records in log data associated with song plays i.e. records with page NextSong
    *   _songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent_


#### **Dimension Tables**



*   **users** - users in the app
    *   _user_id, first_name, last_name, gender, level_
*   **songs** - songs in music database
    *   _song_id, title, artist_id, year, duration_
*   **artists** - artists in music database
    *   _artist_id, name, location, latitude, longitude_
*   **time** - timestamps of records in **songplays** broken down into specific units
    *   _start_time, hour, day, week, month, year, weekday_

**_File Descriptions_**



*   test.ipynb displays the first few rows of each table to let you check your database.
*   create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
*   etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
*   etl.py reads and processes files from song_data and log_data and loads them into your tables. 
*   sql_queries.py contains all your sql queries, and is imported into the last three files above.
