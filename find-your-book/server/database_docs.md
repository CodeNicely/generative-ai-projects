# Database Documentation

## Table 1: Users

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| user_id     | Integer  | Unique ID for each user |
| name        | String   | User's name |
| email       | String   | User's email address |
| password    | String   | User's password (hashed) |

## Table 2: Books

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| book_id     | Integer  | Unique ID for each book |
| title       | String   | Title of the book |
| author      | String   | Author of the book |
| genre       | String   | Genre of the book |
| price       | Float    | Price of the book |

## Table 3: Bookstores

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| store_id    | Integer  | Unique ID for each bookstore |
| name        | String   | Name of the bookstore |
| location    | String   | Location of the bookstore |
| contact     | String   | Contact information of the bookstore |

## Table 4: Reviews

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| review_id   | Integer  | Unique ID for each review |
| book_id     | Integer  | ID of the reviewed book |
| user_id     | Integer  | ID of the user who wrote the review |
| rating      | Integer  | Rating given by the user (1-5) |
| comment     | String   | Comment written by the user |
# Database Documentation

## Table 1: Users

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| user_id     | Integer  | Unique ID for each user |
| name        | String   | User's name |
| email       | String   | User's email address |
| password    | String   | User's password (hashed) |

## Table 2: Books

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| book_id     | Integer  | Unique ID for each book |
| title       | String   | Title of the book |
| author      | String   | Author of the book |
| genre       | String   | Genre of the book |
| price       | Float    | Price of the book |

## Table 3: Bookstores

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| store_id    | Integer  | Unique ID for each bookstore |
| name        | String   | Name of the bookstore |
| location    | String   | Location of the bookstore |
| contact     | String   | Contact information of the bookstore |

## Table 4: Reviews

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| review_id   | Integer  | Unique ID for each review |
| book_id     | Integer  | ID of the reviewed book |
| user_id     | Integer  | ID of the user who wrote the review |
| rating      | Integer  | Rating given by the user (1-5) |
| comment     | String   | Comment written by the user |
