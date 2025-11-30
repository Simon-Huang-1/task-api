# from fastapi import FastAPI
# from app.api import auth, projects, tasks

# app = FastAPI(title="Task & Projects API")

# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(projects.router, prefix="/projects", tags=["projects"])
# # tasks router might be nested under projects or separate
from fastapi import FastAPI

app = FastAPI(title="Task & Projects API")

@app.get("/")
def root():
    return {"message": "Task & Projects API is running!"}
