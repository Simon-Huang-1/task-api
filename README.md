# Task & Projects API

A backend REST API for managing projects and tasks, built with **FastAPI** and **PostgreSQL**.  
Designed to showcase backend fundamentals: authentication, CRUD operations, database modeling, testing, and deployment.

---

## Features

- **User Authentication**: JWT-based signup and login  
- **Projects CRUD**: Create, read, update, delete projects  
- **Tasks CRUD**: Each task belongs to a project; can assign users, set status, priority, and due date  
- **Filtering & Pagination**: Filter tasks by status, assignee, due date, and paginate results  
- **Automatic Docs**: Swagger UI & ReDoc available  
- **Testing**: Unit and integration tests with pytest  
- **Dockerized**: Easily run locally or deploy  
- **CI**: GitHub Actions workflow for linting and tests  

---

## Tech Stack

- **Backend**: FastAPI, Python 3.11  
- **Database**: PostgreSQL, SQLModel (ORM)  
- **Authentication**: JWT (python-jose) + Passlib for password hashing  
- **Testing**: pytest, httpx  
- **Deployment**: Docker & docker-compose  

---

## Installation

### 1. Clone the repo
```bash
git clone https://github.com/Simon-Huang-1/task-api.git
cd task-api
2. Create a virtual environment
bash
Copier le code
uv venv
# Activate the virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
3. Install dependencies
bash
Copier le code
uv pip install fastapi uvicorn sqlmodel "psycopg[binary]" alembic "python-jose[cryptography]" "passlib[bcrypt]" pytest httpx python-dotenv
4. Set environment variables
Create a .env file at project root:

ini
Copier le code
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/taskdb
SECRET_KEY=your_super_secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=60
5. Run the server
bash
Copier le code
uvicorn app.main:app --reload
Visit http://127.0.0.1:8000/docs for interactive API docs.

Project Structure
graphql
Copier le code
task-api/
├─ app/
│  ├─ main.py            # FastAPI app entry point
│  ├─ models.py          # SQLModel database models
│  ├─ schemas.py         # Pydantic schemas for validation
│  ├─ crud.py            # Database operations
│  ├─ api/
│  │  ├─ auth.py         # Authentication endpoints
│  │  ├─ projects.py     # Projects endpoints
│  │  └─ tasks.py        # Tasks endpoints
│  └─ core/
│     ├─ config.py       # Environment & settings
│     └─ security.py     # Password hashing & JWT helpers
├─ tests/                # Unit and integration tests
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ alembic/              # Database migrations
└─ README.md
Testing
Run all tests:

bash
Copier le code
pytest -q
Future Improvements
Invite users to projects & role-based permissions

Background jobs (e.g., email reminders for tasks)

Live deployment with CI/CD

Rate limiting and metrics

License
MIT License

yaml
Copier le code

---

This README:

- Explains **what the project does**  
- Highlights **skills that employers care about**  
- Shows **how to run it locally**  
- Includes **project structure**, **testing**, and **future improvements**  

---

If you want, I can also **write a short “resume-friendly project blurb”** you can copy into your CV that summarizes this backend project in 2–3 lines. This is perfect for recruiters scanning quickly.  

Do you want me to do that next?