#GIS 4085
# Create a Route Class with the following properties
## trail name, OID, trail length in miles, and trip day (store as a short integer data type).
# Add a function that will calculate total miles traveled by day.

import arcpy

wksp = arcpy.env.workspace = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\GIS4085_Week2.gdb'
arcpy.env.overwriteOutput = True
trail_loop = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\GIS4085_Week2.gdb\BearLakeLoop'
camapsite = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\GIS4085_Week2.gdb\ROMO_BackcountryCampsites'
trailhead = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\GIS4085_Week2.gdb\ROMO_Trail_Heads'


#Create Route Class and assign properties with average daily travel of 10 miles a day
class Route(object):
    def __init__(self, name, OID, trip_miles, trip_day):
        self.name = name
        self.OID = OID
        self.trip_miles = trip_miles
        self.trip_day = trip_day
    def trip_miles(self, routes):
        total = 0
        for route in routes:
            if route.trip_day == self.trip_day:
                total += route.trip_miles
        return total
    
#Create a function for miles
def trail_miles(object):
    try:
        with arcpy.da.SearchCursor(trail_loop, ['OID', 'Miles']) as cursor:
            for row in cursor:
                if row[0] == object:
                    return row [1]
                return 0
    
    except:
        print(arcpy.GetMessages(2))

#list of trails per day
route01 = Route("Bear Lake Loop Trail", 15, trail_miles(0.1), 1)
route02 = Route("Bear Lake Loop Trail", 16, trail_miles(0.02), 1)
route03 = Route("Bear Lake Loop Trail", 17, trail_miles(0.02), 1)
route04 = Route("Bear Lake To Bierstadt Junction Trail", 3, trail_miles(0.04), 1)
route05 = Route("Bear Lake To Bierstadt Junction Trail", 14, trail_miles(0.27), 1)
route06 = Route("Flattop Mountain Trail Junction - Cub Lake", 13, trail_miles(0.73), 1)
route07 = Route("Flattop Mountain Trail Junction - Cub Lake", 10, trail_miles(0.50), 1)
route08 = Route("Flattop Mountain Trail Junction - Cub Lake", 2, trail_miles(0.70), 1)
route09 = Route("Flattop Mountain Trail Junction - Cub Lake", 8, trail_miles(0.20), 2)
route10 = Route("Flattop Mountain Trail Junction - Cub Lake", 1, trail_miles(1.50), 2)
route11 = Route("The Pool - Cub Lake Trailhead", 6, trail_miles(0.84), 2)
route12 = Route("The Pool/Odessa Lake", 4, trail_miles(0.84), 3)
route13 = Route("The Pool/Odessa Lake", 7, trail_miles(1.10), 3)
route14 = Route("The Pool/Odessa Lake", 9, trail_miles(0.79), 3)
route15 = Route("Odessa Lake - Flattop Mtn. Junc.", 5, trail_miles(1.00), 4)
route16 = Route("Odessa Lake - Flattop Mtn. Junc.", 11, trail_miles(2.00), 4)
route17 = Route("Flattop Mountain Trail", 12, trail_miles(0.50), 4)
route18 = Route("Bear Lake to Bierstadt Junction Trail", 14, trail_miles(0.27), 4)
route19 = Route("Bear Lake Loop Trail", 15, trail_miles(0.1), 4)
route20 = Route("Bear Lake Loop Trail", 17, trail_miles(0.02), 4)
route21 = Route("Bear Lake Loop Trail", 16, trail_miles(0.02), 4)

routes = [route01, route02, route03, route04, route05, route05, route06, route07, route08, route09, route10, route11, route12, route13, route14, route15, route16, route17, route18, route19, route20, route21]

#loop through each day

for trip_day in [1, 2, 3, 4]:
    total = 0
    names = []
    for route in routes:
        if route.trip_day == trip_day:
            total += route.trip_miles
            names.append(route.name)
    print ("Plan for hiking day", trip_day, "", round(total, 2), "miles hiked ", names)
