# Database Documentation

## User Profile

- id: Integer
- username: String
- email: String
- password: String
- contact_number: String
- is_verified: Boolean
- is_active: Boolean
- created_at: DateTime
- updated_at: DateTime

## Company Profile

- id: Integer
- name: String
- description: Text
- logo: Image
- created_at: DateTime
- updated_at: DateTime

## Document

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- file: File
- created_at: DateTime
- updated_at: DateTime

## Connection

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- connected_user_id: Integer (Foreign Key to User Profile)
- access_level: String
- created_at: DateTime
- updated_at: DateTime

## Post

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- content: Text
- created_at: DateTime
- updated_at: DateTime

## Like

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- post_id: Integer (Foreign Key to Post)
- created_at: DateTime
- updated_at: DateTime

## Comment

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- post_id: Integer (Foreign Key to Post)
- content: Text
- created_at: DateTime
- updated_at: DateTime

## Notification

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- message: Text
- created_at: DateTime
- updated_at: DateTime

## Subscription

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- type: String
- created_at: DateTime
- updated_at: DateTime

## Admin Profile

- id: Integer
- username: String
- email: String
- password: String
- created_at: DateTime
- updated_at: DateTime
# Database Documentation

## User Profile

- id: Integer
- username: String
- email: String
- password: String
- contact_number: String
- is_verified: Boolean
- is_active: Boolean
- created_at: DateTime
- updated_at: DateTime

## Company Profile

- id: Integer
- name: String
- description: Text
- logo: Image
- created_at: DateTime
- updated_at: DateTime

## Document

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- file: File
- created_at: DateTime
- updated_at: DateTime

## Connection

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- connected_user_id: Integer (Foreign Key to User Profile)
- access_level: String
- created_at: DateTime
- updated_at: DateTime

## Post

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- content: Text
- created_at: DateTime
- updated_at: DateTime

## Like

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- post_id: Integer (Foreign Key to Post)
- created_at: DateTime
- updated_at: DateTime

## Comment

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- post_id: Integer (Foreign Key to Post)
- content: Text
- created_at: DateTime
- updated_at: DateTime

## Notification

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- message: Text
- created_at: DateTime
- updated_at: DateTime

## Subscription

- id: Integer
- user_id: Integer (Foreign Key to User Profile)
- type: String
- created_at: DateTime
- updated_at: DateTime

## Admin Profile

- id: Integer
- username: String
- email: String
- password: String
- created_at: DateTime
- updated_at: DateTime
