# SOAP-database
Model System for Occupancy Agreement Processing database and Python application for access

## DDL Script
To run the DDL script, navigate to the project folder and launch sqlite3 with `SOAP.db`:
```
$ cd /path/to/project
$ sqlite3 SOAP.db
```

Use the `.read` command to execute the script then exit:
```
sqlite> .read SOAP_DDL.sql
sqlite> .exit
```

## Python Application
The application program, `SOAP_App.py`, can be run after the SOAP database has been initialized (the file's permissions might need to be modified using `chmod` to allow it to run):
```
$ chmod 777 ./SOAP_App.py
$ python ./SOAP_App.py
```