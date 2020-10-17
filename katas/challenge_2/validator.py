import math
from collections import namedtuple
import datetime
import dateutil.parser
import json
import random

from sample_transactions import TRANSACTION_SAMPLE, TRANSACTION_FAR_AWAY 


DISTANCE_LIMIT = 20
Location = namedtuple('Location', 'lat lng temporary expires')
HOME_LOCATION = Location (119.0611119,35.35581513, False, None)
TRANSACTIONS = json.load(open('data.json','r'))['transactions']
ALLOWED_LOCATIONS = [HOME_LOCATION]
FLAGGED_LOCATIONS = []
DAYS_PERMISSIONED = 15


def save_processed_transactions():
    with open('processed_transactions.json','w') as new_data:
        json.dump({'transactions':[TRANSACTIONS]},new_data)
        new_data.close()


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


def get_user_confirmation(transaction,):
    print(f'Do you confirm this Transaction:{transaction["name"]}?\nPlease enter Y/N')
    # confirmation = input().upper() # Actual confirmation  asking client input
    confirmation = random.choice(['Y','N']) # Simulates a  user input randomly for testing purposes
    print(f'You entered: {confirmation}')
    return confirmation


def expiration_date():
    return (datetime.datetime.now() + datetime.timedelta(days=DAYS_PERMISSIONED)).isoformat 


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
            print(f'Transaction {transaction["name"]} **ALLOWED** and to safe locations updated')
        else:
            FLAGGED_LOCATIONS.append(new_location)
            flag_as_fraud(transaction)
            print(f'Transaction {transaction["name"]}  **REJECTED** flagged as fraud and flagged locations updated')


def process_transaction(transaction):
    print(f'Processing Transaction: {transaction["name"]}')
    location = transaction['location']
    distance_from_allowed_locations = minimum_distance(location, ALLOWED_LOCATIONS)
    distance_from_flagged_locations = minimum_distance(location, FLAGGED_LOCATIONS)
    reject_location = distance_from_flagged_locations < distance_from_allowed_locations if distance_from_flagged_locations else False
    location_needs_user_validation = distance_from_allowed_locations >  DISTANCE_LIMIT and (not reject_location)
    if location_needs_user_validation:
        validate_location(transaction)
    elif reject_location:
        flag_as_fraud(transaction)
        print(f'Transaction {transaction["name"]}  **REJECTED** due to previous flaged location')

    else:
        print(f'Transaction: {transaction["name"]} is OK')



process_transaction(TRANSACTION_FAR_AWAY)