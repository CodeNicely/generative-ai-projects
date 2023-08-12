# API Documentation

## User Endpoints

### Register User

- URL: `/api/register`
- Method: POST
- Request Body:
  ```
  {
    "username": "string",
    "email": "string",
    "password": "string",
    "contact_number": "string"
  }
  ```
- Response:
  ```
  {
    "message": "User registered successfully",
    "data": {
      "id": 1,
      "username": "string",
      "email": "string",
      "contact_number": "string"
    }
  }
  ```

### Login User

- URL: `/api/login`
- Method: POST
- Request Body:
  ```
  {
    "email": "string",
    "password": "string"
  }
  ```
- Response:
  ```
  {
    "message": "User logged in successfully",
    "data": {
      "id": 1,
      "username": "string",
      "email": "string",
      "contact_number": "string"
    }
  }
  ```

### Forgot Password

- URL: `/api/forgot-password`
- Method: POST
- Request Body:
  ```
  {
    "email": "string"
  }
  ```
- Response:
  ```
  {
    "message": "Password reset link sent to email"
  }
  ```

## Company Endpoints

### Create Company Profile

- URL: `/api/company/create`
- Method: POST
- Request Body:
  ```
  {
    "name": "string",
    "description": "string",
    "logo": "file"
  }
  ```
- Response:
  ```
  {
    "message": "Company profile created successfully",
    "data": {
      "id": 1,
      "name": "string",
      "description": "string",
      "logo": "string"
    }
  }
  ```

### Get Company Profile

- URL: `/api/company/{company_id}`
- Method: GET
- Response:
  ```
  {
    "id": 1,
    "name": "string",
    "description": "string",
    "logo": "string"
  }
  ```

## Document Endpoints

### Upload Document

- URL: `/api/document/upload`
- Method: POST
- Request Body:
  ```
  {
    "file": "file"
  }
  ```
- Response:
  ```
  {
    "message": "Document uploaded successfully",
    "data": {
      "id": 1,
      "user_id": 1,
      "file": "string"
    }
  }
  ```

### Get Document

- URL: `/api/document/{document_id}`
- Method: GET
- Response:
  ```
  {
    "id": 1,
    "user_id": 1,
    "file": "string"
  }
  ```

## Connection Endpoints

### Send Connection Request

- URL: `/api/connection/send-request`
- Method: POST
- Request Body:
  ```
  {
    "user_id": 1,
    "connected_user_id": 2
  }
  ```
- Response:
  ```
  {
    "message": "Connection request sent successfully",
    "data": {
      "id": 1,
      "user_id": 1,
      "connected_user_id": 2,
      "access_level": "string"
    }
  }
  ```

### Accept Connection Request

- URL: `/api/connection/accept-request/{connection_id}`
- Method: POST
- Response:
  ```
  {
    "message": "Connection request accepted successfully"
  }
  ```

## Post Endpoints

### Create Post

- URL: `/api/post/create`
- Method: POST
- Request Body:
  ```
  {
    "user_id": 1,
    "content": "string"
  }
  ```
- Response:
  ```
  {
    "message": "Post created successfully",
    "data": {
      "id": 1,
      "user_id": 1,
      "content": "string"
    }
  }
  ```

### Like Post

- URL: `/api/post/like/{post_id}`
- Method: POST
- Response:
  ```
  {
    "message": "Post liked successfully"
  }
  ```

### Comment on Post

- URL: `/api/post/comment/{post_id}`
- Method: POST
- Request Body:
  ```
  {
    "user_id": 1,
    "content": "string"
  }
  ```
- Response:
  ```
  {
    "message": "Comment added successfully",
    "data": {
      "id": 1,
      "user_id": 1,
      "post_id": 1,
      "content": "string"
    }
  }
  ```

## Notification Endpoints

### Get Notifications

- URL: `/api/notification`
- Method: GET
- Response:
  ```
  [
    {
      "id": 1,
      "user_id": 1,
      "message": "string"
    }
  ]
  ```

## Subscription Endpoints

### Subscribe User

- URL: `/api/subscription/subscribe`
- Method: POST
- Request Body:
  ```
  {
    "user_id": 1,
    "type": "string"
  }
  ```
- Response:
  ```
  {
    "message": "User subscribed successfully",
    "data": {
      "id": 1,
      "user_id": 1,
      "type": "string"
    }
  }
  ```

### Get Subscription

- URL: `/api/subscription/{user_id}`
- Method: GET
- Response:
  ```
  {
    "id": 1,
    "user_id": 1,
    "type": "string"
  }
  ```

## Admin Endpoints

### Delete Post

- URL: `/api/admin/post/delete/{post_id}`
- Method: DELETE
- Response:
  ```
  {
    "message": "Post deleted successfully"
  }
  ```

### Block User

- URL: `/api/admin/user/block/{user_id}`
- Method: POST
- Response:
  ```
  {
    "message": "User blocked successfully"
  }
  ```
