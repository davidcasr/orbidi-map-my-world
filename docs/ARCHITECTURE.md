# Architecture Document

## Overview

The `Map My World` API follows a modular architecture to promote scalability, maintainability, and separation of concerns. Built with FastAPI, the system ensures a high-performance, asynchronous environment for managing locations, categories, and reviews.

## High-Level Architecture

### **1. Layers**

- **API Layer**:
  - Handles HTTP requests and responses.
  - Implements routes and endpoint logic using FastAPI.
- **Service Layer** (optional):
  - Can be used to encapsulate business logic in the future.
- **Data Layer**:
  - Manages interaction with the database using SQLAlchemy ORM.

## Components

### **1. FastAPI**

FastAPI is the backbone of the API layer, providing:

- Automatic OpenAPI documentation.
- Input validation and serialization via Pydantic.

### **2. SQLAlchemy**

Used for database interactions with models defined as Python classes. It supports:

- Relationships between tables.
- Composite primary keys for data integrity.

### **3. PostgreSQL**

Relational database chosen for its robustness and scalability.

### **4. Pydantic**

Used for:

- Request validation.
- Response serialization.
- Ensures data integrity at the API layer.

## Database Design

### Tables

1. **locations**:
   - Stores location-specific data.
2. **categories**:
   - Stores category definitions.
3. **location_category_reviewed**:
   - Tracks the review status of location-category combinations.

### Relationships

- Foreign keys ensure referential integrity between `locations` and `categories`.
- Composite keys ensure uniqueness in the `location_category_reviewed` table.
