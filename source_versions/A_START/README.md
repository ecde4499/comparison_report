# 🖼️ 짤·카드 스튜디오 (Jjal & Card Studio)

> 브라우저 내에서 배경 이미지와 문구를 조합하여 카드 뉴스, 짤방, 썸네일 등을 손쉽게 제작하고 High-Res PNG/JPEG 이미지로 다운로드하는 Client-Side 웹 애플리케이션입니다.

---

## ✨ 주요 기능

- **📷 이미지 불러오기 및 캔버스 크롭**
  - 사용자 소장 이미지(PNG, JPEG) 업로드 지원
  - 테스트 및 빠른 제작을 위한 기본 샘플 그래픽 배경 제공
  - 잘못된 파일 업로드 시 기존 작업 상태 유지 (안전성 보장)

- **📐 다양한 화면비(Aspect Ratio) 지원**
  - `1:1` 정사각 (900 × 900 px) - 인스타그램 / 기본 카드
  - `4:5` 카드 (900 × 1125 px) - 피드 게시물
  - `9:16` 세로 (900 × 1600 px) - 숏폼 / 스토리용

- **✍️ 커스텀 텍스트 및 타이포그래피 설정**
  - 실시간 입력 및 줄바꿈/이모지 지원
  - 글자 크기, 폰트 색상, 정렬(Left/Center/Right), 줄 간격 조절
  - 텍스트 위치(X, Y 좌표 %) 슬라이더 조절
  - 이미지 대비 가독성을 높여주는 자동 텍스트 외곽선(Stroke) 처리

- **💾 완성본 내보내기 및 보안 (Public Safety)**
  - HTML5 Canvas 기반의 PNG / JPEG 파일 저장
  - 100% 클라이언트 사이드 동작 (서버 업로드 없음)
  - 저장 시 원본 파일의 EXIF / GPS 위치 메타데이터 자동 제거

- **📁 템플릿 & 작업 상태 관리 (CRUD & JSON)**
  - 자주 쓰는 편집 설정을 템플릿으로 저장/수정/삭제 (`localStorage` 연동)
  - 현재 편집 상태 및 템플릿 목록 전체를 `JSON` 파일로 백업/복원
  - JSON 스키마 검증을 통한 안전한 데이터 로딩

---

## 🛠 기술 스택

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla JS - ES6+)
- **Graphics API**: HTML5 Canvas 2D Context API
- **Storage**: Browser `localStorage`, `FileReader API`

---

## 🚀 시작하기

이 프로젝트는 별도의 서버 설정이나 빌드 도구(Node.js 등) 없이 브라우저만 있으면 바로 실행 가능한 순수 클라이언트 앱입니다.

### 실행 방법
1. 리포지토리를 클론(Clone)합니다.
   ```bash
   git clone https://github.com/username/jjal-card-studio.git
   ```
2. `index.html` (또는 해당 HTML 파일)을 브라우저(Chrome, Edge, Safari 등)로 열어 실행합니다.

---

## 📂 프로젝트 구조

```text
.
├── index.html       # UI Layout, CSS 스타일링, HTML5 Canvas 렌더링 로직 통합 파일
└── README.md        # 프로젝트 소개 및 가이드 문서
```

---

## 🔒 데이터 보호 및 보안 (Privacy & Security)

- **서버 무저장**: 백엔드 서버가 존재하지 않으며, 모든 이미지는 사용자의 브라우저 메모리 내에서만 연산됩니다.
- **인증 불필요**: 회원가입/로그인 절차가 없으며 개인정보를 입력받지 않습니다.
- **메타데이터 세탁**: Canvas 재캡처 방식을 통해 원본 사진에 남은 위치(GPS) 및 디바이스 정보가 배출되지 않습니다.

---

## 📜 라이선스

This project is licensed under the [MIT License](LICENSE).
