#!/usr/bin/env python3
"""
FastAPI Web Application for CI/CD Practice
"""
from datetime import datetime
from typing import List
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


# Pydantic 모델 ?�의
class HealthResponse(BaseModel):
    status: str
    message: str
    timestamp: str


class StatusResponse(BaseModel):
    application: str
    status: str
    version: str
    environment: str
    features: List[str]


class VersionResponse(BaseModel):
    version: str
    build: str
    python_version: str
    framework: str


# FastAPI ???�성
app = FastAPI(
    title="CI/CD Practice API",
    description="GitHub Actions�??�용??CI/CD ?�이?�라???�습??FastAPI ?�플리�??�션",
    version="1.0.0",
    contact={
        "name": "CI/CD Practice",
        "url": "https://github.com/brightalot/cicd",
    },
)

# HTML ?�플�?
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Practice App - FastAPI</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            line-height: 1.6;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }
        .status {
            background: rgba(76, 175, 80, 0.2);
            padding: 20px;
            border-radius: 12px;
            margin: 20px 0;
            border-left: 4px solid #4CAF50;
        }
        .version {
            background: rgba(33, 150, 243, 0.2);
            padding: 15px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            border-left: 4px solid #2196F3;
        }
        .api-links {
            background: rgba(255, 152, 0, 0.2);
            padding: 20px;
            border-radius: 12px;
            margin: 20px 0;
            border-left: 4px solid #FF9800;
        }
        .api-links a {
            color: #FFE082;
            text-decoration: none;
            display: inline-block;
            margin: 5px 0;
            padding: 5px 10px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        .api-links a:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-2px);
        }
        .badge {
            background: #FF6B6B;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>?? CI/CD Practice Application <span class="badge">FastAPI</span></h1>

        <div class="status">
            <h2>✅ Application is running successfully!</h2>
            <p>This is a <strong>FastAPI</strong> application for
               GitHub Actions CI/CD pipeline practice.</p>
            <p>🎯 Includes <strong>automatic API documentation</strong>
               for enhanced development experience!</p>
        </div>

        <div class="version">
            <strong>Version:</strong> 1.0.0<br>
            <strong>Framework:</strong> FastAPI<br>
            <strong>Environment:</strong> development<br>
            <strong>Python:</strong> 3.11+
        </div>

        <div class="api-links">
            <h3>?�� API Endpoints</h3>
            <p>
                <a href="/health">?�� /health</a> - ?�스 체크<br>
                <a href="/api/status">?�� /api/status</a> - ?�태 ?�보<br>
                <a href="/api/version">?���?/api/version</a> - 버전 ?�보<br>
            </p>

            <h3>?�� API 문서 (?�동 ?�성)</h3>
            <p>
                <a href="/docs">?�� Swagger UI</a> - ?�터?�티�?API 문서<br>
                <a href="/redoc">?�� ReDoc</a> - 깔끔??API 문서
            </p>
        </div>
    </div>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse, summary="메인 ?�이지", tags=["Frontend"])
async def home():
    """
    메인 ?�이지�?반환?�니??

    - FastAPI 기반 CI/CD ?�습 ?�플리�??�션???�페?��?
    - API ?�드?�인??�?문서 링크 ?�공
    """
    return HTMLResponse(content=HTML_TEMPLATE)


@app.get("/health", response_model=HealthResponse, summary="?�스 체크", tags=["Health"])
async def health_check():
    """
    ?�플리�??�션 ?�스 체크 ?�드?�인??

    - ?�플리�??�션???�상?�으�??�작?�는지 ?�인
    - 로드밸런?�나 모니?�링 ?�스?�에???�용
    """
    return HealthResponse(
        status="healthy",
        message="FastAPI application is running smoothly!",
        timestamp=datetime.now().isoformat(),
    )


@app.get("/api/status", response_model=StatusResponse, summary="?�플리�??�션 ?�태", tags=["API"])
async def api_status():
    """
    ?�플리�??�션???�세 ?�태 ?�보�?반환?�니??

    - ?�플리�??�션 메�??�이??
    - ?�재 버전 �??�경 ?�보
    - 지??기능 목록
    """
    return StatusResponse(
        application="CI/CD Practice App",
        status="running",
        version="1.0.0",
        environment="development",
        features=[
            "Health Check",
            "Auto-generated API docs",
            "Type validation",
            "Async support",
            "CI/CD Ready",
        ],
    )


@app.get("/api/version", response_model=VersionResponse, summary="버전 ?�보", tags=["API"])
async def api_version():
    """
    ?�플리�??�션 버전 ?�보�?반환?�니??

    - ?�재 ?�플리�??�션 버전
    - 빌드 ?�보
    - ?�용 중인 기술 ?�택
    """
    return VersionResponse(
        version="1.0.0", build="initial", python_version="3.11+", framework="FastAPI"
    )


def add(a: int, b: int) -> int:
    """간단???�셈 ?�수 (?�스?�용)"""
    return a + b


def multiply(a: int, b: int) -> int:
    """간단??곱셈 ?�수 (?�스?�용)"""
    return a * b


def get_app_info() -> dict:
    """???�보 반환"""
    return {
        "name": "CI/CD Practice App",
        "version": "1.0.0",
        "description": "GitHub Actions CI/CD ?�습??FastAPI ?�플리�??�션",
        "framework": "FastAPI",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
