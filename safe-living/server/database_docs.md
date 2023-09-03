# House Rental App Database Documentation

## Table of Contents

1. [Users](#users)
2. [Properties](#properties)
3. [Bookings](#bookings)
4. [Leases](#leases)
5. [Messages](#messages)
6. [Maintenance Requests](#maintenance-requests)

## Users

The Users table stores information about the users of the House Rental App.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the user |
| username | String | User's username |
| email | String | User's email address |
| password | String | User's password (hashed) |
| role | String | User's role (tenant, landlord, admin) |

## Properties

The Properties table stores information about the rental properties listed on the House Rental App.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the property |
| title | String | Property title |
| description | String | Property description |
| price | Decimal | Rental price per month |
| bedrooms | Integer | Number of bedrooms |
| location | String | Property location |
| amenities | String | Property amenities |
| landlord_id | Integer | Foreign key referencing the landlord's user id |

## Bookings

The Bookings table stores information about the booking requests made by tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the booking |
| property_id | Integer | Foreign key referencing the property id |
| tenant_id | Integer | Foreign key referencing the tenant's user id |
| status | String | Booking status (pending, approved, rejected) |

## Leases

The Leases table stores information about the lease agreements between landlords and tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the lease |
| property_id | Integer | Foreign key referencing the property id |
| tenant_id | Integer | Foreign key referencing the tenant's user id |
| start_date | Date | Start date of the lease |
| end_date | Date | End date of the lease |

## Messages

The Messages table stores information about the messages exchanged between users.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the message |
| sender_id | Integer | Foreign key referencing the sender's user id |
| receiver_id | Integer | Foreign key referencing the receiver's user id |
| content | String | Message content |
| timestamp | DateTime | Timestamp of when the message was sent |

## Maintenance Requests

The Maintenance Requests table stores information about the maintenance requests made by tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the maintenance request |
| property_id | Integer | Foreign key referencing the property id |
| tenant_id | Integer | Foreign key referencing the tenant's user id |
| description | String | Description of the maintenance issue |
| status | String | Maintenance request status (pending, in progress, completed) |
# House Rental App Database Documentation

## Table of Contents

1. [Users](#users)
2. [Properties](#properties)
3. [Bookings](#bookings)
4. [Leases](#leases)
5. [Messages](#messages)
6. [Maintenance Requests](#maintenance-requests)

## Users

The Users table stores information about the users of the House Rental App.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the user |
| username | String | User's username |
| email | String | User's email address |
| password | String | User's password (hashed) |
| role | String | User's role (tenant, landlord, admin) |

## Properties

The Properties table stores information about the rental properties listed on the House Rental App.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the property |
| title | String | Property title |
| description | String | Property description |
| price | Decimal | Rental price per month |
| bedrooms | Integer | Number of bedrooms |
| location | String | Property location |
| amenities | String | Property amenities |
| landlord_id | Integer | Foreign key referencing the landlord's user id |

## Bookings

The Bookings table stores information about the booking requests made by tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the booking |
| property_id | Integer | Foreign key referencing the property id |
| tenant_id | Integer | Foreign key referencing the tenant's user id |
| status | String | Booking status (pending, approved, rejected) |

## Leases

The Leases table stores information about the lease agreements between landlords and tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the lease |
| property_id | Integer | Foreign key referencing the property id |
| tenant_id | Integer | Foreign key referencing the tenant's user id |
| start_date | Date | Start date of the lease |
| end_date | Date | End date of the lease |

## Messages

The Messages table stores information about the messages exchanged between users.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the message |
| sender_id | Integer | Foreign key referencing the sender's user id |
| receiver_id | Integer | Foreign key referencing the receiver's user id |
| content | String | Message content |
| timestamp | DateTime | Timestamp of when the message was sent |

## Maintenance Requests

The Maintenance Requests table stores information about the maintenance requests made by tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the maintenance request |
| property_id | Integer | Foreign key referencing the property id |
| tenant_id | Integer | Foreign key referencing the tenant's user id |
| description | String | Description of the maintenance issue |
| status | String | Maintenance request status (pending, in progress, completed) |
