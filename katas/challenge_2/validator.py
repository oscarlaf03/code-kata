import math
from collections import namedtuple
import datetime
import dateutil.parser


TRANSACTION_SAMPLE_2 = {
      "date": "2018-07-02",
      "name": "SINEMA PARK 62 SANKT-PETERBU",
      "amount": 4.18,
      "pending": 'false',
      "category": [ "Food and Drink", "Restaurants"],
      "location": [119.04093,35.2959]
}

TRANSACTION_SAMPLE = {
      "date": "2018-07-02",
      "name": "SINEMA PARK 62 SANKT-PETERBU",
      "amount": 4.18,
      "pending": 'false',
      "category": [ "Food and Drink", "Restaurants"],
      "location": [119.04093,350.2959]
}

DISTANCE_LIMIT = 20
Location = namedtuple('Location', 'lat lng temporary expires')
HOME_LOCATION = Location (119.0611119,35.35581513, False, None)
ALLOWED_LOCATIONS = [HOME_LOCATION]
FLAGGED_LOCATIONS = []
DAYS_PERMISSIONED = 15


def within_expiration_date(location):
    now = datetime.datetime.now()
    expires = location.expires
    return now <= dateutil.parser.parse(expires) if location.temporary else True

def get_unexpired_locations(locations):
 return [ l for l in locations if within_expiration_date(l)]


def euclidean_distance(location_a, location_b):
    lat_user_location = location_a[0]
    lng_user_location = location_a[1]
    lat_transaction = location_b[0]
    lng_transaction = location_b[1]
    return math.sqrt((lat_transaction-lat_user_location)**2 + (lng_transaction-lng_user_location)**2)


def minimum_distance(location,locations):
    eligible_locations = get_unexpired_locations(locations)
    distances = []
    for l in eligible_locations:
        distances.append(euclidean_distance(l,location))
    return min(distances) if distances else None


def get_user_confirmation(transaction):
    print('Do you confirm this transaction: Y/N')
    confirmation = input().upper()
    # while confirmation != 'Y' or confirmation != 'N':
    #     print('Please enter either Y/N')
    #     confirmation  =  input().upper()
    return confirmation


def check_location(transaction):
    pass

def expiration_date():
    return (datetime.datetime.now() + datetime.timedelta(days=DAYS_PERMISSIONED)).isoformat 

def needs_location_validation(location):
    distance_from_allowed_locations = minimum_distance(location, ALLOWED_LOCATIONS)
    return distance_from_allowed_locations >  DISTANCE_LIMIT

def needs_flag(location):
    distance_from_allowed_locations = minimum_distance(location, ALLOWED_LOCATIONS)
    distance_from_flagged_locations = minimum_distance(location, FLAGGED_LOCATIONS)
    if distance_from_flagged_locations:
        return distance_from_flagged_locations < distance_from_allowed_locations
    else:
        return False


def flag_as_fraud(transaction):
    transaction['fraud'] = True

def validate_location(transaction):
        location = transaction['location']
        user_confirmation = get_user_confirmation(transaction)
        new_location = Location(location[0],location[1], True, expiration_date())
        if user_confirmation == 'Y':
            #TODO 
            # accept_transaction(transaction)
            ALLOWED_LOCATIONS.append(new_location)
            print("Allowed and added")
        else:
            FLAGGED_LOCATIONS.append(new_location)
            flag_as_fraud(transaction)
            print("Flagged and rejected")

def process_transaction(transaction):
    location = transaction['location']
    distance_from_allowed_locations = minimum_distance(location, ALLOWED_LOCATIONS)
    distance_from_flagged_locations = minimum_distance(location, FLAGGED_LOCATIONS)
    reject_location = distance_from_flagged_locations < distance_from_allowed_locations if distance_from_flagged_locations else False
    location_needs_user_validation = distance_from_allowed_locations >  DISTANCE_LIMIT and (not reject_location)
    if location_needs_user_validation:
        validate_location(transaction)
    elif reject_location:
        flag_as_fraud(transaction)
    else:
        print("Valid transaction")



process_transaction(TRANSACTION_SAMPLE)