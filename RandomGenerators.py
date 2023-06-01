import random
from datetime import timedelta,datetime

def generate_user():
        sports = ["Football", "Basketball", "Tennis", "Baseball", "Hockey"]
        countries = ["USA", "Germany", "Spain", "Italy", "France", "Brazil", "China"]
        genders = ["Male", "Female"]
        currencies = ["USD", "EUR", "GBP", "CAD", "AUD"]
        start_date = datetime(2022, 3, 1)
        birth_year = random.randint(1950, 2005)
        gender = random.choice(genders)
        country = random.choice(countries)
        sport_pref = random.choice(sports)
        currency = random.choice(currencies)
        registration_date = start_date + timedelta(days=random.randint(0, 365))
        user = {
                "birth_year": birth_year,
                "gender": gender,
                "country": country,
                "sport_pref": sport_pref,
                "currency": currency,
                "registration_date": registration_date.strftime("%Y-%m-%dT%H:%M:%S")
            }
        return user

def generate_event():
    
        leagues = ["Premier League", "La Liga", "Serie A", "NBA", "NFL", "Copa Libertadores"]
        sports = ["Football", "Basketball", "Soccer", "American Football"]
        countries = ["England", "Spain", "Italy", "USA", "Brazil"]
        start_date = datetime(2022, 4, 10)

    
        league = random.choice(leagues)
        sport = random.choice(sports)
        country = random.choice(countries)
        begin_timestamp = start_date + timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        end_timestamp = begin_timestamp + timedelta(hours=random.randint(1, 3))
        participants = random.sample(["Team A", "Team B", "Team C", "Team D"], k=2)

        event = {
            "league": league,
            "sport": sport,
            "country": country,
            "begin_timestamp": begin_timestamp.strftime("%Y-%m-%d %H:%M:%S%z"),
            "end_timestamp": end_timestamp.strftime("%Y-%m-%d %H:%M:%S%z"),
            "participants": participants
        }
        
        return event



def generate_coupon():
    
        coupon_id = random.randint(1, 100)
        selections = []
        timestamp = datetime.now().isoformat()

        stake = round(random.uniform(5.0, 50.0), 2)
        user_id = random.randint(1, 100)

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




    