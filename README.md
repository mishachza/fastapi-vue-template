# FastAPI Vue Template

A web application template with FastAPI backend and Vue.js frontend.

## Installation

```bash
git clone https://github.com/mishachza/fastapi-vue-template.git
cd fastapi-vue-template
```

## Project Structure

```
.
├── backend/             # FastAPI backend
│   ├── main.py         # Main application file
│   ├── schemas.py      # Pydantic schemas
│   └── requirements.txt # Python dependencies
│
└── frontend/           # Vue.js frontend
    ├── src/
    │   ├── router/    # Routing
    │   ├── services/  # API services
    │   └── App.vue    # Root component
    └── package.json   # Node.js dependencies
```

## Running the Project

1. Stop all containers and clean Docker:
```bash
sudo docker-compose down -v && sudo docker system prune -a --volumes
```

2. Start the project:
```bash
sudo docker-compose up --build
```

After startup:
- Backend will be available at http://localhost:8000
- Frontend will be available at http://localhost:5173

## Technologies

- Backend:
  - FastAPI
  - SQLAlchemy
  - PostgreSQL
  - Pydantic

- Frontend:
  - Vue.js 3
  - Vue Router
  - Axios
  - Docker

## API Endpoints

- `GET /test` - Test endpoint
  - Response: `{"message": "API работает!", "status": "success"}` 