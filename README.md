# User Module

## Overview
The **User Module** is a Django-based application that provides user management functionality, including user authentication, profile management, and location-based features using Google Maps. It is built with Django's robust framework and integrates GeoDjango for spatial data handling.

---

## Features
- **User Authentication**:
  - Login and logout functionality.
  - Custom email-based authentication backend.

- **User Management**:
  - View and manage user profiles.
  - Edit user details such as name, email, phone number, and address.

- **Location-Based Features**:
  - Display user locations on a map using Google Maps API.
  - GeoDjango integration for spatial data handling.

- **Pagination**:
  - Paginated views for user profiles.

---

## Technologies Used
- **Backend**:
  - Django
  - GeoDjango
  - PostgreSQL with PostGIS for spatial data

- **Frontend**:
  - HTML, CSS, Bootstrap
  - Google Maps API

- **Other Tools**:
  - Logging for debugging and error tracking
  - Django Test Framework for unit testing

---

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL with PostGIS extension
- Virtual environment (recommended)

### Steps
1. **Clone the Repository**:
   Download the project files from the repository and navigate to the project directory.
    ```bash
    git clone <repository-url>
    ```

2. **Set Up Virtual Environment**:
   Create and activate a virtual environment to isolate dependencies.
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Dependencies**:
   Install all required Python packages listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4. **Create the `.env` File**:
   Create a `.env` file in the root directory and add the following configuration:
    ```plaintext
    # Database configuration
    DB_ENGINE=django.contrib.gis.db.backends.postgis
    DB_NAME=dbname
    DB_USER=dbuser
    DB_PASSWORD=dbpassword
    DB_HOST=127.0.0.1
    DB_PORT=5432

    # Google Maps API Key
    GOOGLE_MAPS_API_KEY=AIzaSyAsQhvWRnmGTyoTyFkANrkzI3shdvkjn
    ```

5. **Set Up the Database**:
   Ensure PostgreSQL with PostGIS is installed and running. Create a database and configure the `.env` file with the correct credentials.

6. **Run Migrations**:
   Apply database migrations to set up the required tables.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Load Static Files**:
   Collect all static files for the project.
    ```bash
    python manage.py collectstatic
    ```

8. **Run the Test Cases**:
   Run the test suite to ensure the application is working as expected.
    ```bash
    python manage.py test
    ```
9. **Run the Development Server**:
   Start the Django development server to access the application.
    ```bash
    python manage.py createsuperuser
    ```
10. **Run the Development Server**:
   Start the Django development server to access the application.
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

10. **Access the Application**:
    Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

---

## Usage

### Authentication
- Use the login page to authenticate users.
- Logout functionality is available via the logout endpoint.

### User Management
- Navigate to the "Manage Users" page to view and edit user profiles.
- Pagination is implemented for better user experience.

### Map View
- View user locations on a map using the "Map" page.
- Ensure the Google Maps API key is configured in the `.env` file.

---

## Testing
Run the test suite to ensure the application is working as expected. The test cases cover user authentication, profile management, and map view functionality.

---

## Project Structure
```
user_module/
├── user_module/
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # WSGI entry point
│   └── asgi.py           # ASGI entry point
├── user_profile/
│   ├── models.py         # User models
│   ├── views.py          # Application views
│   ├── email_back_end.py # Custom email-based authentication backend
│   └── templates/        # HTML templates
├── static/
│   └── assets/           # Static files (CSS, JS, images)
├── templates/
│   ├── base.html         # Base template
│   ├── login.html        # Login page
│   ├── user_profile.html # User profile page
│   └── map.html          # Map view
├── manage.py             # Django management script
└── README.md             # Project documentation
```

---