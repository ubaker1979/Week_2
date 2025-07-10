#GIS 4085
#Calculated miles per day traveled

import arcpy
wksp = arcpy.env.workspace = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\GIS4085_Week2.gdb'
arcpy.env.overwriteOutput = True

def trail_miles(trail):
    try:
        miles = [0]
        with arcpy.da.SearchCursor(trail, "Miles") as cursor:
            for row in cursor:
                miles += row[0]

        if miles == 0:
            print(f"No miles")
        else:
            print(f"The trail is {miles} long")

    except:
        print(arcpy.GetAllMessages(2))
        
