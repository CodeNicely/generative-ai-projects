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
| title | String | Title of the property listing |
| description | String | Description of the property |
| price | Decimal | Rental price of the property |
| bedrooms | Integer | Number of bedrooms in the property |
| location | String | Location of the property |
| amenities | String | List of amenities available in the property |
| landlord_id | Integer | Foreign key referencing the landlord of the property |

## Bookings

The Bookings table stores information about the booking requests made by tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the booking |
| property_id | Integer | Foreign key referencing the property being booked |
| tenant_id | Integer | Foreign key referencing the tenant making the booking |
| status | String | Status of the booking request (pending, approved, rejected) |

## Leases

The Leases table stores information about the lease agreements between landlords and tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the lease |
| property_id | Integer | Foreign key referencing the property being leased |
| tenant_id | Integer | Foreign key referencing the tenant leasing the property |
| start_date | Date | Start date of the lease |
| end_date | Date | End date of the lease |

## Messages

The Messages table stores information about the messages exchanged between users.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the message |
| sender_id | Integer | Foreign key referencing the sender of the message |
| receiver_id | Integer | Foreign key referencing the receiver of the message |
| content | String | Content of the message |
| timestamp | DateTime | Timestamp of when the message was sent |

## Maintenance Requests

The Maintenance Requests table stores information about the maintenance requests made by tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the maintenance request |
| property_id | Integer | Foreign key referencing the property requiring maintenance |
| tenant_id | Integer | Foreign key referencing the tenant making the request |
| description | String | Description of the maintenance issue |
| status | String | Status of the maintenance request (pending, in progress, completed) |
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
| title | String | Title of the property listing |
| description | String | Description of the property |
| price | Decimal | Rental price of the property |
| bedrooms | Integer | Number of bedrooms in the property |
| location | String | Location of the property |
| amenities | String | List of amenities available in the property |
| landlord_id | Integer | Foreign key referencing the landlord of the property |

## Bookings

The Bookings table stores information about the booking requests made by tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the booking |
| property_id | Integer | Foreign key referencing the property being booked |
| tenant_id | Integer | Foreign key referencing the tenant making the booking |
| status | String | Status of the booking request (pending, approved, rejected) |

## Leases

The Leases table stores information about the lease agreements between landlords and tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the lease |
| property_id | Integer | Foreign key referencing the property being leased |
| tenant_id | Integer | Foreign key referencing the tenant leasing the property |
| start_date | Date | Start date of the lease |
| end_date | Date | End date of the lease |

## Messages

The Messages table stores information about the messages exchanged between users.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the message |
| sender_id | Integer | Foreign key referencing the sender of the message |
| receiver_id | Integer | Foreign key referencing the receiver of the message |
| content | String | Content of the message |
| timestamp | DateTime | Timestamp of when the message was sent |

## Maintenance Requests

The Maintenance Requests table stores information about the maintenance requests made by tenants.

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | Integer | Unique identifier for the maintenance request |
| property_id | Integer | Foreign key referencing the property requiring maintenance |
| tenant_id | Integer | Foreign key referencing the tenant making the request |
| description | String | Description of the maintenance issue |
| status | String | Status of the maintenance request (pending, in progress, completed) |
