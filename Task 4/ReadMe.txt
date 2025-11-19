FLASK USER MANAGEMENT REST API

This project is a simple, fundamental RESTful API built with Python and the Flask framework. It demonstrates core API development concepts, specifically the CRUD (Create, Read, Update, Delete) operations, using an in-memory dictionary as a temporary database.

OBJECTIVE

To provide a hands-on example of how to define REST endpoints in Flask for managing a single resource: Users.

SETUP AND INSTALLATION

Prerequisites:

Python 3.x

Flask (Install via pip)

pip install Flask

Running the API:

Ensure your Flask application file (app.py) is complete and saved.

Open your terminal or command prompt.

Navigate to the project directory.

Run the application:

python app.py

The server will start, typically running on https://www.google.com/search?q=http://127.0.0.1:5000/. Keep this terminal window open while testing the API.

DATA STRUCTURE

The API uses an in-memory Python dictionary to store users. This data resets every time the server is restarted.

Initial Data:

users = {
1: {"name": "Alice", "email": "alice@example.com"},
2: {"name": "Bob", "email": "bob@example.com"}
}

API ENDPOINTS

All endpoints use the base URL: https://www.google.com/search?q=http://127.0.0.1:5000

HTTP Method: GET
Route: /users
Description: Retrieves a list of all users.
Action: Read (All)

HTTP Method: GET
Route: /users/int:user_id
Description: Retrieves a single user by ID.
Action: Read (One)

HTTP Method: POST
Route: /users
Description: Creates a new user.
Action: Create

HTTP Method: PUT
Route: /users/int:user_id
Description: Updates an existing user's details.
Action: Update

HTTP Method: DELETE
Route: /users/int:user_id
Description: Deletes a user by ID.
Action: Delete

TESTING THE ENDPOINTS (cURL Examples)

You can test the endpoints using a tool like Postman or through your terminal using cURL.

Important Note for Windows PowerShell Users:
If you encounter an error when using 'curl -X', your system is likely using the PowerShell alias for 'Invoke-WebRequest'. Use the following syntax instead:

GET Example in PowerShell

iwr -Method GET -Uri https://www.google.com/search?q=http://127.0.0.1:5000/users

(For the examples below, we will use the standard 'curl' syntax.)

GET (Read)

A. Get All Users

curl -X GET https://www.google.com/search?q=http://127.0.0.1:5000/users

B. Get a Single User (ID 1)

curl -X GET https://www.google.com/search?q=http://127.0.0.1:5000/users/1

POST (Create)

The server will automatically assign the next available ID (likely ID 3).

curl -X POST

-H "Content-Type: application/json"

-d '{"name": "Charlie", "email": "charlie@example.com"}'

https://www.google.com/search?q=http://127.0.0.1:5000/users

Expected Status: 201 Created

PUT (Update)

Updates the user with ID 1. Note that we send the full update payload.

curl -X PUT

-H "Content-Type: application/json"

-d '{"name": "Alice Smith", "email": "alice.smith@newmail.com"}'

https://www.google.com/search?q=http://127.0.0.1:5000/users/1

Expected Status: 200 OK

DELETE (Delete)

Deletes the user with ID 2.

curl -X DELETE https://www.google.com/search?q=http://127.0.0.1:5000/users/2

Expected Status: 204 No Content