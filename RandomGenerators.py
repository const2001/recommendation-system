import random
from datetime import timedelta,datetime


def generate_users(n):
    users = []
    for i in range(n):
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
        users.append(user)
    return users

def generate_events(n):
    events = []
    for i in range(n):
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
        events.append(event)

    return events

    