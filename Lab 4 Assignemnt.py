"""Name: Hillol Dutta
Date created: 14-Feb-2020
Version of Python you are using: Python 3.4.
Very brief description of the assignment or the assignment name: Three Scripts are used here.
Exercise one is writing a function that capitalizes the first and fourth letters of a name.
Exercise two is to parse and manage a multi-line string.
Exercise three is a code to extract a part of a string."""

#Exercise 1: It capitalizes the first and fourth letters of a name.
name='Hillol' #defines the string.
name = name[:3].capitalize() + name[3:].capitalize()  #command for capitalizing first and fourth letter  
print(name) #prints out the capitalized word


#Exercise 2: It parses and manages a multi-line string.

#-*- coding: utf-8 -*-

# Scraped multi-line String
forecast = '''

Tonight
ClearLow: 55 F

Thursday
Sunny thenChanceShowersHigh: 77 F

Friday
SunnyHigh: 73 F

Saturday
Mostly SunnyHigh: 77 F

Sunday
Mostly SunnyHigh: 71 F'''

# Split string into a list
forecast_list = forecast.split('\n\n')
#print(forecast_list)

# Use two blank lines (\n\n) as the separator
# Creates a list item at every instance of separator


# Loop through list to make string replacements to each item
# Remove extra whitespaces or lines for a cleaner format
for day in forecast_list:
    day = day.replace('\n',': ')
    day = day.replace('High',' High')
    day = day.replace('Low','Low')
    day = day.replace('Clear','Clear, ')
    day = day.replace('then','then ')
    day = day.replace('Chance','Chance ')
    day = day.replace('Showers','Showers,')
    day = day.replace('Sunny thenChanceShowersHigh','Sunny then Chance Showers High')
    day = day.replace('Sunny','Sunny,')
    
    # add your code here
    print(day)

#Exercise 3: Extracts Latitude and Longitude from a url.
    
x="https://www.google.com/maps/@42.2509428,-71.8249939,17z"

print("Latitude: "+x[29:39])
print("Longitude: "+x[40:52])


