from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Document Processing Platform",
    description="Secure document processing with AI analysis",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Document Processing Platform API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "backend"}