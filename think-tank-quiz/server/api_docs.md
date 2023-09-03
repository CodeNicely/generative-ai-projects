# API Documentation

## Base URL

The base URL for all API endpoints is: `https://quiz-competition.com/api`

## Authentication

All API endpoints require authentication using a JWT token. To authenticate, include the JWT token in the `Authorization` header of the request.

Example:

```
Authorization: Bearer <JWT_TOKEN>
```

## Endpoints

### User Registration

**Endpoint:** `/register`

**Method:** POST

**Description:** Register a new user

**Request Body:**

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123"
}
```

**Response:**

```json
{
  "message": "User registered successfully",
  "user_id": 123
}
```

### User Login

**Endpoint:** `/login`

**Method:** POST

**Description:** Login a user

**Request Body:**

```json
{
  "username": "john_doe",
  "password": "password123"
}
```

**Response:**

```json
{
  "message": "Login successful",
  "token": "<JWT_TOKEN>",
  "user_id": 123
}
```

### Get Quiz Categories

**Endpoint:** `/categories`

**Method:** GET

**Description:** Get a list of available quiz categories

**Response:**

```json
{
  "categories": [
    "Science",
    "History",
    "Sports",
    "Geography"
  ]
}
```

### Get Quizzes

**Endpoint:** `/quizzes`

**Method:** GET

**Description:** Get a list of quizzes

**Query Parameters:**

- `category` (optional): Filter quizzes by category
- `difficulty` (optional): Filter quizzes by difficulty level

**Response:**

```json
{
  "quizzes": [
    {
      "id": 1,
      "title": "Quiz 1",
      "category": "Science",
      "difficulty": "Easy"
    },
    {
      "id": 2,
      "title": "Quiz 2",
      "category": "History",
      "difficulty": "Medium"
    }
  ]
}
```

### Get Quiz Details

**Endpoint:** `/quizzes/{quiz_id}`

**Method:** GET

**Description:** Get details of a specific quiz

**Response:**

```json
{
  "id": 1,
  "title": "Quiz 1",
  "category": "Science",
  "difficulty": "Easy",
  "questions": [
    {
      "id": 1,
      "question": "Question 1",
      "options": [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
      ]
    },
    {
      "id": 2,
      "question": "Question 2",
      "options": [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
      ]
    }
  ]
}
```

### Submit Quiz

**Endpoint:** `/quizzes/{quiz_id}/submit`

**Method:** POST

**Description:** Submit a quiz

**Request Body:**

```json
{
  "answers": [
    {
      "question_id": 1,
      "selected_option": 2
    },
    {
      "question_id": 2,
      "selected_option": 3
    }
  ]
}
```

**Response:**

```json
{
  "message": "Quiz submitted successfully",
  "score": 80
}
```

### Get User Quiz Results

**Endpoint:** `/users/{user_id}/results`

**Method:** GET

**Description:** Get quiz results for a specific user

**Response:**

```json
{
  "results": [
    {
      "quiz_id": 1,
      "quiz_title": "Quiz 1",
      "score": 80
    },
    {
      "quiz_id": 2,
      "quiz_title": "Quiz 2",
      "score": 90
    }
  ]
}
```

### Get Quiz Leaderboard

**Endpoint:** `/quizzes/{quiz_id}/leaderboard`

**Method:** GET

**Description:** Get the leaderboard for a specific quiz

**Response:**

```json
{
  "leaderboard": [
    {
      "user_id": 1,
      "username": "john_doe",
      "score": 80
    },
    {
      "user_id": 2,
      "username": "jane_smith",
      "score": 90
    }
  ]
}
```

### Create Quiz

**Endpoint:** `/quizzes/create`

**Method:** POST

**Description:** Create a new quiz

**Request Body:**

```json
{
  "title": "Quiz 3",
  "category": "Science",
  "difficulty": "Medium",
  "questions": [
    {
      "question": "Question 1",
      "options": [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
      ],
      "correct_option": 2
    },
    {
      "question": "Question 2",
      "options": [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
      ],
      "correct_option": 3
    }
  ]
}
```

**Response:**

```json
{
  "message": "Quiz created successfully",
  "quiz_id": 3
}
```

### Update Quiz

**Endpoint:** `/quizzes/{quiz_id}/update`

**Method:** PUT

**Description:** Update an existing quiz

**Request Body:**

```json
{
  "title": "Updated Quiz",
  "category": "Science",
  "difficulty": "Hard",
  "questions": [
    {
      "question": "Updated Question 1",
      "options": [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
      ],
      "correct_option": 3
    },
    {
      "question": "Updated Question 2",
      "options": [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
      ],
      "correct_option": 4
    }
  ]
}
```

**Response:**

```json
{
  "message": "Quiz updated successfully"
}
```

### Delete Quiz

**Endpoint:** `/quizzes/{quiz_id}/delete`

**Method:** DELETE

**Description:** Delete an existing quiz

**Response:**

```json
{
  "message": "Quiz deleted successfully"
}
```
