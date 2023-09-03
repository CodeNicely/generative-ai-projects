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
| category    | String   | Product category |
| price       | Decimal  | Product price |

## Table 3: Orders

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each order |
| user_id     | Integer  | ID of the user who placed the order |
| product_id  | Integer  | ID of the product in the order |
| quantity    | Integer  | Quantity of the product in the order |
| status      | String   | Status of the order (e.g., processing, delivered) |

## Table 4: Stores

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each store |
| name        | String   | Store name |
| address     | String   | Store address |

## Table 5: Delivery Personnel

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each delivery personnel |
| name        | String   | Delivery personnel's name |
| vehicle     | String   | Type of vehicle used for delivery |

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
| category    | String   | Product category |
| price       | Decimal  | Product price |

## Table 3: Orders

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each order |
| user_id     | Integer  | ID of the user who placed the order |
| product_id  | Integer  | ID of the product in the order |
| quantity    | Integer  | Quantity of the product in the order |
| status      | String   | Status of the order (e.g., processing, delivered) |

## Table 4: Stores

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each store |
| name        | String   | Store name |
| address     | String   | Store address |

## Table 5: Delivery Personnel

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each delivery personnel |
| name        | String   | Delivery personnel's name |
| vehicle     | String   | Type of vehicle used for delivery |

