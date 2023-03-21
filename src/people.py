from typing import List

class Person:
    name : str
    number: int
    location: str
    sign : str
    todayEvent : str
    traits : List[str]
    interests : List[str]
    cords = tuple

class Laney(Person):
    name = "Laney"
    number = 6788761173
    location = 'Los Angeles'
    sign = "Libra"
    todayEvent = "Dinner with their sister"
    traits = ["Sweet", "Nice", "Kind", "Funny", "Beautiful"]
    interests = ["Film", "Cooking", "Boyfriend", "Books","Celebrities"]
    cords = (34.097852508492196, -118.31971204478285)

class Kyle(Person):
    name = "Kyle"
    number = 6033419006
    location  = "South Boston, Massachusets"
    sign = "Pisces"
    todayEvent = "Working out on exercise bike"
    traits = ["Funny", "Tall", "Smart", "Goofy", "Personable", "Unique"]
    interests = ["Gaming", "ESports", "Optic Gaming", "Accounting", "Sports", "Soccer", "Food"]
    cords = (42.334438, -71.041985)

class Sean(Person):
    name = "Sean"
    number = 6033919919
    location  = "South Boston, Massachusets"
    sign = "Pisces"
    todayEvent = None
    traits = ["Funny", "Smart", "Kinds", "Entrepreneur", "Cute", "Interesting"]
    interests = ["Sailing", "Gaming", "Gardening", "Finance", "Stocks", "Classic Rocks", "Programming", "Science"]
    cords = (42.334438, -71.041985)

class Lauren(Person):
    name = "Lauren"
    number = 6033876001
    location  = "Winthrop, Massachusets"
    sign = "Taurus"
    todayEvent = None
    traits = ["Creative", "Kind", "Kinds", "Compassionate", "Pretty"]
    interests = ["Marketing", "Philanthropy", "Homeownership", "Couples", "Cats", "Horoscopes", "Celebrities", "The Bachelor"]

class Courtney(Person):
    name = "Coutney"
    number = 6035407494
    location  = "British Virgin, Isles"
    sign = "Leo"
    todayEvent = "Sailing on catamaran"
    traits = ["Reliable", "Kind", "Trustworthy", "Fun", "Compassionate", "Friendly", ""]
    interests = ["Tennis", "Pickleball", "Philathapry", "Celebrities", "Vacation", "the 70s", "Retirement", "Florida"]

class AllFriends:
    List[Person]