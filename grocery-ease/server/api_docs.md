# API Documentation

## Base URL

The base URL for all API endpoints is `https://grocerydeliveryapp.com/api`

## Authentication

All API endpoints require authentication using a JWT token. The token should be included in the `Authorization` header of each request in the format `Bearer <token>`.

## Endpoints

### 1. User Registration

- URL: `/users/register`
- Method: POST
- Description: Register a new user
- Request Body:
  ```
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- Response Body:
  ```
  {
    "id": 1,
    "username": "string",
    "email": "string"
  }
  ```

### 2. User Login

- URL: `/users/login`
- Method: POST
- Description: Log in a user
- Request Body:
  ```
  {
    "email": "string",
    "password": "string"
  }
  ```
- Response Body:
  ```
  {
    "token": "string"
  }
  ```

### 3. Get Product List

- URL: `/products`
- Method: GET
- Description: Get a list of all products
- Response Body:
  ```
  [
    {
      "id": 1,
      "name": "string",
      "category": "string",
      "price": 10.99
    }
  ]
  ```

### 4. Add Product to Cart

- URL: `/cart/add`
- Method: POST
- Description: Add a product to the user's cart
- Request Body:
  ```
  {
    "product_id": 1,
    "quantity": 2
  }
  ```
- Response Body:
  ```
  {
    "message": "Product added to cart"
  }
  ```

### 5. Place Order

- URL: `/orders/place`
- Method: POST
- Description: Place an order
- Request Body:
  ```
  {
    "cart_items": [
      {
        "product_id": 1,
        "quantity": 2
      }
    ]
  }
  ```
- Response Body:
  ```
  {
    "message": "Order placed successfully"
  }
  ```

### 6. Track Order

- URL: `/orders/track/{order_id}`
- Method: GET
- Description: Track the status of an order
- Response Body:
  ```
  {
    "order_id": 1,
    "status": "processing"
  }
  ```

### 7. Get Order History

- URL: `/orders/history`
- Method: GET
- Description: Get the order history for the user
- Response Body:
  ```
  [
    {
      "order_id": 1,
      "status": "delivered"
    }
  ]
  ```

### 8. Get Store List

- URL: `/stores`
- Method: GET
- Description: Get a list of all stores
- Response Body:
  ```
  [
    {
      "id": 1,
      "name": "string",
      "address": "string"
    }
  ]
  ```

### 9. Get Delivery Personnel List

- URL: `/delivery-personnel`
- Method: GET
- Description: Get a list of all delivery personnel
- Response Body:
  ```
  [
    {
      "id": 1,
      "name": "string",
      "vehicle": "string"
    }
  ]
  ```

### 10. Get User Profile

- URL: `/users/profile`
- Method: GET
- Description: Get the user's profile
- Response Body:
  ```
  {
    "id": 1,
    "username": "string",
    "email": "string"
  }
  ```

### 11. Update User Profile

- URL: `/users/profile`
- Method: PUT
- Description: Update the user's profile
- Request Body:
  ```
  {
    "username": "string",
    "email": "string"
  }
  ```
- Response Body:
  ```
  {
    "message": "Profile updated successfully"
  }
  ```

### 12. Update User Password

- URL: `/users/password`
- Method: PUT
- Description: Update the user's password
- Request Body:
  ```
  {
    "current_password": "string",
    "new_password": "string"
  }
  ```
- Response Body:
  ```
  {
    "message": "Password updated successfully"
  }
  ```
