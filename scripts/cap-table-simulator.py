#!/usr/bin/env python3
"""
cap-table-simulator.py — 라운드별 캡테이블 + 희석 + Anti-dilution + 다운라운드 시뮬

사용법:
    python3 cap-table-simulator.py --scenario series-a
    python3 cap-table-simulator.py --custom rounds.json

근거: 한국 RCPS·SAFE 표준 + Weighted Average Anti-dilution
확신도: 70 (표준 모델, 거래별 변동 큼. 1차 추정용)
"""
import argparse
import json
import copy


def round_dilution(cap_table: dict, round_info: dict) -> dict:
    """라운드별 희석 계산"""
    pre_money = round_info["pre_money"]
    investment = round_info["investment"]
    post_money = pre_money + investment

    # 신규 투자자 지분
    new_investor_share = investment / post_money

    # ESOP refresh (있을 경우)
    esop_target = round_info.get("esop_target", 0)  # post-money 기준 %
    if esop_target:
        # ESOP를 pre-money에서 미리 확보 (창업자 추가 희석)
        existing_esop = cap_table.get("ESOP", 0)
        # post-money에서 esop_target 달성 위한 신규 ESOP
        # (existing + new_esop) / 1 = esop_target → new_esop = esop_target - existing × (1 - new_investor_share)
        new_esop_share = esop_target - existing_esop * (1 - new_investor_share)
        new_esop_share = max(0, new_esop_share)

        # 기존 주주들은 (1 - new_investor_share - new_esop_share) 만큼 보유
        dilution_factor = 1 - new_investor_share - new_esop_share
    else:
        dilution_factor = 1 - new_investor_share
        new_esop_share = 0

    new_cap_table = {}
    for holder, share in cap_table.items():
        if holder == "ESOP" and esop_target:
            new_cap_table[holder] = esop_target  # ESOP는 target으로 재설정
        else:
            new_cap_table[holder] = share * dilution_factor

    new_cap_table[round_info["investor"]] = new_investor_share
    new_cap_table["_meta"] = {
        "round": round_info["name"],
        "pre_money": pre_money,
        "investment": investment,
        "post_money": post_money,
        "price_per_share": round_info.get("price_per_share", "TBD"),
    }
    return new_cap_table


def apply_anti_dilution(cap_table: dict, prior_price: float, new_price: float,
                        method: str = "weighted_average_broad") -> dict:
    """Anti-dilution 발동 (다운라운드)"""
    if new_price >= prior_price:
        return cap_table  # No trigger

    if method == "full_ratchet":
        # 우선주 전환비율 = prior_price / new_price 로 즉시 조정
        ratio = prior_price / new_price
        # (단순화) 우선주 보유자 지분 × ratio 증가
        adjustment = ratio - 1
        # 주의: 실제로는 전환비율 조정이지 지분율 직접 증가가 아님
        # 단순 시뮬용
        return {
            "method": "full_ratchet",
            "adjustment_ratio": ratio,
            "note": "우선주 전환가 prior_price → new_price로 하향. 보통주 환산 시 지분 ratio 배",
        }

    if method == "weighted_average_broad":
        # Conversion Price 조정 = OP × (A + B) / (A + C)
        # A = pre-round 발행 보통주 총수 (Fully diluted)
        # B = 신규투자금액 / 기존 conversion price
        # C = 신규 발행주식 수
        return {
            "method": "weighted_average_broad",
            "formula": "OP × (A + B) / (A + C)",
            "note": "온건한 조정. 한국 표준",
        }

    return cap_table


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scenario", choices=["seed", "series-a", "series-b", "series-c", "down-round"], default="series-a")
    p.add_argument("--custom", help="JSON 파일 경로")
    args = p.parse_args()

    if args.custom:
        with open(args.custom) as f:
            scenario = json.load(f)
    else:
        # 디폴트 시나리오
        scenario = {
            "name": "한국 표준 SaaS",
            "initial": {"창업자A": 0.6, "창업자B": 0.3, "엔젤": 0.1},
            "rounds": [
                {
                    "name": "Seed",
                    "investor": "Seed_VC",
                    "pre_money": 30,  # 억원
                    "investment": 5,
                    "esop_target": 0.10,
                    "price_per_share": 1000,
                },
                {
                    "name": "Series A",
                    "investor": "Series_A_Lead",
                    "pre_money": 200,
                    "investment": 50,
                    "esop_target": 0.12,
                    "price_per_share": 5000,
                },
                {
                    "name": "Series B",
                    "investor": "Series_B_Lead",
                    "pre_money": 800,
                    "investment": 200,
                    "esop_target": 0.15,
                    "price_per_share": 15000,
                },
            ],
        }

    print(f"# Cap Table Simulation — {scenario['name']}\n")
    print(f"## Initial\n```json\n{json.dumps(scenario['initial'], ensure_ascii=False, indent=2)}\n```\n")

    cap_table = copy.deepcopy(scenario["initial"])
    for r in scenario["rounds"]:
        cap_table = round_dilution(cap_table, r)
        meta = cap_table.pop("_meta")
        print(f"## After {meta['round']}")
        print(f"- Pre-money: {meta['pre_money']}억 / Investment: {meta['investment']}억 / Post-money: {meta['post_money']}억")
        print(f"- 1주당: {meta['price_per_share']}원")
        print(f"```json\n{json.dumps({k: f'{v*100:.2f}%' for k, v in cap_table.items()}, ensure_ascii=False, indent=2)}\n```\n")

    # 다운라운드 시뮬
    if args.scenario == "down-round":
        print("## Down-round Anti-dilution 발동")
        result = apply_anti_dilution(cap_table, prior_price=15000, new_price=8000,
                                     method="weighted_average_broad")
        print(f"```json\n{json.dumps(result, ensure_ascii=False, indent=2)}\n```")

    print("\n---")
    print("**주의**: 본 시뮬은 1차 추정. 실제 거래 시 세무·법률 자문 + 발행주식 수·1주당가격 정밀 계산 필수.")
    print("**확신도**: 70 (단순 모델 + ESOP refresh 표준 가정)")


if __name__ == "__main__":
    main()
