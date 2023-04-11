from datetime import datetime, timezone


# Recommend coupons based on user preferences and odds


def recommend_coupons(user, coupons, events):

    recommended_coupons = []
    for coupon in coupons:
        coupon_odds = 1
        for selection in coupon["selections"]:
            event_id = selection["event_id"]
            event = next(
                (e for e in events if e["event_id"] == event_id), None)
            if event and event["country"] == user["country"] and event["sport"] == user["sport_pref"]:
                coupon_odds *= selection["odds"]
            else:
                coupon_odds = 0
                break
        if coupon_odds > 0:
            coupon_copy = coupon.copy()
            coupon_copy["odds"] = coupon_odds
            recommended_coupons.append(coupon_copy)
    return sorted(recommended_coupons, key=lambda x: x["odds"], reverse=True)




# print(recommend_coupons(1, coupons, events)) # Outputs [{'coupon_id': 'C001', 'selections': [{'event_id': 'E001', 'odds': 2.0}], 'stake': 10.0, 'timestamp': '2022-04-08T09:30:00', 'user_id': 1, 'odds': 2.0}]
