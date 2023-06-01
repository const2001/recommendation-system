from datetime import datetime, timezone


# Recommend coupons based on user preferences and odds


def recommend_coupons(user, events, coupons):
    # Find the user with the given user_id
   
    # Get a list of events that match the user's sport preference
    events_for_user = []
    for event in events:
        if event["sport"] == user["sport_pref"]:
            events_for_user.append(event)

    # Get a list of coupons that contain selections for the events the user is interested in
    coupons_for_user = []
    for coupon in coupons:
        for selection in coupon["selections"]:
            for event in events_for_user:
                if selection["event_id"] == event["event_id"]:
                    coupons_for_user.append(coupon)
                    break

    # Sort the coupons by odds, from highest to lowest
    coupons_for_user.sort(key=lambda x: max([s["odds"] for s in x["selections"]]), reverse=True)

    # Return the top 3 coupons
    return coupons_for_user[:3]





