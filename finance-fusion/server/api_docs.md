# API Documentation

## Authentication

### Register User

- Endpoint: `/api/register`
- Method: POST
- Description: Register a new user
- Request Body:
  ```json
  {
    "username": "string",
    "password": "string",
    "email": "string"
  }
  ```
- Response:
  - Status Code: 201
  - Body:
    ```json
    {
      "message": "User registered successfully",
      "user": {
        "id": 1,
        "username": "string",
        "email": "string"
      }
    }
    ```

### Login

- Endpoint: `/api/login`
- Method: POST
- Description: User login
- Request Body:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- Response:
  - Status Code: 200
  - Body:
    ```json
    {
      "message": "Login successful",
      "user": {
        "id": 1,
        "username": "string",
        "email": "string"
      },
      "token": "string"
    }
    ```

## Expense Management

### Add Expense

- Endpoint: `/api/expenses`
- Method: POST
- Description: Add a new expense
- Request Body:
  ```json
  {
    "date": "string",
    "amount": 0,
    "category": "string",
    "description": "string",
    "payment_method": "string"
  }
  ```
- Headers:
  - Authorization: Bearer {token}
- Response:
  - Status Code: 201
  - Body:
    ```json
    {
      "message": "Expense added successfully",
      "expense": {
        "id": 1,
        "date": "string",
        "amount": 0,
        "category": "string",
        "description": "string",
        "payment_method": "string"
      }
    }
    ```

### Get Expenses

- Endpoint: `/api/expenses`
- Method: GET
- Description: Get all expenses
- Headers:
  - Authorization: Bearer {token}
- Response:
  - Status Code: 200
  - Body:
    ```json
    {
      "expenses": [
        {
          "id": 1,
          "date": "string",
          "amount": 0,
          "category": "string",
          "description": "string",
          "payment_method": "string"
        }
      ]
    }
    ```

### Get Expense

- Endpoint: `/api/expenses/{expense_id}`
- Method: GET
- Description: Get a specific expense
- Headers:
  - Authorization: Bearer {token}
- Response:
  - Status Code: 200
  - Body:
    ```json
    {
      "expense": {
        "id": 1,
        "date": "string",
        "amount": 0,
        "category": "string",
        "description": "string",
        "payment_method": "string"
      }
    }
    ```

### Update Expense

- Endpoint: `/api/expenses/{expense_id}`
- Method: PUT
- Description: Update a specific expense
- Request Body:
  ```json
  {
    "date": "string",
    "amount": 0,
    "category": "string",
    "description": "string",
    "payment_method": "string"
  }
  ```
- Headers:
  - Authorization: Bearer {token}
- Response:
  - Status Code: 200
  - Body:
    ```json
    {
      "message": "Expense updated successfully",
      "expense": {
        "id": 1,
        "date": "string",
        "amount": 0,
        "category": "string",
        "description": "string",
        "payment_method": "string"
      }
    }
    ```

### Delete Expense

- Endpoint: `/api/expenses/{expense_id}`
- Method: DELETE
- Description: Delete a specific expense
- Headers:
  - Authorization: Bearer {token}
- Response:
  - Status Code: 200
  - Body:
    ```json
    {
      "message": "Expense deleted successfully"
    }
    ```
