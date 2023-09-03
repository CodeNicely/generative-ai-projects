# API Documentation

## Base URL

The base URL for all API endpoints is `https://example.com/api/`

## Endpoints

### 1. User Registration

- URL: `/users/register/`
- Method: `POST`
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
    "id": "integer",
    "username": "string",
    "email": "string"
  }
  ```

### 2. User Login

- URL: `/users/login/`
- Method: `POST`
- Description: Log in a user
- Request Body:
  ```
  {
    "username": "string",
    "password": "string"
  }
  ```
- Response Body:
  ```
  {
    "token": "string"
  }
  ```

### 3. Product Listing

- URL: `/products/`
- Method: `GET`
- Description: Get a list of all products
- Response Body:
  ```
  [
    {
      "id": "integer",
      "name": "string",
      "description": "string",
      "price": "decimal"
    }
  ]
  ```

### 4. Add to Cart

- URL: `/cart/add/`
- Method: `POST`
- Description: Add a product to the user's cart
- Request Body:
  ```
  {
    "product_id": "integer",
    "quantity": "integer"
  }
  ```
- Response Body:
  ```
  {
    "message": "string"
  }
  ```

### 5. Checkout

- URL: `/cart/checkout/`
- Method: `POST`
- Description: Process the user's cart and create an order
- Request Body:
  ```
  {
    "shipping_address": "string",
    "payment_method": "string"
  }
  ```
- Response Body:
  ```
  {
    "order_id": "integer",
    "total_price": "decimal"
  }
  ```

### 6. Order History

- URL: `/orders/`
- Method: `GET`
- Description: Get a list of the user's order history
- Response Body:
  ```
  [
    {
      "order_id": "integer",
      "total_price": "decimal",
      "status": "string"
    }
  ]
  ```

### 7. Order Details

- URL: `/orders/{order_id}/`
- Method: `GET`
- Description: Get the details of a specific order
- Response Body:
  ```
  {
    "order_id": "integer",
    "total_price": "decimal",
    "status": "string",
    "products": [
      {
        "product_id": "integer",
        "name": "string",
        "quantity": "integer",
        "price": "decimal"
      }
    ]
  }
  ```

### 8. Product Recommendations

- URL: `/products/recommendations/`
- Method: `GET`
- Description: Get personalized product recommendations for the user
- Response Body:
  ```
  [
    {
      "id": "integer",
      "name": "string",
      "description": "string",
      "price": "decimal"
    }
  ]
  ```

### 9. Product Reviews

- URL: `/products/{product_id}/reviews/`
- Method: `GET`
- Description: Get the reviews for a specific product
- Response Body:
  ```
  [
    {
      "review_id": "integer",
      "user_id": "integer",
      "username": "string",
      "rating": "integer",
      "comment": "string"
    }
  ]
  ```

### 10. Customer Support

- URL: `/support/`
- Method: `POST`
- Description: Send a message to customer support
- Request Body:
  ```
  {
    "message": "string"
  }
  ```
- Response Body:
  ```
  {
    "message": "string"
  }
  ```
# API Documentation

## Base URL

The base URL for all API endpoints is `https://example.com/api/`

## Endpoints

### 1. User Registration

- URL: `/users/register/`
- Method: `POST`
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
    "id": "integer",
    "username": "string",
    "email": "string"
  }
  ```

### 2. User Login

- URL: `/users/login/`
- Method: `POST`
- Description: Log in a user
- Request Body:
  ```
  {
    "username": "string",
    "password": "string"
  }
  ```
- Response Body:
  ```
  {
    "token": "string"
  }
  ```

### 3. Product Listing

- URL: `/products/`
- Method: `GET`
- Description: Get a list of all products
- Response Body:
  ```
  [
    {
      "id": "integer",
      "name": "string",
      "description": "string",
      "price": "decimal"
    }
  ]
  ```

### 4. Add to Cart

- URL: `/cart/add/`
- Method: `POST`
- Description: Add a product to the user's cart
- Request Body:
  ```
  {
    "product_id": "integer",
    "quantity": "integer"
  }
  ```
- Response Body:
  ```
  {
    "message": "string"
  }
  ```

### 5. Checkout

- URL: `/cart/checkout/`
- Method: `POST`
- Description: Process the user's cart and create an order
- Request Body:
  ```
  {
    "shipping_address": "string",
    "payment_method": "string"
  }
  ```
- Response Body:
  ```
  {
    "order_id": "integer",
    "total_price": "decimal"
  }
  ```

### 6. Order History

- URL: `/orders/`
- Method: `GET`
- Description: Get a list of the user's order history
- Response Body:
  ```
  [
    {
      "order_id": "integer",
      "total_price": "decimal",
      "status": "string"
    }
  ]
  ```

### 7. Order Details

- URL: `/orders/{order_id}/`
- Method: `GET`
- Description: Get the details of a specific order
- Response Body:
  ```
  {
    "order_id": "integer",
    "total_price": "decimal",
    "status": "string",
    "products": [
      {
        "product_id": "integer",
        "name": "string",
        "quantity": "integer",
        "price": "decimal"
      }
    ]
  }
  ```

### 8. Product Recommendations

- URL: `/products/recommendations/`
- Method: `GET`
- Description: Get personalized product recommendations for the user
- Response Body:
  ```
  [
    {
      "id": "integer",
      "name": "string",
      "description": "string",
      "price": "decimal"
    }
  ]
  ```

### 9. Product Reviews

- URL: `/products/{product_id}/reviews/`
- Method: `GET`
- Description: Get the reviews for a specific product
- Response Body:
  ```
  [
    {
      "review_id": "integer",
      "user_id": "integer",
      "username": "string",
      "rating": "integer",
      "comment": "string"
    }
  ]
  ```

### 10. Customer Support

- URL: `/support/`
- Method: `POST`
- Description: Send a message to customer support
- Request Body:
  ```
  {
    "message": "string"
  }
  ```
- Response Body:
  ```
  {
    "message": "string"
  }
  ```
