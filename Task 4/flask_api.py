from flask import Flask, request, jsonify

app = Flask(__name__)

# --- In-Memory Data Store ---
# A dictionary to store user data. The key is the user_id.
# Initial data for testing
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}
current_id = 3 # Start the next ID after the initial data

# --- Helper function to get the next ID ---
def get_next_id():
    global current_id
    next_id = current_id
    current_id += 1
    return next_id

# --- 1. GET (Read all users and Read a single user) ---
@app.route('/users', methods=['GET'])
def get_users():
    """Returns a list of all users."""
    # Convert the dictionary of users to a list of user objects with their IDs
    user_list = [{"id": user_id, **user_data} for user_id, user_data in users.items()]
    return jsonify(user_list)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Returns a single user by ID."""
    if user_id not in users:
        # Return 404 Not Found if user doesn't exist
        return jsonify({"error": "User not found"}), 404
    
    # Return the user data along with their ID
    user_data = {"id": user_id, **users[user_id]}
    return jsonify(user_data)

# --- 2. POST (Create a new user) ---
@app.route('/users', methods=['POST'])
def create_user():
    """Creates a new user."""
    # Get JSON data from the request body
    new_user_data = request.get_json()
    
    # Basic validation for required fields
    if not new_user_data or 'name' not in new_user_data or 'email' not in new_user_data:
        return jsonify({"error": "Missing 'name' or 'email' in request body"}), 400

    # Get the next unique ID
    user_id = get_next_id()
    
    # Store the new user
    users[user_id] = {'name': new_user_data['name'], 'email': new_user_data['email']}
    
    # Return the created user object and a 201 Created status code
    response_data = {"id": user_id, **users[user_id]}
    return jsonify(response_data), 201

# --- 3. PUT (Update an existing user) ---
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Updates an existing user's data."""
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    update_data = request.get_json()
    
    # Basic validation for required fields
    if not update_data or ('name' not in update_data and 'email' not in update_data):
        return jsonify({"error": "Missing 'name' or 'email' in request body"}), 400

    # Update only the fields provided in the request
    if 'name' in update_data:
        users[user_id]['name'] = update_data['name']
    if 'email' in update_data:
        users[user_id]['email'] = update_data['email']
        
    # Return the updated user object
    response_data = {"id": user_id, **users[user_id]}
    return jsonify(response_data)

# --- 4. DELETE (Remove a user) ---
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes a user by ID."""
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    # Remove the user from the dictionary
    del users[user_id]
    
    # Return a 204 No Content status code to indicate successful deletion
    return '', 204

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)