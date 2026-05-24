# AI / 딥테크 라운드 특수성 (2026.5)

> 일반 §1~§7에 묻힌 AI·딥테크 스타트업 투자 특수성 별도 정리.

## 1. AI 스타트업 밸류에이션 특수성
### 1.1 ARR 적용 제약
- 일반 SaaS: 15-25x ARR (Series A)
- AI 인프라/모델: **50-100x ARR** (잠재시장 평가 우선)
- AI 응용 (Vertical): 20-40x ARR
- **2024-25 정점 → 2026 정상화 30-50x로 수렴**

### 1.2 비전통 지표
| 지표 | 의미 | 적정 범위 |
|---|---|---|
| Training Compute | 학습 비용 (GPU 시간) | 시리즈 A: $100K-1M / B: $1-10M |
| Model Performance | Benchmark 점수 (MMLU·HumanEval 등) | 단계별 SOTA 근접 |
| Data Moat | 학습 데이터 독점성 | 라이선스·계약·생성 |
| Talent Density | ML PhD 비율 | 시리즈 A 30%+ |
| GPU 인프라 | 자체 보유 vs 클라우드 | 시리즈 B+ 자체 추세 |
| Customer ARR Growth | 응용 AI 한정 | 200%+ YoY |

### 1.3 한국 AI 스타트업 평균 밸류 (2026.Q1)
- Seed: 30-100억 (일반 SaaS 대비 2x)
- Series A: 300-1,000억 (일반 대비 2-3x)
- Series B: 1,500억-5,000억 (Lunit·뤼튼·업스테이지 등 사례)

## 2. AI 딜 구조 특수성
### 2.1 IP 귀속
- **베이스 모델** — 개발사 보유
- **Fine-tuning 모델** — 양측 협상 (디폴트 개발사)
- **학습 데이터** — 제공자 (라이선스만 부여)
- **출력물** — 사용자 보유 (단, 비배타적 라이선스 개발사 가질 수 있음)

### 2.2 데이터 라이선싱
- **2025 서울중앙지법 2025가합30000** — 무단 학습 = 저작권 침해
- AI 스타트업은 데이터 라이선싱 비용을 별도 자금조달
- VC 텀시트에 **"Data License Reserve"** 항목 추가 트렌드

### 2.3 인재 보유 약정
- **창업자 + 핵심 ML 엔지니어 vesting 4-6년** (일반 4년보다 길게)
- **Non-compete 강화** — 동종 AI 회사 1-2년
- **IP 양도 클로즈** — 입사 전 IP 명확 분리

### 2.4 컴퓨팅 자원 확보 조항
- 「펀드 운용사 또는 LP의 GPU 인프라 우선 접근권」
- 「클라우드 크레딧 (AWS·GCP·Azure) 별도 지원」
- 「자체 GPU 클러스터 구축 funding allocation」

## 3. 딥테크 (우주·바이오·에너지·시스템반도체) 특수성
### 3.1 자금조달 패턴
- **Time-to-Market 5-10년** vs SaaS 1-2년
- **Capital intensive** — 시리즈 B+ 500억-1,000억 표준
- **정부 R&D 매칭** — 기술특례·국가과제

### 3.2 마일스톤 기반 분할 투자
- 기술개발 milestone 달성 시 tranche 별 자금집행
- 임상 단계, 시제품, 양산 등 정량적 기준
- 미달성 시 valuation 재조정 또는 추가투자 거절권

### 3.3 IP·특허 평가
- 특허 패밀리 수 + 청구항 + 인용지수
- FTO (Freedom-to-Operate) 분석
- 특허 라이선싱 잠재 수익

### 3.4 한국 딥테크 정책 지원 (2026)
- **기술특례 상장** AI/우주/에너지/바이오/시스템반도체 확대
- **AI 기본법** 영향평가 + 표시 의무 (2026.1)
- **소부장 펀드** 1조 (2026 결성)
- **모태펀드 우주·바이오 분야** 별도 출자

## 4. AI 라운드 텀시트 — 일반과 다른 조항 5
| 조항 | 일반 SaaS | AI 특수 |
|---|---|---|
| Use of Proceeds | 인건비·마케팅·R&D | GPU/Compute 별도 line item |
| IP Assignment | 표준 | 베이스 모델·Fine-tuning·Data 분리 |
| Non-compete | 1-2년 | 1-2년 + 동종 AI 회사 명시 |
| Information Rights | 분기 KPI | Model Performance + Compute Usage 월간 |
| Strategic | VC 단독 | LP (CVC·전략적 투자자) 우선권 |

## 5. AI 응용 (Vertical AI) vs AI 인프라 차별
| 항목 | 응용 AI (Vertical) | AI 인프라 (Foundation/Tooling) |
|---|---|---|
| 평가 | ARR + Customer Growth | Capability + Adoption + Moat |
| Burn Rate | 보통 | 매우 높음 (Training 비용) |
| Time-to-Revenue | 6-12개월 | 18-36개월 |
| Exit | M&A 활발 | IPO 또는 빅테크 인수 |
| 한국 사례 | Lunit·뤼튼·Riiid | 업스테이지·Sionic AI |
| 글로벌 사례 | Harvey·Cresta | OpenAI·Anthropic·Mistral·DeepSeek |

## 6. AI 스타트업 투자 시 redflag
1. **데이터 라이선스 미확보** — 무단 학습 = 향후 소송 위험
2. **베이스 모델 부재** — Wrapping AI (단순 API 호출) → moat 없음
3. **GPU 의존도** — 자체 인프라 없으면 비용 폭증
4. **핵심 인재 1-2명 집중** — 이탈 시 회사 와해
5. **2024-25 정점 valuation** — 2026 정상화 디스카운트 필요
6. **AI 기본법 미준수** — 영향평가 + 표시 의무 미이행
7. **오픈소스 라이선스 위반** — LLaMA Custom License·AGPL 등

확신도: 70 (AI 시장 변동성 높음. 2026.Q3 재확인 권고)
