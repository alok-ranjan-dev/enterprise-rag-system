from fastapi import FastAPI

# Initialize the backend application
app = FastAPI(title="Enterprise RAG API",version="1.0")

# Create a simple endpoint to verify the server is running
@app.get("/")
def read_root():
    return{"status":"Active","message":"RAG Backend is running perfectly.(:"}