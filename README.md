PROJECT DESCRIPTION
This project is a simple public API built using Django and Django REST Framework. It provides basic information including:

1. My registered HNG12 email.
2. The current datetime in ISO 8601 format (UTC).
3. The GitHub URL of this repository.
The API is deployed and publicly accessible for testing.

FEATURES
1. GET request to retrieve JSON response.
2. Dynamically generated current_datetime in ISO 8601 format.
3. CORS Handling for cross-origin requests

TECHNOLOGY USED
1. Backend: Django, Django REST Framework (DRF)
2. Database: SQLite (default for Django)
3. Deployment: Render (or your chosen platform)
4. Version Control: Git & GitHub

Installation & Setup
1. Clone the Repository
git clone https://github.com/okonkwo348/API-Basic-Information/tree/master
2. Create a Virtual Environment (Optional but Recommended)
# On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run Migrations
python manage.py migrate
5. Start the Development Server
python manage.py runserver

API Documentation
Endpoint:http://127.0.0.1:8000/api/infor/

Response Example (200 OK)
{
    "email": "okonkwoemmanuel348@gmail.com",
    "current_datetime": "2025-01-29T11:32:48.792889Z",
    "github_url": "https://github.com/okonkwo348"
<<<<<<< HEAD
}
=======
}
>>>>>>> b343d64 (Initial commit)
