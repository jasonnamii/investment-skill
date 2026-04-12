# startup-investment

> 🇺🇸 [English README](./README.md)

**스타트업 투자 전 생애주기 백과 + 진단/의사결정 엔진. 7단계(엔젤→IPO→Exit) × 3관점(전략·법률·재무) + 5횡단축 + 밸류에이션. 진단·전략·판정·조회 4모드.**

## 사전 요구

- **Claude Cowork 또는 Claude Code** 환경
- 웹 검색 접근 (실시간 법규·세무 검증용)

## 목표

스타트업 투자유치는 단계마다 법률·재무·전략 의사결정이 뒤바뀌는 복잡한 영역이다. 이 스킬은 전체 생애주기 — 7단계(Pre-Seed~Secondary), 3관점(전략·법률·재무), 5횡단축(지분설계·거버넌스·글로벌구조·실패패턴·투자자-창업자관계), 밸류에이션 전용 모듈 — 을 구조화된 지식 베이스로 압축하고, 236개 성공/실패 패턴 쌍에 유효·무효 조건을 명시하여 상황별 맞춤 판단을 제공한다.

## 사용 시점 & 방법

입력 유형에 따라 4개 모드가 자동 판별된다:
- **현재 상황 설명** ("우리 지금 시리즈A 준비 중") → **진단** 모드: 갭 분석 + 체크리스트 + 액션
- **방향 질문** ("밸류에이션 어떻게 올려") → **전략** 모드: 조건부 전략 + 대조군 + 액션
- **갈림길 제시** ("팔까 다음 라운드 갈까") → **판정** 모드: 리스크 매트릭스 + 핵심변수 + 재평가기한
- **개념 질문** ("안티딜루션 종류") → **조회** 모드: 직접 응답 + 관할권 태그 + 대조 패턴 1쌍

수동 모드 선택 불필요. 복합 상황은 진단→전략 파이프라인으로 자동 체이닝.

## 사용 사례

| 상황 | 프롬프트 | 동작 |
|---|---|---|
| 시드 라운드 준비도 점검 | `"SaaS MRR $50K, 공동창업자 2명 50:50, ESOP 없음 — 시드 가능?"` | 진단: L2+X1 스포크 로드, 갭 분석, 캡테이블·ESOP 이슈 플래그 + 패턴 대조 |
| 밸류에이션 전략 | `"ARR $3M, NRR 130%, 시리즈A 밸류에이션 전략"` | 전략: L3+VX 로드, ARR 멀티플 × NRR 프리미엄 접근법 + 유효조건 제시 |
| 엑시트 의사결정 | `"M&A $50M 오퍼 vs 시리즈C — 런웨이 18개월"` | 판정: L3+L6+X4+교차분석 로드, 런웨이 기반 리스크 매트릭스 구성 |
| 빠른 참조 | `"SAFE와 전환사채 차이점?"` | 조회: L1 로드, [US]/[KR] 관할권 태그 포함 직접 응답 + 대조 패턴 1쌍 |
## 주요 기능

- **허브-스포크 아키텍처** — 9.6KB 허브(SKILL.md)가 16개 레퍼런스 스포크(총 127K 토큰)를 오케스트레이션
- **236개 조건부 패턴** — 모든 성공 패턴에 실패 대조군 병치, 유효/무효 조건 명시로 생존자 편향 차단
- **모드 자동 판별** — 수동 전환 없이 입력으로부터 진단/전략/판정/조회 자동 추론
- **3Phase 핑퐁** — 현황→목적→제약 순서로 맥락 수집 후 응답, 성급한 조언 방지
- **이중 관할권** — 모든 법률·세무 정보에 [KR]/[US] 태그 + 기준연도 마커, 델라웨어 플립 구조와 한국 규제 현실 반영
- **교차분석 레이어** — 모순 6건, 강화 루프 5건, 빈자리 9건, Exit 매트릭스로 단계 간 패턴 연결

## 연동 스킬

- **[bp-guide](https://github.com/jasonnamii/bp-guide)** — 투자유치 전략 수립 후 BP 작성으로 핸드오프
- **[biz-skill](https://github.com/jasonnamii/biz-skill)** — 비즈니스 전략 패턴; 자본·퇴장 관련 패턴을 흡수
- **[holdings-consulting](https://github.com/jasonnamii/holdings-consulting)** — 엑시트 후 지주회사 구조 설계
- **[research-frame](https://github.com/jasonnamii/research-frame)** — 신규 엣지 케이스 딥 리서치

## 설치

```bash
git clone https://github.com/jasonnamii/startup-investment.git ~/.claude/skills/startup-investment
```

## 업데이트

```bash
cd ~/.claude/skills/startup-investment && git pull
```

`~/.claude/skills/`에 배치된 스킬은 Claude Code 및 Cowork 세션에서 자동으로 사용 가능합니다.

## Cowork Skills

25개 이상의 커스텀 스킬 중 하나입니다. 전체 카탈로그: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## 라이선스

MIT License — 자유롭게 사용, 수정, 공유 가능합니다.