# San Francisco Restaurant Recommendations

## Instructions
A CSV file contains a list of restaurants in San Francisco with their latitudes and longitudes, ratings (on a scale of 1 to 5) and their time-slots of operation. A restaurant can serve breakfast (8 am - 11 am), lunch (12 pm - 3 pm), or dinner (6:30 pm to 9:30 pm). For someone visiting San Francisco, you need to recommend the top three restaurants nearest to the visitor’s current location (in a 1-mile radius) for the current time-slot, based on restaurant ratings. The visitor’s current location (latitude and longitude), and time of the day (24-hour format) will be given as inputs.

## Solution

Meet the class `RestaurantFinder` 
"RestaurantFinder" reads the data from the data sources and generates a recommendation for the top three restaurants more close to your location and sorted by restaurant rating

## Requirements 
- Python 3.8.5
- python modules: csv and math

### Available methods

**RestaurantFinder().top_three_restaurants(visitor_coordinates_tuple,string_of_24h_format_time)**
Returns an python list of size three with the top restaurants information sorted by closeness to the visitor and rating
```
RestaurantFinder().top_three_restaurants((37.786079,-122.4013878),'2030')  #=>  [['Sweetgreen', 'dinner', '4.4', '37.7872625', '-122.4008233', 0.07282038890033096], ['Rooster & Rice', 'dinner', '4.3', '37.785322', '-122.3976747', 0.1744844970185767], ['Red Dog', 'dinner', '4.1', '37.784809', '-122.3976457', 0.18530962004444534]]

```
**RestaurantFinder().top_three_restaurants_for_every_visitor()**
Reads all the data of the the visitors from the data source and returns a key-value object where the key is an index of the visitor and value is list of the original visitor attributes plus a list of the top three selected restaurants
```
RestaurantFinder().top_three_restaurants_for_every_visitor() #=>  {0: ['37.7773896', '-122.3941619', '1230', [['Tender Greens', 'lunch', '4.2', '37.7773353', '-122.3955456', 0.063045730729058], ['Cafe Centro', 'lunch', '4.3', '37.7817154', '-122.3964454', 0.26986597306853], ['Mexico Au Parc', 'lunch', '4.3', '37.7822884', '-122.3958525', 0.29235218673606705]]], 1: ['37.7773896', '-122.3941619', '0930', [['Bravado Coffee', 'breakfast', '4.5', '37.7787631', '-122.3935401', 0.08398925263543082], ['The Creamery', 'breakfast', '4.2', '37.7774628', '-122.3973465', 0.14498309718264804], ['Blue Bottle Coffee', 'breakfast', '4.5', '37.7824756', '-122.3953044', 0.29740594803181547]]], 2: ['37.7773896', '-122.3941619', '0700', 'Restaurants are currently closed try again during business hours'], 3: ['37.7847372', '-122.3962326', '1415', [['Mexico Au Parc', 'lunch', '4.3', '37.7822884', '-122.3958525', 0.14204656881244598], ['Cafe Centro', 'lunch', '4.3', '37.7817154', '-122.3964454', 0.17424939525555758], ['Soma Pizza', 'lunch', '4.0', '37.781729', '-122.3981837', 0.19462646573831496]]], 4: ['37.7847372', '-122.3962326', '1630', 'Restaurants are currently closed try again during business hours'], 5: ['37.7847372', '-122.3962326', '2000', [['Red Dog', 'dinner', '4.1', '37.784809', '-122.3976457', 0.06443240218955108], ['Rooster & Rice', 'dinner', '4.3', '37.785322', '-122.3976747', 0.07375304745139971], ['Rooh', 'dinner', '4.4', '37.7812954', '-122.3947494', 0.20933959162055024]]], 6: ['37.7847372', '-122.3962326', '1000', [['Blue Bottle Coffee', 'breakfast', '4.5', '37.7824756', '-122.3953044', 0.13689031315431405], ['Philz Coffee', 'breakfast', '4.6', '37.7887133', '-122.3952601', 0.23316141285128547], ['Bravado Coffee', 'breakfast', '4.5', '37.7787631', '-122.3935401', 0.3651286958460436]]], 7: ['37.786079', '-122.4013878', '2230', 'Restaurants are currently closed try again during business hours'], 8: ['37.786079', '-122.4013878', '1500', [["Lee's Deli", 'lunch', '4.1', '37.7853216', '-122.4042408', 0.13694557755013034], ['Soma Pizza', 'lunch', '4.0', '37.781729', '-122.3981837', 0.2897972251591848], ['Mexico Au Parc', 'lunch', '4.3', '37.7822884', '-122.3958525', 0.33327165909832435]]], 9: ['37.786079', '-122.4013878', '0830', [['Philz Coffee', 'breakfast', '4.6', '37.7887133', '-122.3952601', 0.3173990321830728], ['Blue Bottle Coffee', 'breakfast', '4.5', '37.7824756', '-122.3953044', 0.34592913140957504], ['The Creamery', 'breakfast', '4.2', '37.7774628', '-122.3973465', 0.5290663307831324]]], 10: ['37.786079', '-122.4013878', '2100', [['Sweetgreen', 'dinner', '4.4', '37.7872625', '-122.4008233', 0.07282038890033096], ['Rooster & Rice', 'dinner', '4.3', '37.785322', '-122.3976747', 0.1744844970185767], ['Red Dog', 'dinner', '4.1', '37.784809', '-122.3976457', 0.18530962004444534]]]}

```

## Error Handling

For both methods whenever requesting a restaurant recommendation outside business hours  a string with the message **"'Restaurants are currently closed try again during business hours'"** is returned



Thank you

Enjoy
