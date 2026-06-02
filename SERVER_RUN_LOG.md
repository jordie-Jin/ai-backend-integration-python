# Server Run Log

로컬 서버 실행 명령어, 포트, 주요 실행 기록을 관리하는 문서입니다.

## 현재 서버

| Server | App path | Port | Command | Notes |
| --- | --- | ---: | --- | --- |
| 루트 빈 서버 | `main:app` | `8001` | `uv run python -m uvicorn main:app --host 127.0.0.1 --port 8001 --reload` | 루트 `main.py`의 빈 FastAPI 서버 |
| 앱 서버 | `app.main:app` | `8000` | `uv run python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload` | 기존 라우터가 포함된 API 서버 |

## 기록

| Date | Item | Detail |
| --- | --- | --- |
| 2026-06-02 | 생성 로그 파일 삭제 | `server.err.log`, `server.out.log`, `server-root.err.log`, `server-root.out.log` 삭제 |
| 2026-06-02 | 로그 무시 규칙 추가 | `.gitignore`에 `server*.log` 추가 |
| 2026-06-02 | 포트 충돌 확인 | `8000`은 기존 `app.main:app` 서버가 사용 중이라 루트 서버는 `8001` 사용 |
| 2026-06-02 | 루트 서버 확인 | `http://127.0.0.1:8001/openapi.json`에서 title `backend`, version `1.0.0` 확인 |

## 관리 규칙

생성된 `server*.log` 파일은 저장소에 남기지 않습니다. 중요한 서버 실행 기록은 이 문서에 남깁니다.
