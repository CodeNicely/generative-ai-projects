# Database Documentation

## Table: Users

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Primary key |
| username    | String   | User's username |
| password    | String   | User's password |
| email       | String   | User's email address |

## Table: Expenses

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Primary key |
| user_id     | Integer  | Foreign key referencing the Users table |
| date        | Date     | Date of the expense |
| amount      | Decimal  | Amount spent |
| category    | String   | Category of the expense |
| description | String   | Description of the expense |
| payment_method | String | Payment method used |

## Table: Attachments

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Primary key |
| expense_id  | Integer  | Foreign key referencing the Expenses table |
| file_path   | String   | File path of the attachment |

# Database Documentation

## Table: Users

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Primary key |
| username    | String   | User's username |
| password    | String   | User's password |
| email       | String   | User's email address |

## Table: Expenses

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Primary key |
| user_id     | Integer  | Foreign key referencing the Users table |
| date        | Date     | Date of the expense |
| amount      | Decimal  | Amount spent |
| category    | String   | Category of the expense |
| description | String   | Description of the expense |
| payment_method | String | Payment method used |

## Table: Attachments

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Primary key |
| expense_id  | Integer  | Foreign key referencing the Expenses table |
| file_path   | String   | File path of the attachment |

