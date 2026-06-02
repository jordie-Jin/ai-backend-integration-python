from fastapi import FastAPI

app = FastAPI(title= 'backend', version= '1.0.0' )

@app.get('/health', tags= ['meta'])
def health() -> dict[str, str]:
    '''헬스 체크 - Docker/k8s liveness 용도.'''
    return {'status' : 'ok'}

@app.get('items')
def list_items(limit: int = 10)
    return {'status': 'ok'}