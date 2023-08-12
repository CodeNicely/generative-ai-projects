# API Documentation

## User

### Register

- Endpoint: `/api/register`
- Method: POST
- Request Body:
  - email: String (required)
  - password: String (required)

### Login

- Endpoint: `/api/login`
- Method: POST
- Request Body:
  - email: String (required)
  - password: String (required)

## Task

### Create Task

- Endpoint: `/api/tasks`
- Method: POST
- Request Body:
  - title: String (required)
  - description: String
  - priority: String
  - due_date: Date

### Update Task

- Endpoint: `/api/tasks/{task_id}`
- Method: PUT
- Request Body:
  - title: String
  - description: String
  - priority: String
  - status: String
  - due_date: Date

### Delete Task

- Endpoint: `/api/tasks/{task_id}`
- Method: DELETE

### Get Task

- Endpoint: `/api/tasks/{task_id}`
- Method: GET

### Get All Tasks

- Endpoint: `/api/tasks`
- Method: GET

### Filter Tasks

- Endpoint: `/api/tasks/filter`
- Method: GET
- Query Parameters:
  - status: String
  - priority: String
  - due_date: Date

### Sort Tasks

- Endpoint: `/api/tasks/sort`
- Method: GET
- Query Parameters:
  - sort_by: String
  - sort_order: String
