# Injection 
Run the uprotected_webserver.py and experiment with the injection explained below. 


To perform the SQL injection for logging in as a known user without knowing their password, you would manipulate the input fields in the login page. Here's what you should enter:

In the Username Field: Enter the known username followed by a single quote (') and a double hyphen (--). For example, if the known username is alice, you would enter:

Copy this into the username field. 
admin' --
In the Password Field: You can enter any value or leave it blank. It won't matter because the SQL injection will comment out the password check in the SQL query. For example:

sql
Copy code
[any value or leave empty]
Explanation of the Inputs:
Username Input (admin' --):
The admin' portion closes the string literal for the username in the SQL query.
The -- is a comment indicator in SQL. It effectively comments out the rest of the query, ignoring the password check.



For the login form on your application, use the following inputs:

Username Field: Enter an SQL condition that always evaluates to true, followed by SQL to limit the result to one row. For example:

vbnet
Copy code
' OR 1=1 LIMIT 1 --
Password Field: This field can be left blank or filled with any random value, as the SQL injection will negate the need to check the password.

What Happens in the Backend
With the injected input, the SQL query executed by your Flask application will turn into:

sql
Copy code
SELECT * FROM users WHERE username = '' OR 1=1 LIMIT 1 --' AND password = 'whatever'
Here’s what happens:

'' OR 1=1: The condition 1=1 is always true. The OR operator thus ensures that the WHERE clause is true for all rows in the table.
LIMIT 1: This limits the results to just one row, which will typically be the first user in the database.
--: This comments out the rest of the SQL query, rendering the password check irrelevant.
Result of the Injection
The SQL query effectively becomes a command to select the first user from the users table, completely ignoring any username or password conditions. As a result, you will be logged in as the first user in the database, whoever that might be.