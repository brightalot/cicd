#!/usr/bin/env python3
"""
Unit Tests for FastAPI CI/CD Practice App
"""
import pytest
import pytest_asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from app import app, add, multiply, get_app_info


@pytest.fixture
def client():
    """FastAPI 동기 테스트 클라이언트 설정"""
    return TestClient(app)


@pytest_asyncio.fixture
async def async_client():
    """FastAPI 비동기 테스트 클라이언트 설정"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


class TestRoutes:
    """웹 애플리케이션 라우트 테스트"""

    def test_home_page(self, client):
        """메인 페이지 테스트"""
        response = client.get("/")
        assert response.status_code == 200
        assert "CI/CD Practice Application" in response.text
        assert "FastAPI" in response.text

    def test_health_check(self, client):
        """헬스 체크 엔드포인트 테스트"""
        response = client.get("/health")
        assert response.status_code == 200

        data = response.json()
        assert data["status"] == "healthy"
        assert "message" in data
        assert "timestamp" in data
        assert "FastAPI" in data["message"]

    def test_api_status(self, client):
        """API 상태 엔드포인트 테스트"""
        response = client.get("/api/status")
        assert response.status_code == 200

        data = response.json()
        assert data["application"] == "CI/CD Practice App"
        assert data["status"] == "running"
        assert data["version"] == "1.0.0"
        assert "features" in data
        assert len(data["features"]) > 0

    def test_api_version(self, client):
        """버전 API 테스트"""
        response = client.get("/api/version")
        assert response.status_code == 200

        data = response.json()
        assert data["version"] == "1.0.0"
        assert "build" in data
        assert data["framework"] == "FastAPI"

    @pytest.mark.asyncio
    async def test_async_health_check(self, async_client):
        """비동기 헬스 체크 테스트"""
        response = await async_client.get("/health")
        assert response.status_code == 200

        data = response.json()
        assert data["status"] == "healthy"


class TestBusinessLogic:
    """비즈니스 로직 테스트"""

    def test_add_function(self):
        """덧셈 함수 테스트"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(10, -5) == 5

    def test_multiply_function(self):
        """곱셈 함수 테스트"""
        assert multiply(2, 3) == 6
        assert multiply(0, 5) == 0
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6

    def test_get_app_info(self):
        """앱 정보 함수 테스트"""
        info = get_app_info()
        assert isinstance(info, dict)
        assert info["name"] == "CI/CD Practice App"
        assert info["version"] == "1.0.0"
        assert info["framework"] == "FastAPI"
        assert "description" in info


class TestIntegration:
    """통합 테스트"""

    def test_all_endpoints_accessible(self, client):
        """모든 엔드포인트가 접근 가능한지 테스트"""
        endpoints = ["/", "/health", "/api/status", "/api/version"]

        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200, f"Failed for endpoint: {endpoint}"

    def test_json_responses_valid(self, client):
        """JSON 응답이 유효한지 테스트"""
        json_endpoints = ["/health", "/api/status", "/api/version"]

        for endpoint in json_endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200

            # JSON으로 파싱 가능한지 확인 (FastAPI 테스트 클라이언트 사용)
            try:
                data = response.json()
                assert isinstance(data, dict)
            except Exception as e:
                pytest.fail(f"Invalid JSON response from {endpoint}: {e}")

    @pytest.mark.asyncio
    async def test_async_endpoints(self, async_client):
        """비동기 엔드포인트 통합 테스트"""
        json_endpoints = ["/health", "/api/status", "/api/version"]

        for endpoint in json_endpoints:
            response = await async_client.get(endpoint)
            assert response.status_code == 200
            data = response.json()
            assert isinstance(data, dict)


class TestAPIDocumentation:
    """API 문서화 테스트 (FastAPI 특화)"""

    def test_openapi_schema(self, client):
        """OpenAPI 스키마 접근 테스트"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        schema = response.json()
        assert "openapi" in schema
        assert "info" in schema
        assert schema["info"]["title"] == "CI/CD Practice API"

    def test_docs_endpoint(self, client):
        """Swagger UI 문서 페이지 테스트"""
        response = client.get("/docs")
        assert response.status_code == 200
        assert "swagger" in response.text.lower()

    def test_redoc_endpoint(self, client):
        """ReDoc 문서 페이지 테스트"""
        response = client.get("/redoc")
        assert response.status_code == 200
        assert "redoc" in response.text.lower()
