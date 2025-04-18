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
   cd user_module

2. **Set Up Virtual Environment**:
   Create and activate a virtual environment to isolate dependencies.
    ```bash
   python3 -m venv env
   source env/bin/activate

3. **Install Dependencies**:
   Install all required Python packages listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt

4. **Set Up the Database**:
   Configure a PostgreSQL database with PostGIS extension and update the database settings in the `settings.py` file.
    ```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis', 
            'NAME': 'username',                                
            'USER': 'dbname',                                      
            'PASSWORD': 'password',                                      
            'HOST': 'hostname',                               
            'PORT': 'port',                                  
        }
    }

6. **Load Static Files**:
   Collect all static files for the project.
   ```bash
    python manage.py collectstatic

5. **Run Migrations**:
   Apply database migrations to set up the required tables.
   ```bash
    python manage.py makemigrations

6. **Run Migrate**:
   Apply database migrate to set up the required tables.
   ```bash
    python manage.py migrate

7. **Run the Test Case**:
   Apply the test cases.
   ```bash
    python manage.py test

8. **Run the development server**:
   Start the Django development server to access the application.
   ```bash
    python manage.py runserver 0.0.0.0:8000

8. **Access the Application**:
   Open your browser and navigate to the local server URL.

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
- Ensure the Google Maps API key is configured in the `settings.py` file.

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