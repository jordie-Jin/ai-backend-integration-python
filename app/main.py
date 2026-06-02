from fastapi import FastAPI

app = FastAPI(title= 'backend', version= '1.0.0' )

from .schemas import ChatResponse, ChatRequest

@app.get('/health', tags= ['meta'])
def health() -> dict[str, str]:
    '''헬스 체크 - Docker/k8s liveness 용도.'''
    return {'status' : 'ok'}

@app.post("/echo", response_model=ChatResponse, tags=["meta"])
def echo(req: ChatRequest) -> ChatResponse:
    """Pydantic v2 검증 시연용 echo 엔드포인트."""
    return ChatResponse(answer=req.prompt, model="echo-1")