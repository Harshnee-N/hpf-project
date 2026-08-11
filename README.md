# HPF – LSA Service Booking API

## Overview

This project is a Django REST Framework backend for an LSA (Learning Support Assistant) Service Booking system.

The system allows parents to create booking requests with LSAs and provides an API to search for available LSAs based on skills and availability.

## Tech Stack

- Python 3.14
- Django 5.2.17
- Django REST Framework
- MySQL 8.0.46
- mysqlclient
- pytest
- pytest-django
- requests
- GitHub Actions

## Database Design

The system contains three main entities:

### 1. Parent

Stores information about the parent requesting an LSA service.

### 2. LSAProfile

Stores information about Learning Support Assistants, including their skills and availability status.

### 3. BookingRequest

Stores booking information and connects a Parent with an LSAProfile.

### Relationship

```text
Parent 1 ──────── * BookingRequest * ──────── 1 LSAProfile