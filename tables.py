from ctypes.wintypes import CHAR, DOUBLE
from lib2to3.pgen2.token import STRING
from sqlite3 import Date
from tkinter.tix import INTEGER
from tokenize import Double, String


class regions():
    region_id: INTEGER
    region_name: STRING

class countries():
    country_id: CHAR
    country_name: String
    region_id: INTEGER

class locations():
    location_id: INTEGER
    street_address: String
    postal_code: String
    city: String     
    state_province: String
    country_id: CHAR

class departments():
    department_id: INTEGER
    department_name: String
    manager_id: INTEGER
    location_id: INTEGER

class jobs():
    job_id: String
    job_title: String
    min_salary: INTEGER
    max_salary: INTEGER

class employees():
    employee_id: INTEGER 
    first_name: String
    last_name: String 
    email: String   
    phone_number: String
    hire_date: Date        
    job_id: String    
    salary: DOUBLE
    commission_pct: DOUBLE
    manager_id: INTEGER
    department_id: INTEGER

class job_history():
    employee_id: INTEGER  
    start_date: Date            
    end_date: Date           
    job_id: String  
    department_id: INTEGER
