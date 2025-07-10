#HW2_4085 Bear Lake loop
#Write a new Python script to select backcountry campsites within 100ft of the Bear Lake Loop feature class, see the image below for the route. 

import arcpy
arcpy.env.overwriteOutput = True
wksp = arcpy.env.workspace = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\HW2_RMNP\HW2_RMNP.gdb'

BearLakeBuffer100 = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\GIS4085_Week2.gdb\BearLakeBuffer'

#Create a 100 foot buffer around Bear Lake Loop
arcpy.analysis.Buffer('BearLakeLoop', BearLakeBuffer100, '100 FEET', 'FULL', 'ROUND')

#Select campsites within the buffer
campsites = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\GIS4085_Week2.gdb\ROMO_BackcountryCampsites'
arcpy.management.SelectLayerByLocation(campsites, 'WITHIN', BearLakeBuffer100, 'NEW_SELECTION')

