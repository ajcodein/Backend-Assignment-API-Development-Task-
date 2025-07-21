# Backend-Assignment-API-Development-Task-
# KPA Assignment - Backend API

This project implements **two APIs** from the provided KPA Form Data collection using **Django REST Framework (DRF)** and **PostgreSQL**.  
It demonstrates a fully functional backend for form submission and retrieval that integrates seamlessly with the given frontend.

---

## **Setup Instructions**

1. **Clone the repository**
   ```bash
   git clone https://github.com/<ajcodein>/kpa_backend.git
   cd kpa_backend
Install dependencies
      pip install -r requirements.txt
      
Configure PostgreSQL
      Create a database (e.g., kpa_db) in PostgreSQL.
      Create a .env file in the project root:
            SECRET_KEY=your-secret-key
            DB_NAME=kpa_db
            DB_USER=postgres
            DB_PASSWORD=your_password
            DB_HOST=localhost
            DB_PORT=5432
Apply migrations
       python manage.py makemigrations
       python manage.py migrate
Run the server
        python manage.py runserver
Test APIs using Postman
       POST http://127.0.0.1:8000/api/form/
       GET http://127.0.0.1:8000/api/form/{id}/

Tech Stack
      Backend: Django 5, Django REST Framework
      Database: PostgreSQL
      Environment Management: python-decouple for .env configs
      Tools: Postman for testing, GitHub for version control       
      

Implemented APIs
      1. POST /api/form/
          Description: Creates a new form submission.

              Request Body:

              json
                   {
                    "name": "Ajesh",
                    "phone": "5678908769",
                    "email": "ajesh@example.com"
                    }
                Response:
                        {
                          "id": 1,
                          "name": "Ajesh",
                          "phone": "5678908769",
                          "email": "ajesh@example.com",
                          "document": null,
                          "created_at": "2025-07-21T11:00:00Z"
                        }

2. GET /api/form/{id}/
         Description: Retrieves form details by ID.

              Response Example:

                  json

                    {
                      "id": 1,
                      "name": "Ajesh",
                      "phone": "7760873976",
                      "email": "ajesh@example.com",
                      "document": null,
                      "created_at": "2025-07-21T11:00:00Z"
                    }


Limitations & Assumptions
    Authentication/authorization is not implemented as per assignment scope.
    phone is optional (null=True, blank=True).
    File uploads (document) are supported but not mandatory.
    Designed for local development; production deployment not configured.
                        

                    




