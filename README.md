# rest-example
REST API Example using Django REST Framework

Clone Repo:
$git clone https://github.com/microangel/rest-example.git

Create Python 3 virtual environment: 
$virtualenv P3VE -p /usr/bin/python3

pip install -r requirements.txt

The data is already generated an in the sqlite DB. You can regenerate with the provided script.

Basic auth with: larry/hello

Use curl or Postman to perform the REST calls

---

Based on these requirements:

Employee REST server

Create a web application that exposes REST operations for employees. The API should be able to:

Get employees by an ID
Create new employee
Update existing employee
Delete employee
Get all employees

An employee is made up of the following data:
Employee spec
ID - Unique identifier for an employee
FirstName - Employee first name
MiddleInitial - Employee middle initial
LastName - Employee last name
DateOfBirth - Employee birthday and year
DateOfEmployment - Employee start date
Status - ACTIVE or INACTIVE

Startup

On startup, the application should be able to ingest an external source of employees, and should make them available via the GET endpoint.

ACTIVE vs INACTIVE employees
By default, all employees are active, but by way of the API, can be switched to inactive. This should be done by the delete API call. This call should require some manner of authorization header.
When an employee is inactive, they should no longer be able to be retrieved in either the get by id, or get all employees calls

 

All data should be persisted into either memory, or externally. Please include instructions on how to run and interact with the web server.
