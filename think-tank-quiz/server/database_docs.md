# Database Documentation

## Table 1: Users

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each user |
| username    | String   | User's username |
| email       | String   | User's email address |
| password    | String   | User's password (hashed) |

## Table 2: Quizzes

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each quiz |
| title       | String   | Title of the quiz |
| category    | String   | Category of the quiz |
| difficulty  | String   | Difficulty level of the quiz |

## Table 3: Questions

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each question |
| quiz_id     | Integer  | ID of the quiz the question belongs to |
| question    | String   | The question text |
| option1     | String   | Option 1 for the question |
| option2     | String   | Option 2 for the question |
| option3     | String   | Option 3 for the question |
| option4     | String   | Option 4 for the question |
| correct_option | Integer | The correct option for the question |

## Table 4: Quiz Results

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each quiz result |
| user_id     | Integer  | ID of the user who took the quiz |
| quiz_id     | Integer  | ID of the quiz |
| score       | Integer  | Score achieved by the user |

# Database Documentation

## Table 1: Users

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each user |
| username    | String   | User's username |
| email       | String   | User's email address |
| password    | String   | User's password (hashed) |

## Table 2: Quizzes

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each quiz |
| title       | String   | Title of the quiz |
| category    | String   | Category of the quiz |
| difficulty  | String   | Difficulty level of the quiz |

## Table 3: Questions

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each question |
| quiz_id     | Integer  | ID of the quiz the question belongs to |
| question    | String   | The question text |
| option1     | String   | Option 1 for the question |
| option2     | String   | Option 2 for the question |
| option3     | String   | Option 3 for the question |
| option4     | String   | Option 4 for the question |
| correct_option | Integer | The correct option for the question |

## Table 4: Quiz Results

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id          | Integer  | Unique ID for each quiz result |
| user_id     | Integer  | ID of the user who took the quiz |
| quiz_id     | Integer  | ID of the quiz |
| score       | Integer  | Score achieved by the user |

