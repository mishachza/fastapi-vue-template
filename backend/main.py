from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import TestResponse

app = FastAPI(title="FastAPI Vue Template")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue.js default dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Vue Template"}

@app.get("/test", response_model=TestResponse)
async def test_endpoint():
    return TestResponse(message="API is working!") 