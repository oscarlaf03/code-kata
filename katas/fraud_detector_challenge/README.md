# Fraud Detection 
## Chalenge
 We have a stilt user who lives in Bakersfield, CA(119.0611119,35.35581513). 

 Design a location based fraud detection system that flags and notifies the user whenever there is a transaction that happens outside of the user's home location.
 The system should work like this:
 * Monitor the transactions as they occur
 * Notify the user when there is a suspicious transaction
 * If the user responds saying, "it's NOT fraud", allow the subsequent transactions in that new location area(probably a travel) and don't ask the user again for that new location
 * If the user responds saying, "it's fraud", add a key-value pair to that transaction that looks like {fraud: true} and also the subsequent ones coming in from that new location

### Inputs
* Eucledien distance: sqrt((x2-x1)^2 + (y2-y1)^2)
* Read from file "data.json"
* var home = [119.0611119,35.35581513]

## My Solution
I split the logic into several small functions grouped together inside the `FraudDetector` class 

### Assumptions
In spite of the data in "data.json" having a `date` attribute for each transaction with very different broad ranging from either 2016 or 2018 I assumed that `FraudDectecor` will receive each transaction for analysis in real time and assume a  time value of `datetime.datetime.now()`for the moment in which `FraudDetector` conducts its anlysis


### Available methods

* `FraudDetector().process_all_transactions()`  This methd does everything. it will read the transactions from "data.json"  analyse each of them one by one, ask for user confirmation when needed and simulate such an user input and save the processed transactions to a new file "processed_transactions.json" for furthter inspection

* `FraudDetector().get_fraudulent_transactions()` it looks inside it is own properties to retrieve a list of only the transactions marked as fraudulent, to get accurate data you might want to run first the `process_all_transactions()` method on the same instance in order to first asses which transactions have been rejected due to proximity to valid `FLAGGED_LOCATIONS`

### Requirements
* `math`
* `collections.namedtuple`
* `datetime`
* `dateutil.parser`
* `json`
* `random`

## How to run:

`FraudDetector` has fun prints while it runs and I created a run.py file with imports and method calls.
Assuming you have all the requirements then from the project folder  run `python run.py` and see the magic happen. Don't forget to inspect the results in `processed_data.json` afterwards.

Enjoy

For a very lengthy explanation keep reading.

### How it works

**Initial check**
Basically `FraudDetectors`  first needs to know whether or not  it needs to ask the user for a transaction confirmation

**When should we NOT ask for user confirmation?**
There two main broad escenarios in which We shouldn't ask the user for confirmation one positive and one negative.

The "positive" one is when we know that the transaction is within the `DISTANCE_LIMIT` of either the `HOME_LOCATION` or any valid previously allowed location denoted by `ALLOWED_LOCATIONS`

The "negative" one is when we know that the location of the transactions is closest to a previously valid "flagged location" denoted in `FLAGGED_LOCATIONS`

so we have two types of "valid locations" one is a sort of "whitelist"  `ALLOWED_LOCATIONS` and the other one is a blacklist `FLAGGED_LOCATIONS`

**But what does "valid location" means?**

For this challenge I realised that I needed to enrich the `location` data in my program and that a mere `lat` and `lng` would not suffice. I neede to to enrich the `location` data with  an attribute of whether o not that given location is to be considered permanent or temporary  and  the expiration date of such location. Thus "valid location" is one which "expiration_data" is yet to happen according to the default attibute of number of `DAYS_PERMISSIONED` a location should be considerd

In order to keep it simple, to enrich `location` data and not to tax with more than one class I decided to configure a `namedtuple` for `location` and pass `temporary` attribute and an `expires` string with the isformat datetime of the expiration of such location

Thus whenever  a new locatios is added either to `ALLOWED_LOCATIONS` or to `FLAGGED_LOCATIONS` the `expires` string is the time value at the moment of the addition  `datetime.datetime.now()` plus the `DAYS_PERMISSIONES`

with the exception of the `HOME_LOCATION` which is loaded and configurated by default, is not "temporary" and do not have an expiraton date

Thus everytime we need to look for a location either in `ALLOWED_LOCATIONS` or in `FLAGGED_LOCATIONS` the  method `get_unexpired_locations` will be ran first to return only the locations that are within the expiration date

So in shor thanks to running that logic we will that we do not need to ask for user confirmation either because we already know to reject or accept the tansaction accordingly

**User Confirmation**

When the location of the transactions is not the closest to any valid known `FLAGGED_LOCATION` and it is not within the `DISTANCE_LIMIT` of any valid `ALLOWED_LOCATIONS` then it is time to ask for user confirmation on such suspicious transaction

`FraudDetector` prompts the user for a transaction confirmation. In this challenge the user input is simulated randomly in order to get any type of scenarios automatically

**Handling User confirmation**
Depending on the user confirmation input the location of the suspicious transaction will be added to either `ALLOWED_LOCATIONS` or  `FLAGGED_LOCATIONS` and thus the instance of the class `FraudDetector` becomes smarter to handle the next transaction request

