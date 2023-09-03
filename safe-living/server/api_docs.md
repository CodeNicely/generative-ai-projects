# House Rental App API Documentation

## Table of Contents

1. [Authentication](#authentication)
2. [Users](#users)
3. [Properties](#properties)
4. [Bookings](#bookings)
5. [Leases](#leases)
6. [Messages](#messages)
7. [Maintenance Requests](#maintenance-requests)

## Authentication

### Register User

Endpoint: `/api/register`

Method: `POST`

Request Body:

```json
{
  "username": "string",
  "email": "string",
  "password": "string",
  "role": "string"
}
```

### Login User

Endpoint: `/api/login`

Method: `POST`

Request Body:

```json
{
  "username": "string",
  "password": "string"
}
```

### Logout User

Endpoint: `/api/logout`

Method: `POST`

### Get Current User

Endpoint: `/api/user`

Method: `GET`

## Users

### Get User

Endpoint: `/api/users/{user_id}`

Method: `GET`

### Update User

Endpoint: `/api/users/{user_id}`

Method: `PUT`

Request Body:

```json
{
  "username": "string",
  "email": "string",
  "password": "string",
  "role": "string"
}
```

### Delete User

Endpoint: `/api/users/{user_id}`

Method: `DELETE`

## Properties

### Get All Properties

Endpoint: `/api/properties`

Method: `GET`

### Get Property

Endpoint: `/api/properties/{property_id}`

Method: `GET`

### Create Property

Endpoint: `/api/properties`

Method: `POST`

Request Body:

```json
{
  "title": "string",
  "description": "string",
  "price": "number",
  "bedrooms": "number",
  "location": "string",
  "amenities": "string",
  "landlord_id": "number"
}
```

### Update Property

Endpoint: `/api/properties/{property_id}`

Method: `PUT`

Request Body:

```json
{
  "title": "string",
  "description": "string",
  "price": "number",
  "bedrooms": "number",
  "location": "string",
  "amenities": "string",
  "landlord_id": "number"
}
```

### Delete Property

Endpoint: `/api/properties/{property_id}`

Method: `DELETE`

## Bookings

### Get All Bookings

Endpoint: `/api/bookings`

Method: `GET`

### Get Booking

Endpoint: `/api/bookings/{booking_id}`

Method: `GET`

### Create Booking

Endpoint: `/api/bookings`

Method: `POST`

Request Body:

```json
{
  "property_id": "number",
  "tenant_id": "number"
}
```

### Update Booking

Endpoint: `/api/bookings/{booking_id}`

Method: `PUT`

Request Body:

```json
{
  "status": "string"
}
```

### Delete Booking

Endpoint: `/api/bookings/{booking_id}`

Method: `DELETE`

## Leases

### Get All Leases

Endpoint: `/api/leases`

Method: `GET`

### Get Lease

Endpoint: `/api/leases/{lease_id}`

Method: `GET`

### Create Lease

Endpoint: `/api/leases`

Method: `POST`

Request Body:

```json
{
  "property_id": "number",
  "tenant_id": "number",
  "start_date": "string",
  "end_date": "string"
}
```

### Update Lease

Endpoint: `/api/leases/{lease_id}`

Method: `PUT`

Request Body:

```json
{
  "start_date": "string",
  "end_date": "string"
}
```

### Delete Lease

Endpoint: `/api/leases/{lease_id}`

Method: `DELETE`

## Messages

### Get All Messages

Endpoint: `/api/messages`

Method: `GET`

### Get Message

Endpoint: `/api/messages/{message_id}`

Method: `GET`

### Create Message

Endpoint: `/api/messages`

Method: `POST`

Request Body:

```json
{
  "sender_id": "number",
  "receiver_id": "number",
  "content": "string"
}
```

### Delete Message

Endpoint: `/api/messages/{message_id}`

Method: `DELETE`

## Maintenance Requests

### Get All Maintenance Requests

Endpoint: `/api/maintenance-requests`

Method: `GET`

### Get Maintenance Request

Endpoint: `/api/maintenance-requests/{request_id}`

Method: `GET`

### Create Maintenance Request

Endpoint: `/api/maintenance-requests`

Method: `POST`

Request Body:

```json
{
  "property_id": "number",
  "tenant_id": "number",
  "description": "string"
}
```

### Update Maintenance Request

Endpoint: `/api/maintenance-requests/{request_id}`

Method: `PUT`

Request Body:

```json
{
  "status": "string"
}
```

### Delete Maintenance Request

Endpoint: `/api/maintenance-requests/{request_id}`

Method: `DELETE`
