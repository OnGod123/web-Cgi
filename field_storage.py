#!/usr/bin/env python

import cgi

# Assume these are values retrieved from the backend
default_name = "John Doe"
default_email = "john@example.com"

# Print headers
print("Content-Type: text/html")
print()

# Parse form data
form = cgi.FieldStorage()

# Retrieve form data
if form.method == "POST":
    name = form.getvalue('name')
    email = form.getvalue('email')
else:
    name = default_name
    email = default_email

# Generate HTML response with pre-filled form fields
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<title>Simple Form</title>")
print("</head>")
print("<body>")
print("<h2>Simple Form</h2>")
print("<form action='cgi-bin/process_form.py' method='post'>")
print("Name: <input type='text' name='name' value='{}' required><br>".format(name))
print("Email: <input type='email' name='email' value='{}' required><br>".format(email))
print("<input type='submit' value='Submit'>")
print("</form>")
print("</body>")
print("</html>")

