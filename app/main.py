from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import ChatResponse, ChatRequest
from .middleware import add_process_time

app = FastAPI(title= 'backend', version= '1.0.0' )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(add_process_time)

@app.get('/health', tags= ['meta'])
def health() -> dict[str, str]:
    '''헬스 체크 - Docker/k8s liveness 용도.'''
    return {'status' : 'ok'}

@app.post("/echo", response_model=ChatResponse, tags=["meta"])
def echo(req: ChatRequest) -> ChatResponse:
    """Pydantic v2 검증 시연용 echo 엔드포인트."""
    return ChatResponse(answer=req.prompt, model="echo-1")