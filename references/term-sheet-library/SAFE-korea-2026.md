# SAFE (Simple Agreement for Future Equity) — 한국 2026 표준

> Y Combinator 원본 + 한국 벤특법(차등의결권·세컨더리)·세제 반영. 2026.5 갱신.

## 1. 4가지 SAFE 유형
| 유형 | Valuation Cap | Discount | Pro-rata | 한국 빈도 |
|---|---|---|---|---|
| Cap, no Discount | ✅ | ✗ | 옵션 | 60% |
| Discount, no Cap | ✗ | ✅ (20-30%) | 옵션 | 10% |
| Cap and Discount | ✅ | ✅ | 옵션 | 25% |
| MFN | ✗ | ✗ | 옵션 | 5% |

## 2. 한국 표준 SAFE (Cap + MFN) verbatim

```
한국형 SAFE — Cap 35억 / Discount 20% / MFN / Pro-rata Option

본 SAFE (Simple Agreement for Future Equity)는 ___ (이하 "투자자")와 주식회사 ___ (이하 "회사") 간 ___년 ___월 ___일 체결된다.

1. 투자금: ___원 (이하 "구매금액")

2. 전환 사건 (Conversion Event)
   (a) Equity Financing — 적격투자 (Series A) 발생 시 자동 전환
   (b) Liquidity Event — 청산·해산·M&A 시
   (c) Dissolution Event — 회사 해산

3. 전환 가격 (Conversion Price)
   = MIN(① Valuation Cap ÷ Pre-money Capitalization, ② Equity Financing Price × (1 - Discount))

4. Valuation Cap: 35억원 (pre-money)
5. Discount: 20%
6. MFN: 후속 SAFE가 더 유리한 조건일 경우 본 SAFE도 동등 적용

7. Pro-rata Right (옵션)
   투자자는 Series A에서 본인 지분비율 유지를 위한 비례 투자 권리를 가진다.

8. 정보권 (Information Rights)
   분기 재무제표 + 연간 사업보고

9. 청산우선권 (in case of Liquidity Event before Equity Financing)
   = 구매금액의 1배 (1x non-participating)

10. 한국법 적용 + 서울중재 (KCAB)
```

## 3. 미국 SAFE vs 한국 SAFE 차이
| 항목 | 미국 (YC) | 한국 변형 |
|---|---|---|
| 법적 성격 | Convertible Security | 전환 권리부 자금조달 (한국 상법 모호) |
| 회계처리 | Equity로 분류 | 부채로 분류 우세 (K-IFRS 1032) |
| 세제 | C-corp 명확 | 전환 시점 과세 이슈 (조특법 §13) |
| Discount | 80-90% (10-20% 할인) | 70-80% (20-30% 할인) — VC 위험프리미엄 |
| Cap | 일반적 | 일반적 |
| Pro-rata | 옵션 | 표준 (한국 VC 요구) |
| MFN | 옵션 | 표준 (보수적) |

## 4. SAFE 발행 시 한국 법적 이슈
1. **상법 §469 (사채) vs §417 (전환사채) 적용 모호**
   → 실무: 전환사채(CB)로 처리하거나 별도 약정으로 보완
2. **K-IFRS 1032 — 부채/자본 분류**
   → Cap 있고 Discount 있으면 부채 분류 (전환 시 자본 재분류)
3. **세제** — 전환 시점 시가 vs Cap 차이 과세
   → 조특법 §13 벤처투자 세액공제 적용 (개인 10%)
4. **벤특법 차등의결권** — 비상장 벤처 한정
5. **세컨더리** — 2025 모태펀드 2,000억 펀드 활용

## 5. 표준 카운터 패턴 (KAJ 흔히 박는 변형)
| 변형 | 우리 카운터 |
|---|---|
| "MFN 적용 시 후속 SAFE 조건 즉시 적용" | "정보권으로 충분. MFN은 30일 통지 후 명시적 행사" |
| "Discount 없이 Cap만" | "Cap + Discount 묶음. 둘 다 없으면 Pro-rata 강화" |
| "Pro-rata 없음" | "Series A 진입 시 본인 비율 유지 필수" |
| "Liquidity Event 시 1x participating" | "1x non-participating + cap 3x" |

확신도: 75 (한국 시장 표준 + 벤특법·세제 반영. 거래별 변동)
