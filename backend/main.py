from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from backend.chain import stream_verdict

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


@app.get("/")
def root():
    return {"message": "Argument Referee API is running 🏆"}


@app.post("/verdict")
def get_argument_verdict(request: ArgumentRequest):
    return StreamingResponse(
        stream_verdict(
            person1=request.person1,
            person2=request.person2
        ),
        media_type="text/plain"
    )