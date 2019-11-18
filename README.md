# BigDataAnalysis-Project
# Project Title

Big Data Analysis Project- Weather

## Getting Started
This project will have you perform Data Analysis and processing using MapReduce/ Apache Spark. The Project will use the weather dataset from https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/ 
.This project will use only 19 years of data ( 2000 - 2019) for all the stations starting with US and elements TMAX, TMIN. The dataset is available on the CEAS hadoop directory /user/tatavag/weather.

The following information serves as a definition of each field in one line of data covering one station-day. Each field described below is separated by a comma ( , ) and follows the order presented in this document. 

ID = 11 character station identification code

 YEAR/MONTH/DAY = 8 
 
character date in YYYYMMDD format (e.g. 19860529 = May 29, 1986) 
ELEMENT = 4 character indicator of element type
 DATA VALUE = 5 character data value for 
ELEMENT M-FLAG = 1 character Measurement Flag 
Q-FLAG = 1 character Quality Flag 
S-FLAG = 1 character Source Flag 
OBS-TIME = 4-character time of observation in hour-minute format (i.e. 0700 =7:00 am)
 See section III of the GHCN-Daily ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt  file for an explanation of ELEMENT codes and their units as well as the M-FLAG, Q-FLAGS and S-FLAGS. The OBS-TIME field is populated with the observation times contained in NOAA/NCDC’s Multinetwork Metadata System (MMS). 

In particular, it will have you build a hadoop map/reduce or Apache Spark that yields the following analysis.:
 *  Average TMIN, TMAX for each year excluding abnormalities or missing data
 *  Maximum TMAX, Minimum TMIN for each year excluding abnormalities or missing data
 *  5 hottest , 5 coldest weather stations for each year excluding abnormalities or missing data 
 *  Hottest and coldest day and corresponding weather stations in the entire dataset

Using the Hadoop streaming API, python mapper and reducer scripts, weather data is analyzed and Average minimum temperature and maximum temperature is displayed. Used Hive to calculate Median for TMAX and TMIN.

### Prerequisites
Install Hadoop and python in order to run mapper.py and reducer.py.

Install Hive.

### Steps in execution for Map Reduce code.
* Write mapper.py and reducer.py. 
* Then change access permission of mapper and reducer.
* Run the Mapreduce on Hadoop

     $ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file /home/patilay/mapper.py -mapper /home/patilay/mapper.py -file /home/patilay/reducer.py -reducer /home/patilay/reducer.py -input /user/tatavag/weather  -output /tmp/weatherOutput/
     
* Get the result
     $ hdfs dfs -cat /tmp/weatherOutput/part*
### Steps in execution for Hive QL.
•	Ran the Script given below to get data in /user/patilay/weather

	for i in `seq 2000 2019` do wget https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/${i}.csv.gz gzip -cd ${i}.csv.gz | grep -e TMIN -e TMAX | grep ^US > ${i}.csv 
done
•	Type command hive on Hadoop server.

•	Run the Queries to create table.

•	Run further queries to calculate Median for TMAX and TMIN of the weather dataset.



## References

 * http://rare-chiller-615.appspot.com/mr1.html
 * http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/ 


