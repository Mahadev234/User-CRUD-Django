## User CRUD (Django Project)

### Steps to Run the Project

1. Clone the repository:

```
git clone https://github.com/Mahadev234/User-CRUD-Django.git
```

2. Navigate to the project directory:

```
cd user_crud
```

3. Install the project dependencies:

```
pip install -r requirements.txt
```

4. Apply the database migrations:

```
python manage.py migrate
```

5. Start the development server:

```
python manage.py runserver
```

6. Access the application in your browser at `http://localhost:8000`.

7. Use the provided API endpoints to perform CRUD operations on users or you can use the default frontend to add, view, update or remove the users.

- **Create a new user:** Send a POST request to `/api/users` with the user data in the request body.

- **Get all users:** Send a GET request to `/api/users`.

- **Read user details:** Send a GET request to `/api/users/{user_id}` to retrieve the details of a specific user.

- **Update user details:** Send a PUT request to `/api/users/{user_id}` with the updated user data in the request body.

- **Delete a user:** Send a DELETE request to `/api/users/{user_id}` to remove a user from the system.

Make sure to replace `{user_id}` with the actual ID of the user you want to perform the CRUD operations on.

For more information on how to use the API endpoints, please refer to the API documentation.

#### Running with Docker

To run the project using Docker, follow these steps:

##### Linux and macOS

1. Install Docker on your system if you haven't already.

2. Open a terminal and navigate to the project directory.

3. Build the Docker image:

```
docker build -t user-crud-django .
```

4. Run the Docker container:

```
docker run -p 8000:8000 user-crud-django
```

5. Access the application in your browser at `http://localhost:8000`.

##### Windows

1. Install Docker Desktop on your system if you haven't already.

2. Open a command prompt and navigate to the project directory.

3. Build the Docker image:

```
docker build -t user-crud-django .
```

4. Run the Docker container:

```
docker run -p 8000:8000 user-crud-django
```

5. Access the application in your browser at `http://localhost:8000`.

