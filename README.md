# Demystifying LLM

A Django-based Prompt Engineering Refinement application that helps users analyse, improve, and compare prompts using custom rubrics and LLMs.

## Tech Stack

- **Backend:** Django, Django REST Framework
- **LLM:** AWS Bedrock (Qwen)
- **Orchestration:** LangGraph
- **Database:** PostgreSQL
- **Containerisation:** Docker, Docker Compose

## Prerequisites

- Docker and Docker Compose
- AWS credentials with Bedrock access (for LLM functionality)

## Local Setup

**1. Clone the repository**

```bash
git clone <repository-url>
cd demystifying-llm
```

**2. Configure environment variables**

```bash
cp .env.example .env
```

Update `.env` with the required configuration.

**3. Build and start the containers**

```bash
docker compose up -d --build
```

**4. Run database migrations**

```bash
docker compose exec web python manage.py migrate
```

**5. Access the application**

- Application: http://localhost:8000
- Health Check: http://localhost:8000/api/v1/health/
- Django Admin: http://localhost:8000/admin/

## Development Commands

```bash
# View logs
docker compose logs -f web

# Run migrations
docker compose exec web python manage.py migrate

# Create migrations
docker compose exec web python manage.py makemigrations

# Run tests
docker compose run --rm web sh -c "pip install -r requirements/development.txt && pytest"

# Stop containers
docker compose down
```

## Project Structure

```text
apps/
├── core/            # Shared application functionality
├── prompt_editor/   # Prompt analysis and refinement workflows
└── llm/             # AWS Bedrock integration

config/              # Django configuration
rubrics/             # Custom prompt evaluation rubrics
prompts/             # LLM prompt templates
templates/           # Django HTML templates
static/              # CSS and JavaScript
tests/               # Automated tests
```