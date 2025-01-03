# Map My World API | ORBIDI Challenge

ORBIDI Challenge for Senior Backend Developer.

Map My World API is a RESTful service built using FastAPI, designed to manage locations, categories, and user reviews. This API enables users to explore various places, categorize them, and maintain updated reviews.

## Features

- **CRUD Operations**:
  - Manage locations, categories, and reviews.
- **Recommendations**:
  - Fetch reviews that need updating based on the last review date.
- **Documentation**:
  - Auto-generated API documentation using Swagger and ReDoc.
- **Scalable Design**:
  - Modular structure following best practices.

## Installation

### Prerequisites

Ensure you have the following installed:

- Docker and Docker Compose
- Python 3.11+

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. Create a .env file based on .env.example:

   ```bash
   cp .env.example .env
   ```

3. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

4. Access the API documentation:

   - Swagger: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Testing

```bash
pytest
```

Made with ❤️ by @davidcasr
