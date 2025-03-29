# Contacts API

Contacts API is a RESTful API for managing contacts. It provides functionality to create, read, update, and delete contacts, as well as search for contacts and retrieve a list of contacts with upcoming birthdays.

## Features

### Core Functionality:

1. **CRUD Operations**:

   - Create a new contact.
   - Retrieve a list of contacts with pagination.
   - Retrieve a single contact by its ID.
   - Update an existing contact by its ID.
   - Delete a contact by its ID.

2. **Search Contacts**:

   - Search by first name, last name, or email with pagination.

3. **Upcoming Birthdays**:
   - Retrieve a list of contacts with birthdays in the next `n` days (default: 7 days) with pagination.

## Prerequisites

- Python 3.8+
- Docker

## Setup and Usage

### Step 1: Start a PostgreSQL Container

Run the following command to start a PostgreSQL container:

```sh
docker run --name hw8-db -p 54321:5432 -e POSTGRES_USER=hw8 -e POSTGRES_PASSWORD=hw8pass -d postgres
```

### Step 2: Install Dependencies

Ensure you have a virtual environment activated, then install dependencies:

```sh
pip install -r requirements.txt
```

### Step 3: Configure and Apply Migrations

Use Alembic to manage database migrations. To create and apply the initial migration, run:

```sh
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### Step 4: Run application using command

Start the FastAPI server:

```sh
fastapi dev src/main.py
```

### Use swagger to perform available commands

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
