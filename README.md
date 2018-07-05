# wxinfo

Simple Python utility for extracting and reporting general statistical information of interest from the logfiles of a home weather station (or other sensor system of some kind).  

## Input 

Wxinfo expects to read a weather station logfile, called “wxlogfile.txt”, containing a series of lines of data, each of which is of the form: `datetime,sample#,temperature,barometer`
Where:
* `datetime` = the date and time the weather data was recorded, in ISO 8601 format, which allows capturing the date, the time, and the timezone.  As an example, `2018-06-29T12:37:00-0700` is 12:37:00 local time on June 29th, 2018, in a timezone with an offset of -7 hours (-0700) from GMT.
* `sample#` = a sequential sample number reported by the weather station, which can help detect when samples might be missing or otherwise unreported
* `temperature` = the temperature reading in degrees Farenheit, e.g., 62.7
* `barometer` = the barometric pressure in inches of mercury, e.g. 28.85
The logfile could contain any number of lines of recorded data, over the period of many days.

## Output

Wxinfo sends the summary report it generates via email to an address specified in the Python script.  Edit the script to change the recipient address (or addresses)
