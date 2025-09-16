# 🚀 CI/CD Practice Project

GitHub Actions를 사용한 CI/CD 파이프라인 실습 프로젝트입니다.

## 📋 프로젝트 개요

이 프로젝트는 GitHub Actions를 활용하여 현대적인 CI/CD 파이프라인을 구축하고 실습하기 위한 샘플 FastAPI 웹 애플리케이션입니다.

## 🛠️ 기술 스택

- **Backend**: Python 3.11, FastAPI
- **ASGI Server**: Uvicorn
- **Testing**: pytest, pytest-asyncio, httpx
- **Code Quality**: flake8, black, isort
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

## 📁 프로젝트 구조

```
cicd/
├── app.py              # 메인 FastAPI 애플리케이션
├── test_app.py         # 단위 테스트 및 통합 테스트
├── requirements.txt    # Python 의존성
├── Dockerfile         # Docker 컨테이너 설정
├── pytest.ini        # pytest 설정
├── .github/           # GitHub Actions 워크플로우
│   └── workflows/
│       ├── ci.yml     # CI 파이프라인
│       └── cd.yml     # CD 파이프라인
└── README.md          # 프로젝트 문서
```

## 🚀 로컬 실행

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. 애플리케이션 실행
```bash
# 개발 모드로 실행
python app.py

# 또는 uvicorn으로 직접 실행
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 3. 테스트 실행
```bash
# 전체 테스트 실행
pytest

# 비동기 테스트 포함하여 실행
pytest -v

# 커버리지와 함께 실행
pytest --cov=app --cov-report=html
```

## 🐳 Docker 실행

### 이미지 빌드
```bash
docker build -t cicd-practice-app .
```

### 컨테이너 실행
```bash
docker run -p 8000:8000 cicd-practice-app
```

## 🌐 API 엔드포인트

- `GET /` - 메인 페이지 (HTML)
- `GET /health` - 헬스 체크 (JSON)
- `GET /api/status` - 애플리케이션 상태 (JSON)
- `GET /api/version` - 버전 정보 (JSON)

## 📚 API 문서 (FastAPI 자동 생성)

- `GET /docs` - **Swagger UI** 인터랙티브 API 문서
- `GET /redoc` - **ReDoc** 깔끔한 API 문서  
- `GET /openapi.json` - OpenAPI 3.0 스키마

## 🔄 CI/CD 파이프라인

### CI (Continuous Integration)
- ✅ 코드 품질 검사 (flake8)
- ✅ 단위 테스트 실행
- ✅ 테스트 커버리지 검증
- ✅ Docker 이미지 빌드

### CD (Continuous Deployment)  
- 🚀 자동 배포 (프로덕션)
- 📦 Docker 이미지 레지스트리 푸시
- 🔍 배포 후 헬스 체크

## 📈 개발 워크플로우

1. **Feature Branch** 생성
2. **코드 개발** 및 테스트 작성
3. **Pull Request** 생성
4. **CI 파이프라인** 자동 실행
5. **코드 리뷰** 및 승인
6. **Main Branch** 머지
7. **CD 파이프라인** 자동 배포

## 🎯 학습 목표

- [x] GitHub Actions 기본 개념 이해
- [x] CI 파이프라인 구성 (테스트, 빌드)
- [x] CD 파이프라인 구성 (배포)
- [x] Docker 컨테이너화
- [x] 자동화된 품질 검증
- [x] 배포 전략 및 롤백

## 📚 참고 자료

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Docker Documentation](https://docs.docker.com/)
- [pytest Documentation](https://docs.pytest.org/)