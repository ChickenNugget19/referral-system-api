# Referral System API

## Description
A Django-based REST API for user registration, login, and referral system. This project allows users to sign up, login, and manage referral codes. It includes:

- User Registration API with a unique referral code.
- User Login API with email and password validation.
- Referral API to view users who signed up using a referral code.

## Features
- User registration with mandatory fields: email, name, mobile number, city, and password.
- Referral code support: if a valid referral code is provided, the user's referrer is recorded.
- User login with email and password.
- Referral system to get users who signed up using your referral code.

## Setup

### Prerequisites
- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/referral-system-api.git
cd referral-system-api

```
2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations to set up the database:
```bash
python manage.py migrate
```
5. Start the development server:
```bash
python manage.py runserver
```
**The API will be available at http://127.0.0.1:8000/**

## Endpoints

1. Register a User (POST /api/users/register/)

Example request body:

```json
Copy code
{
  "email": "test@example.com",
  "name": "John Doe",
  "mobile_number": "1234567890",
  "city": "New York",
  "password": "password123"
}
```
Response:

```json
Copy code
{
  "message": "User registered successfully!",
  "referral_code": "35e3d71a"
}
```
2. Login a User (POST /api/users/login/)

Example request body:

```json
Copy code
{
  "email": "test@example.com",
  "password": "password123"
}
```
Response:

```json
Copy code
{
  "user_id": 1,
  "email": "test@example.com"
}
```
3. Get Referrals (GET /api/users/referrals/)

Example response:

```json
Copy code
[
  {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "registration_date": "2024-11-17T12:00:00"
  }
]
```

## Testing the API
### Using Postman or cURL

You can use tools like Postman or cURL to test the APIs.

1. User Registration

>Endpoint: /api/users/register/
>Method: POST
>Request body: JSON data with the required fields.

Example:

```json
Copy code
{
  "email": "test@example.com",
  "name": "John Doe",
  "mobile_number": "1234567890",
  "city": "New York",
  "password": "password123"
}
```
Response:

```json
Copy code
{
  "message": "User registered successfully!",
  "referral_code": "35e3d71a"
}
```
2. User Login

>Endpoint: /api/users/login/
>Method: POST
>Request body: Email and password.
Example:

```json
Copy code
{
  "email": "test@example.com",
  "password": "password123"
}
```
Response:

```json
Copy code
{
  "user_id": 1,
  "email": "test@example.com"
}
```
3. Get Referrals

>Endpoint: /api/users/referrals/
>Method: GET
>Response:
```json
Copy code
[
  {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "registration_date": "2024-11-17T12:00:00"
  }
]
```
