# API Documentation

## Authentication

### Register User

- Endpoint: `/api/register`
- Method: POST
- Description: Register a new user
- Request Body:
  ```
  {
    "username": "string",
    "password": "string",
    "email": "string"
  }
  ```
- Response:
  ```
  {
    "message": "string",
    "user": {
      "id": "integer",
      "username": "string",
      "email": "string"
    }
  }
  ```

### Login User

- Endpoint: `/api/login`
- Method: POST
- Description: Login an existing user
- Request Body:
  ```
  {
    "username": "string",
    "password": "string"
  }
  ```
- Response:
  ```
  {
    "message": "string",
    "user": {
      "id": "integer",
      "username": "string",
      "email": "string"
    }
  }
  ```

## Expense Management

### Create Expense

- Endpoint: `/api/expenses`
- Method: POST
- Description: Create a new expense
- Request Body:
  ```
  {
    "date": "string",
    "amount": "number",
    "category": "string",
    "description": "string",
    "payment_method": "string"
  }
  ```
- Response:
  ```
  {
    "message": "string",
    "expense": {
      "id": "integer",
      "date": "string",
      "amount": "number",
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
- Response:
  ```
  {
    "expenses": [
      {
        "id": "integer",
        "date": "string",
        "amount": "number",
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
- Response:
  ```
  {
    "expense": {
      "id": "integer",
      "date": "string",
      "amount": "number",
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
  ```
  {
    "date": "string",
    "amount": "number",
    "category": "string",
    "description": "string",
    "payment_method": "string"
  }
  ```
- Response:
  ```
  {
    "message": "string",
    "expense": {
      "id": "integer",
      "date": "string",
      "amount": "number",
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
- Response:
  ```
  {
    "message": "string"
  }
  ```

### Upload Attachment

- Endpoint: `/api/expenses/{expense_id}/attachments`
- Method: POST
- Description: Upload an attachment for a specific expense
- Request Body: Form data with `file` field
- Response:
  ```
  {
    "message": "string",
    "attachment": {
      "id": "integer",
      "file_path": "string"
    }
  }
  ```

### Get Attachments

- Endpoint: `/api/expenses/{expense_id}/attachments`
- Method: GET
- Description: Get all attachments for a specific expense
- Response:
  ```
  {
    "attachments": [
      {
        "id": "integer",
        "file_path": "string"
      }
    ]
  }
  ```

### Delete Attachment

- Endpoint: `/api/attachments/{attachment_id}`
- Method: DELETE
- Description: Delete a specific attachment
- Response:
  ```
  {
    "message": "string"
  }
  ```
