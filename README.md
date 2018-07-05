# wxinfo

Simple Python utility for extracting and reporting general statistical information of interest from the logfiles of a home weather station (or other sensor system of some kind).  

## Input 

Wxinfo expects to read a weather station logfile, called “wxlogfile.txt”, containing a series of lines of data, each of which is of the form: `date,time,temperature,barometer`
Where:
* `date` = the date the weather data was recorded, in the form MM/DD/YY, e.g. 03/27/2018 for March 27, 2018
* `time` = the time of day the weather data was recorded, in the form hh:mm on a 24-hour clock, e.g. 13:53 = 1:53pm.
* `temperature` = the temperature reading in degrees Farenheit, e.g., 62.7
* `barometer` = the barometric pressure in inches of mercury, e.g. 28.85
The logfile could contain any number of lines of recorded data, over the period of many days.

## Output

Wxinfo sends the summary report it generates via email to an address specified in the Python script.  Edit the script to change the recipient address (or addresses)
