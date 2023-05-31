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



def generate_coupon(user_id, stake):
    coupon_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    selections = []
    timestamp = datetime.now().isoformat()

    num_selections = random.randint(1, 5)
    for _ in range(num_selections):
        event_id = random.randint(1, 10)
        odds = round(random.uniform(1.0, 3.0), 2)
        selection = {"event_id": event_id, "odds": odds}
        selections.append(selection)

    coupon = {
        "coupon_id": coupon_id,
        "selections": selections,
        "stake": stake,
        "timestamp": timestamp,
        "user_id": user_id
    }

    return coupon




# # print(recommend_coupons(1, coupons, events)) # Outputs [{'coupon_id': 'C001', 'selections': [{'event_id': 'E001', 'odds': 2.0}], 'stake': 10.0, 'timestamp': '2022-04-08T09:30:00', 'user_id': 1, 'odds': 2.0}]
# if __name__ == "__main__":

#  users = [

#     {
#         "user_id": 1,
#         "birth_year": 1990,
#         "gender": "Male",
#         "country": "Italy",
#         "sport_pref": "Football",
#         "currency": "EUR",
#         "registration_date": "2022-03-01T00:00:00",
#     },
#     {
#         "user_id": 2,
#         "birth_year": 1985,
#         "gender": "Male",
#         "country": "Germany",
#         "sport_pref": "Football",
#         "currency": "EUR",
#         "registration_date": "2022-03-01T00:00:00",
#     },
#     {
#         "user_id": 3,
#         "birth_year": 1995,
#         "gender": "Male",
#         "country": "Spain",
#         "sport_pref": "Football",
#         "currency": "EUR",
#         "registration_date": "2022-03-01T00:00:00",
#     },
#     {
#         "user_id": 4,
#         "birth_year": 2000,
#         "gender": "Male",
#         "country": "France",
#         "sport_pref": "Basketball",
#         "currency": "EUR",
#         "registration_date": "2022-04-10T00:00:00",
#     },
#     {
#         "user_id": 5,
#         "birth_year": 1998,
#         "gender": "Male",
#         "country": "USA",
#         "sport_pref": "American Football",
#         "currency": "USD",
#         "registration_date": "2022-04-11T00:00:00",
#     },
#     {
#         "user_id": 6,
#         "birth_year": 1989,
#         "gender": "Male",
#         "country": "Brazil",
#         "sport_pref": "Soccer",
#         "currency": "BRL",
#         "registration_date": "2022-04-12T00:00:00",
#     },
# ]
#  events = [
#     {
#         "event_id": "E001",
#         "league": "Premier League",
#         "sport": "Football",
#         "country": "England",
#         "begin_timestamp": "2022-04-10 15:00:00+00:00",
#         "end_timestamp": "2022-04-10 17:00:00+00:00",
#         "participants": ["Liverpool", "Chelsea"],
#     },
#     {
#         "event_id": "E002",
#         "league": "La Liga",
#         "sport": "Football",
#         "country": "Spain",
#         "begin_timestamp": "2022-04-10 20:00:00+02:00",
#         "end_timestamp": "2022-04-10 22:00:00+02:00",
#         "participants": ["Real Madrid", "Barcelona"],
#     },
#     {
#         "event_id": "E003",
#         "league": "Serie A",
#         "sport": "Football",
#         "country": "Italy",
#         "begin_timestamp": "2022-04-12 21:00:00+02:00",
#         "end_timestamp": "2022-04-12 23:00:00+02:00",
#         "participants": ["Juventus", "AC Milan"],
#     },
#     {
#         "event_id": "E056",
#         "league": "Serie A",
#         "sport": "Football",
#         "country": "Italy",
#         "begin_timestamp": "2022-04-12 21:00:00+02:00",
#         "end_timestamp": "2022-04-12 23:00:00+02:00",
#         "participants": ["Juventus", "AC Milan"],
#     },
#     {
#         "event_id": "E004",
#         "league": "NBA",
#         "sport": "Basketball",
#         "country": "USA",
#         "begin_timestamp": "2022-04-14 19:00:00+00:00",
#         "end_timestamp": "2022-04-14 21:00:00+00:00",
#         "participants": ["Los Angeles Lakers", "Brooklyn Nets"],
#     },
#     {
#         "event_id": "E005",
#         "league": "NFL",
#         "sport": "American Football",
#         "country": "USA",
#         "begin_timestamp": "2022-04-16 17:00:00+00:00",
#         "end_timestamp": "2022-04-16 19:00:00+00:00",
#         "participants": ["New England Patriots", "Tampa Bay Buccaneers"],
#     },
#     {
#         "event_id": "E006",
#         "league": "Copa Libertadores",
#         "sport": "Soccer",
#         "country": "Brazil",
#         "begin_timestamp": "2022-04-20 20:00:00-03:00",
#         "end_timestamp": "2022-04-20 22:00:00-03:00",
#         "participants": ["Santos FC", "Palmeiras"],
#     },
# ]

# # Coupon data
#  coupons = [
#     {
#         "coupon_id": "C001",
#         "selections": [{"event_id": "E001", "odds": 2.0}],
#         "stake": 10.0,
#         "timestamp": "2022-04-08T09:30:00",
#         "user_id": 1,
#     },
#     {
#         "coupon_id": "C002",
#         "selections": [
#             {"event_id": "E002", "odds": 1.5},
#             {"event_id": "E003", "odds": 2.0},
#         ],
#         "stake": 5.0,
#         "timestamp": "2022-04-08T10:30:00",
#         "user_id": 2,
#     },
#     {
#         "coupon_id": "C003",
#         "selections": [{"event_id": "E003", "odds": 2.5}],
#         "stake": 20.0,
#         "timestamp": "2022-04-08T11:30:00",
#         "user_id": 3,
#     },
#     {
#         "coupon_id": "C087",
#         "selections": [{"event_id": "E003", "odds": 2.5}],
#         "stake": 20.0,
#         "timestamp": "2022-04-08T11:30:00",
#         "user_id": 3,
#     },
#     {
#         "coupon_id": "C004",
#         "selections": [{"event_id": "E004", "odds": 1.8}],
#         "stake": 15.0,
#         "timestamp": "2022-04-13T09:30:00",
#         "user_id": 4,
#     },
#     {
#         "coupon_id": "C005",
#         "selections": [
#             {"event_id": "E005", "odds": 1.5},
#             {"event_id": "E006", "odds": 1.7},
#         ],
#         "stake": 10.0,
#         "timestamp": "2022-04-13T10:30:00",
#         "user_id": 5,
#     },
#     {
#         "coupon_id": "C006",
#         "selections": [{"event_id": "E006", "odds": 2.3}],
#         "stake": 25.0,
#         "timestamp": "2022-04-13T11:30:00",
#         "user_id": 6,
#     },
# ]
# user = {
#         "user_id": 1,
#         "birth_year": 1990,
#         "gender": "Male",
#         "country": "Italy",
#         "sport_pref": "Football",
#         "currency": "EUR",
#         "registration_date": "2022-03-01T00:00:00",
#     }
# print(recommend_coupons(user,events,coupons))
