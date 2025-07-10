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
trail01 = Route("Bear Lake Loop Trail", 15, trail_miles(0.1), 1)
trail02 = Route("Bear Lake Loop Trail", 16, trail_miles(0.02), 1)
trail03 = Route("Bear Lake Loop Trail", 17, trail_miles(0.02), 1)
trail04 = Route("Bear Lake To Bierstadt Junction Trail", 3, trail_miles(0.04), 1)
trail05 = Route("Bear Lake To Bierstadt Junction Trail", 14, trail_miles(0.27), 1)
trail06 = Route("Flattop Mountain Trail Junction - Cub Lake", 13, trail_miles(0.73), 1)
trail07 = Route("Flattop Mountain Trail Junction - Cub Lake", 10, trail_miles(0.50), 1)
trail08 = Route("Flattop Mountain Trail Junction - Cub Lake", 2, trail_miles(0.70), 1)
trail09 = Route("Flattop Mountain Trail Junction - Cub Lake", 8, trail_miles(0.20), 2)
trail10 = Route("Flattop Mountain Trail Junction - Cub Lake", 1, trail_miles(1.50), 2)
trail11 = Route("The Pool - Cub Lake Trailhead", 6, trail_miles(0.84), 2)
trail12 = Route("The Pool/Odessa Lake", 4, trail_miles(0.84), 3)
trail13 = Route("The Pool/Odessa Lake", 7, trail_miles(1.10), 3)
trail14 = Route("The Pool/Odessa Lake", 9, trail_miles(0.79), 3)
trail15 = Route("Odessa Lake - Flattop Mtn. Junc.", 5, trail_miles(1.00), 4)
trail16 = Route("Odessa Lake - Flattop Mtn. Junc.", 11, trail_miles(2.00), 4)
trail17 = Route("Flattop Mountain Trail", 12, trail_miles(0.50), 4)
trail18 = Route("Bear Lake to Bierstadt Junction Trail", 14, trail_miles(0.27), 4)
trail19 = Route("Bear Lake Loop Trail", 15, trail_miles(0.1), 4)
trail20 = Route("Bear Lake Loop Trail", 17, trail_miles(0.02), 4)
trail21 = Route("Bear Lake Loop Trail", 16, trail_miles(0.02), 4)

routes = [trail01, trail02, trail03, trail04, trail05, trail05, trail06, trail07, trail08, trail09, trail10, trail11, trail12, trail13, trail14, trail15, trail16, trail17, trail18, trail19, trail20, trail21]

#loop through each day

for trip_day in [1, 2, 3, 4]:
    total = 0
    names = []
    for route in routes:
        if route.trip_day == trip_day:
            total += route.trip_miles
            names.append(route.name)
    print ("Plan for hiking day", trip_day, "", round(total, 2), "miles hiked ", names)
