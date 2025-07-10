#HW2. Functions
#Call a function within the same script: Write a Python script that contains a function to select backcountry campsites within 200 feet of trails. 
#Print the campsite names to the console. 
#Call the function within the same script.

import arcpy
arcpy.env.overwriteOutput = True
wksp = arcpy.env.workspace = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\HW2_RMNP\HW2_RMNP.gdb'
campsites = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\GIS4085_Week2.gdb\ROMO_BackcountryCampsites'
trails = r'C:\GIS 4085 Python Programming II in GIS\Week 2\GIS4085_Week2_Data\GIS4085_Week2.gdb\NPS_trails'


#Select by location campsites within 200 feet from trails and make a layer from selected features
campsites_layer = "campsites_lyr"
trails_layer = "trails_lyr"
arcpy.management.MakeFeatureLayer(campsites, campsites_layer)
arcpy.management.MakeFeatureLayer(trails, trails_layer)
arcpy.management.SelectLayerByLocation(campsites_layer, 'WITHIN_A_DISTANCE', trails, '200 Feet', 'NEW_SELECTION')
selected_campsites_layer = "selected_campsites_200ft_lyr"
arcpy.management.MakeFeatureLayer(campsites_layer, selected_campsites_layer)
print(f"Feature layer '{selected_campsites_layer}' created with selected campsites.")
                                     
count = arcpy.management.GetCount(selected_campsites_layer)
print(f"Number of selected campsites: {count}")

try:
    with arcpy.da.SearchCursor(selected_campsites_layer, 'Campsite') as cursor:
        for row in cursor:
            print(row[0]) # row[0] refers to the value of the first field in the list (name_field)
except Exception as e:
    print(f"Error accessing campsite names: {e}")
    print(f"Please check if the field 'Campsite' exists in your 'ROMO_BackcountryCampsites' feature class.")

arcpy.management.SelectLayerByAttribute(campsites_layer, 'CLEAR_SELECTION')