from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}

# TODO: Add your CRUD endpoints here</content>
<parameter name="filePath">/workspaces/skills-customize-your-github-copilot-experience/assignments/rest-apis-fastapi/starter-code.py