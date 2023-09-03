# House Rental App API Documentation

## Base URL

The base URL for all API endpoints is `https://api.houserentalapp.com`

## Authentication

All API endpoints require authentication using JSON Web Tokens (JWT). Clients should include the JWT in the `Authorization` header of each request.

## Endpoints

### Users

#### Register User

- Endpoint: `/api/users/register`
- Method: `POST`
- Description: Register a new user
- Request Body:

```json
{
  "username": "example_user",
  "email": "example@example.com",
  "password": "password123",
  "role": "tenant"
}
```

- Response Body:

```json
{
  "id": 1,
  "username": "example_user",
  "email": "example@example.com",
  "role": "tenant"
}
```

#### Login User

- Endpoint: `/api/users/login`
- Method: `POST`
- Description: Login a user
- Request Body:

```json
{
  "email": "example@example.com",
  "password": "password123"
}
```

- Response Body:

```json
{
  "token": "<JWT_TOKEN>"
}
```

### Properties

#### Get All Properties

- Endpoint: `/api/properties`
- Method: `GET`
- Description: Get a list of all properties
- Response Body:

```json
[
  {
    "id": 1,
    "title": "Example Property",
    "description": "Lorem ipsum dolor sit amet",
    "price": 1000,
    "bedrooms": 3,
    "location": "New York",
    "amenities": "Swimming pool, Gym",
    "landlord": {
      "id": 1,
      "username": "example_landlord",
      "email": "landlord@example.com"
    }
  }
]
```

#### Create Property

- Endpoint: `/api/properties`
- Method: `POST`
- Description: Create a new property
- Request Body:

```json
{
  "title": "Example Property",
  "description": "Lorem ipsum dolor sit amet",
  "price": 1000,
  "bedrooms": 3,
  "location": "New York",
  "amenities": "Swimming pool, Gym"
}
```

- Response Body:

```json
{
  "id": 1,
  "title": "Example Property",
  "description": "Lorem ipsum dolor sit amet",
  "price": 1000,
  "bedrooms": 3,
  "location": "New York",
  "amenities": "Swimming pool, Gym",
  "landlord": {
    "id": 1,
    "username": "example_landlord",
    "email": "landlord@example.com"
  }
}
```

### Bookings

#### Create Booking

- Endpoint: `/api/bookings`
- Method: `POST`
- Description: Create a new booking
- Request Body:

```json
{
  "property_id": 1
}
```

- Response Body:

```json
{
  "id": 1,
  "property": {
    "id": 1,
    "title": "Example Property",
    "description": "Lorem ipsum dolor sit amet",
    "price": 1000,
    "bedrooms": 3,
    "location": "New York",
    "amenities": "Swimming pool, Gym",
    "landlord": {
      "id": 1,
      "username": "example_landlord",
      "email": "landlord@example.com"
    }
  },
  "tenant": {
    "id": 1,
    "username": "example_tenant",
    "email": "tenant@example.com"
  },
  "status": "pending"
}
```

### Leases

#### Create Lease

- Endpoint: `/api/leases`
- Method: `POST`
- Description: Create a new lease
- Request Body:

```json
{
  "property_id": 1,
  "start_date": "2022-01-01",
  "end_date": "2022-12-31"
}
```

- Response Body:

```json
{
  "id": 1,
  "property": {
    "id": 1,
    "title": "Example Property",
    "description": "Lorem ipsum dolor sit amet",
    "price": 1000,
    "bedrooms": 3,
    "location": "New York",
    "amenities": "Swimming pool, Gym",
    "landlord": {
      "id": 1,
      "username": "example_landlord",
      "email": "landlord@example.com"
    }
  },
  "tenant": {
    "id": 1,
    "username": "example_tenant",
    "email": "tenant@example.com"
  },
  "start_date": "2022-01-01",
  "end_date": "2022-12-31"
}
```

### Messages

#### Send Message

- Endpoint: `/api/messages`
- Method: `POST`
- Description: Send a message
- Request Body:

```json
{
  "receiver_id": 1,
  "content": "Hello, how are you?"
}
```

- Response Body:

```json
{
  "id": 1,
  "sender": {
    "id": 1,
    "username": "example_user",
    "email": "example@example.com"
  },
  "receiver": {
    "id": 2,
    "username": "example_landlord",
    "email": "landlord@example.com"
  },
  "content": "Hello, how are you?",
  "timestamp": "2022-01-01T12:00:00Z"
}
```

### Maintenance Requests

#### Create Maintenance Request

- Endpoint: `/api/maintenance-requests`
- Method: `POST`
- Description: Create a new maintenance request
- Request Body:

```json
{
  "property_id": 1,
  "description": "There is a leak in the bathroom"
}
```

- Response Body:

```json
{
  "id": 1,
  "property": {
    "id": 1,
    "title": "Example Property",
    "description": "Lorem ipsum dolor sit amet",
    "price": 1000,
    "bedrooms": 3,
    "location": "New York",
    "amenities": "Swimming pool, Gym",
    "landlord": {
      "id": 1,
      "username": "example_landlord",
      "email": "landlord@example.com"
    }
  },
  "tenant": {
    "id": 1,
    "username": "example_tenant",
    "email": "tenant@example.com"
  },
  "description": "There is a leak in the bathroom",
  "status": "pending"
}
```
# House Rental App API Documentation

