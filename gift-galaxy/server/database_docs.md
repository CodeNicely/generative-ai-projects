# Database Documentation

## Table 1: Users

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each user |
| username    | String   | User's username |
| email       | String   | User's email address |
| password    | String   | User's password (hashed) |

## Table 2: Products

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each product |
| name        | String   | Product name |
| description | String   | Product description |
| price       | Decimal  | Product price |

## Table 3: Orders

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each order |
| user_id     | Integer  | ID of the user who placed the order |
| product_id  | Integer  | ID of the product in the order |
| quantity    | Integer  | Quantity of the product in the order |
| total_price | Decimal  | Total price of the order |

## Table 4: Shipping Addresses

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each shipping address |
| user_id     | Integer  | ID of the user who owns the address |
| address     | String   | Shipping address |

## Table 5: Payments

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each payment |
| user_id     | Integer  | ID of the user who made the payment |
| order_id    | Integer  | ID of the order associated with the payment |
| amount      | Decimal  | Payment amount |

# Database Documentation

## Table 1: Users

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each user |
| username    | String   | User's username |
| email       | String   | User's email address |
| password    | String   | User's password (hashed) |

## Table 2: Products

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each product |
| name        | String   | Product name |
| description | String   | Product description |
| price       | Decimal  | Product price |

## Table 3: Orders

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each order |
| user_id     | Integer  | ID of the user who placed the order |
| product_id  | Integer  | ID of the product in the order |
| quantity    | Integer  | Quantity of the product in the order |
| total_price | Decimal  | Total price of the order |

## Table 4: Shipping Addresses

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each shipping address |
| user_id     | Integer  | ID of the user who owns the address |
| address     | String   | Shipping address |

## Table 5: Payments

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each payment |
| user_id     | Integer  | ID of the user who made the payment |
| order_id    | Integer  | ID of the order associated with the payment |
| amount      | Decimal  | Payment amount |

