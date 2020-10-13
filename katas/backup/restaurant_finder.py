
import csv
import math


class RestaurantFinder:
    def __init__(self):
        self.RESTAURANTS_DATA ={}
        self.VISITORS_DATA = {}
        self.set_restaurants_data()
        self.set_visitors_data()

    def set_visitors_data(self):
        with open('visitors_data.csv') as locations:
            csv_reader = csv.reader(locations, delimiter=',')
            line_count = 0
            for r in csv_reader:
                if line_count != 0:
                    self.VISITORS_DATA[line_count - 1] = r
                line_count += 1

    def set_restaurants_data(self):
        with open('sf_restaurants.csv') as locations:
            csv_reader = csv.reader(locations, delimiter=',')
            line_count = 0
            for r in csv_reader:
                if line_count != 0:
                    self.RESTAURANTS_DATA[line_count - 1] = r
                line_count += 1


    def event(self,time_string):
        time = int(time_string)
        if time <= 1100 and time >= 800:
            return 'breakfast'
        elif time >= 1200 and time <= 1500:
            return 'lunch'
        elif time >= 1830 and time <= 2130:
            return 'dinner'
        else:
            return 'closed'

    def get_restaurants_by_event(self,event):
        restaurants = []
        for k in self.RESTAURANTS_DATA.keys():
            if self.RESTAURANTS_DATA[k][1] == event:
                restaurants.append(self.RESTAURANTS_DATA[k])
        return restaurants


    def sort_resturants_by_rating_and_distance(self,restaurants_list):
        sorted_list =  sorted(restaurants_list, key=lambda x: (float(x[5]), float(x[2])))
        return sorted_list


    def append_distance(self, visitor_location, restaurant):
        lat_res = float(restaurant[3])
        lng_res = float(restaurant[4])
        lat_vis = float(visitor_location[0])
        lng_vis = float(visitor_location[1])
        distance = math.degrees(math.acos(math.sin(math.radians(lat_res)) * math.sin(math.radians(lat_vis)) + math.cos(math.radians(lat_res)) *  math.cos(math.radians(lat_vis)) * math.cos(math.radians(lng_res - lng_vis)))) * 50 * 1.1515
        restaurant.append(distance)


    def set_distance_in_restaurants(self,visitor_location, eligible_restaurants):
        for restaurant in eligible_restaurants:
            self.append_distance(visitor_location,restaurant)

    def top_three_restaurants(self,location,time_string):
        self.set_restaurants_data() # Data from the source might have changed since our last function call
        meal_type = self.event(time_string)
        if meal_type != 'closed':
            options = self.get_restaurants_by_event(meal_type)
            self.set_distance_in_restaurants(location,options) # save resources by only calculating the distnance of eligible restaurants and  save it memory instead of the global state

            sorted_options = self.sort_resturants_by_rating_and_distance(options)
            return sorted_options[:3]
        else:
            return 'Restaurants are currently closed try again during business hours'

    def top_three_restaurants_for_every_visitor(self):
        results = {}  #Making  a copy from the state to return to in order not to touch the data state
        for i in self.VISITORS_DATA.keys():
            visitor_data = self.VISITORS_DATA[i]
            results[i] = visitor_data
            results[i].append(self.top_three_restaurants((visitor_data[0],visitor_data[1]),visitor_data[2]))
        return results



## **  PRINTING **

finder = RestaurantFinder()
top_restaurants = finder.top_three_restaurants((37.786079,-122.4013878),'2030')
visitors_data = finder.VISITORS_DATA
restauratants_data = finder.RESTAURANTS_DATA
print(visitors_data)
all_matches = finder.top_three_restaurants_for_every_visitor()
print('**PRINTING ALL MATCHES')
print(all_matches)
print('**PRINTING TOP RESTAURANTS')
print(top_restaurants)