## Base URL

The base URL for all API endpoints is `https://api.houserentalapp.com`

## Authentication

All API endpoints require authentication using JSON Web Tokens (JWT). Clients should include the JWT in the `Authorization` header of each request.

## Endpoints

### Users

#### Register User

- Endpoint: `/api/users/register`
- Method: `POST`
- Description: Register a new user
- Request Body:

```json
{
  "username": "example_user",
  "email": "example@example.com",
  "password": "password123",
  "role": "tenant"
}
```

- Response Body:

```json
{
  "id": 1,
  "username": "example_user",
  "email": "example@example.com",
  "role": "tenant"
}
```

#### Login User

- Endpoint: `/api/users/login`
- Method: `POST`
- Description: Login a user
- Request Body:

```json
{
  "email": "example@example.com",
  "password": "password123"
}
```

- Response Body:

```json
{
  "token": "<JWT_TOKEN>"
}
```

### Properties

#### Get All Properties

- Endpoint: `/api/properties`
- Method: `GET`
- Description: Get a list of all properties
- Response Body:

```json
[
  {
    "id": 1,
    "title": "Example Property",
    "description": "Lorem ipsum dolor sit amet",
    "price": 1000,
    "bedrooms": 3,
    "location": "New York",
    "amenities": "Swimming pool, Gym",
    "landlord": {
      "id": 1,
      "username": "example_landlord",
      "email": "landlord@example.com"
    }
  }
]
```

#### Create Property

- Endpoint: `/api/properties`
- Method: `POST`
- Description: Create a new property
- Request Body:

```json
{
  "title": "Example Property",
  "description": "Lorem ipsum dolor sit amet",
  "price": 1000,
  "bedrooms": 3,
  "location": "New York",
  "amenities": "Swimming pool, Gym"
}
```

- Response Body:

```json
{
  "id": 1,
  "title": "Example Property",
  "description": "Lorem ipsum dolor sit amet",
  "price": 1000,
  "bedrooms": 3,
  "location": "New York",
  "amenities": "Swimming pool, Gym",
  "landlord": {
    "id": 1,
    "username": "example_landlord",
    "email": "landlord@example.com"
  }
}
```

### Bookings

#### Create Booking

- Endpoint: `/api/bookings`
- Method: `POST`
- Description: Create a new booking
- Request Body:

```json
{
  "property_id": 1
}
```

- Response Body:

```json
{
  "id": 1,
  "property": {
    "id": 1,
    "title": "Example Property",
    "description": "Lorem ipsum dolor sit amet",
    "price": 1000,
    "bedrooms": 3,
    "location": "New York",
    "amenities": "Swimming pool, Gym",
    "landlord": {
      "id": 1,
      "username": "example_landlord",
      "email": "landlord@example.com"
    }
  },
  "tenant": {
    "id": 1,
    "username": "example_tenant",
    "email": "tenant@example.com"
  },
  "status": "pending"
}
```

### Leases

#### Create Lease

- Endpoint: `/api/leases`
- Method: `POST`
- Description: Create a new lease
- Request Body:

```json
{
  "property_id": 1,
  "start_date": "2022-01-01",
  "end_date": "2022-12-31"
}
```

- Response Body:

```json
{
  "id": 1,
  "property": {
    "id": 1,
    "title": "Example Property",
    "description": "Lorem ipsum dolor sit amet",
    "price": 1000,
    "bedrooms": 3,
    "location": "New York",
    "amenities": "Swimming pool, Gym",
    "landlord": {
      "id": 1,
      "username": "example_landlord",
      "email": "landlord@example.com"
    }
  },
  "tenant": {
    "id": 1,
    "username": "example_tenant",
    "email": "tenant@example.com"
  },
  "start_date": "2022-01-01",
  "end_date": "2022-12-31"
}
```

### Messages

#### Send Message

- Endpoint: `/api/messages`
- Method: `POST`
- Description: Send a message
- Request Body:

```json
{
  "receiver_id": 1,
  "content": "Hello, how are you?"
}
```

- Response Body:

```json
{
  "id": 1,
  "sender": {
    "id": 1,
    "username": "example_user",
    "email": "example@example.com"
  },
  "receiver": {
    "id": 2,
    "username": "example_landlord",
    "email": "landlord@example.com"
  },
  "content": "Hello, how are you?",
  "timestamp": "2022-01-01T12:00:00Z"
}
```

### Maintenance Requests

#### Create Maintenance Request

- Endpoint: `/api/maintenance-requests`
- Method: `POST`
- Description: Create a new maintenance request
- Request Body:

```json
{
  "property_id": 1,
  "description": "There is a leak in the bathroom"
}
```

- Response Body:

```json
{
  "id": 1,
  "property": {
    "id": 1,
    "title": "Example Property",
    "description": "Lorem ipsum dolor sit amet",
    "price": 1000,
    "bedrooms": 3,
    "location": "New York",
    "amenities": "Swimming pool, Gym",
    "landlord": {
      "id": 1,
      "username": "example_landlord",
      "email": "landlord@example.com"
    }
  },
  "tenant": {
    "id": 1,
    "username": "example_tenant",
    "email": "tenant@example.com"
  },
  "description": "There is a leak in the bathroom",
  "status": "pending"
}
```
