import math
from collections import namedtuple
import datetime
import dateutil.parser
import json
import random

class FraudDetector:
    def __init__(self):
        self.DISTANCE_LIMIT = 20
        self.Location = namedtuple('Location', 'lat lng temporary expires')
        self.HOME_LOCATION = self.Location (119.0611119,35.35581513, False, None)
        self._TRANSACTIONS = json.load(open('data.json','r'))['transactions']
        self.set_transactions_id()
        self.ALLOWED_LOCATIONS = [self.HOME_LOCATION]
        self.FLAGGED_LOCATIONS = []
        self.DAYS_PERMISSIONED = 15

    @property
    def TRANSACTIONS(self):
        return self._TRANSACTIONS

    @TRANSACTIONS.setter
    def TRANSACTIONS(self, value):
        self._TRANSACTIONS = value

    def set_transactions_id(self):
        counter = 0
        indexed_transactions = []
        for t in self.TRANSACTIONS:
            t['id'] = counter
            t['fraud'] = False
            indexed_transactions.append(t)
            counter += 1
        self.TRANSACTIONS = indexed_transactions

    def save_processed_transactions(self):
        print('\n== SAVING DATA==\n')
        frauds = [ t for t in self.TRANSACTIONS if t['fraud'] == True]
        print(f'TOTAL FRAUDS DETECTED: {len(frauds)} \n\n')
        with open('processed_transactions.json','w') as new_data:
            to_save ={'transactions':self.TRANSACTIONS}
            json.dump( to_save,new_data)
            new_data.close()

    def within_expiration_date(self,location):
        now = datetime.datetime.now()
        expires = location.expires
        return now <= dateutil.parser.parse(expires) if location.temporary else True

    def get_unexpired_locations(self,locations):
        return [ l for l in locations if self.within_expiration_date(l)]

    def print_transaction_details(self,transaction):
        print(f'Amount: ${transaction["amount"]} date: {transaction["date"]} location:{transaction["location"]}')

    def euclidean_distance(self,location_a, location_b):
        lat_user_location = location_a[0]
        lng_user_location = location_a[1]
        lat_transaction = location_b[0]
        lng_transaction = location_b[1]
        return math.sqrt((lat_transaction-lat_user_location)**2 + (lng_transaction-lng_user_location)**2)

    def minimum_distance(self,location,locations):
        eligible_locations = self.get_unexpired_locations(locations)
        distances = []
        for l in eligible_locations:
            distances.append(self.euclidean_distance(l,location))
        return min(distances) if distances else None

    def get_user_confirmation(self,transaction,):
        print('\n**DANGER** This transaction needs user confirmation\n')
        print(f'Do you confirm this Transaction:{transaction["name"]}?\nPlease enter Y/N')
        # confirmation = input().upper() # Actual confirmation  asking client input
        confirmation = random.choice(['Y','N']) # Simulates a  user input randomly for testing purposes
        print(f'User entered: {confirmation}')
        return confirmation

    def expiration_date(self):
        return (datetime.datetime.now() + datetime.timedelta(days=self.DAYS_PERMISSIONED)).isoformat()

    def needs_flag(self,location):
        distance_from_allowed_locations = self.minimum_distance(location, self.ALLOWED_LOCATIONS)
        distance_from_flagged_locations = self.minimum_distance(location, self.FLAGGED_LOCATIONS)
        if distance_from_flagged_locations:
            return distance_from_flagged_locations < distance_from_allowed_locations
        else:
            return False

    def flag_as_fraud(self,transaction):
        to_update = self.TRANSACTIONS[transaction['id']]
        to_update['fraud'] = True
        self.TRANSACTIONS = self.TRANSACTIONS

    def validate_location(self,transaction):
            location = transaction['location']
            user_confirmation = self.get_user_confirmation(transaction)
            new_location = self.Location(location[0],location[1], True, self.expiration_date())
            if user_confirmation == 'Y':
                self.ALLOWED_LOCATIONS.append(new_location)
                print(f'Transaction {transaction["name"]} **ALLOWED** and to safe locations updated')
            else:
                self.FLAGGED_LOCATIONS.append(new_location)
                self.flag_as_fraud(transaction)
                print(f'Transaction {transaction["name"]}  **REJECTED** flagged as fraud and flagged locations updated')

    def process_transaction(self,transaction):
        print(f'Processing Transaction: {transaction["name"]}')
        self.print_transaction_details(transaction)
        location = transaction['location']
        distance_from_allowed_locations = self.minimum_distance(location, self.ALLOWED_LOCATIONS)
        distance_from_flagged_locations = self.minimum_distance(location, self.FLAGGED_LOCATIONS)
        reject_location = distance_from_flagged_locations < distance_from_allowed_locations if distance_from_flagged_locations else False
        location_needs_user_validation = distance_from_allowed_locations >  self.DISTANCE_LIMIT and (not reject_location)
        if location_needs_user_validation:
            self.validate_location(transaction)
        elif reject_location:
            self.flag_as_fraud(transaction)
            print(f'Transaction {transaction["name"]}  **REJECTED** automatically due to previously flagged location')
        else:
            print(f'Transaction: {transaction["name"]} is OK')

    def process_all_transactions(self):
        for transaction in self.TRANSACTIONS:
            self.process_transaction(transaction)
        self.save_processed_transactions()

    def get_fraudulent_transactions(self):
        return [ t for t in self.TRANSACTIONS if t['fraud']]

