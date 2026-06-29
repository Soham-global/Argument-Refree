from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.chain import get_verdict

app = FastAPI(
    title="Argument Referee API",
    description="An AI-powered argument referee that gives neutral verdicts.",
    version="0.1.0"
)

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request model
class ArgumentRequest(BaseModel):
    person1: str
    person2: str


# Response model
class VerdictResponse(BaseModel):
    verdict: str


@app.get("/")
def root():
    return {"message": "Argument Referee API is running 🏆"}


@app.post("/verdict", response_model=VerdictResponse)
def get_argument_verdict(request: ArgumentRequest):
    verdict = get_verdict(
        person1=request.person1,
        person2=request.person2
    )
    return VerdictResponse(verdict=verdict)