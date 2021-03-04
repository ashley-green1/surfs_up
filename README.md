# Surfs Up

## Project Overview

"Surfs Up," the surf shop is seeking to expand and Oahu, Hawaii is on the shop owner's radar as a potential location.  In addition to offering surfing gear, there would be an ice cream shop included with the expansion.  

We have already determined that the average annual weather conditions for Oahu are good, but we specifically want to know if operating the surf and ice cream shop is sustainable year round.  

There are concerns that June and December weather conditions are a risk to operating year round, so lets analyze the weather data found in hawaii.sqlite.  

Using an SQL Lite Viewer, we can see that the data includes temperature and precipitation measurements from 01/01/2010-08/23/2017.  This will give us a reliable analysis of June and December weather conditions. We will dive further into this data using SQLAlchemy, a Python SQL toolkit and Object Relationship Manager.


## Resources
- Data Source: hawaii.sqlite
- Software: SQLite, SQLAlchemy, Flask, VS Code


## Results
### June Temperature Statistics

Following at the temperature statistics for June
*  average temperature is 74.94 degrees
*  the temperature ranges from 64-85 degrees
*  the temperature is 77 degrees or higher for about one week out of the month

![June_Temps](https://github.com/ashley-green1/surfs_up/blob/main/June_Temperature_Stats.png)


### December Temperature Statistics

  Following at the temperature statistics for December
*  average temperature is 71.04 degrees
*  the temperature ranges from 56-83 degrees
*  the temperature is 69 degrees or lower for about one week out of the month

![December_Temps](https://github.com/ashley-green1/surfs_up/blob/main/December_Temperature_Stats.png)


## Summary

When surfing, the 80s can be uncomfortable and the 60s typically require a wetsuit, but the 70s are just about right.  

With December being one of the coldest months of the year, we can see from the lower quartile and that temperatures range from 56-69 for about one week.  Thats not too bad.  The colder weather may drive sales for wetsuits and other related gear, which is good for business.  However, ice cream sales may not be as rewarding. 

June presents almost the opposite with the hottest week of the month randing from 77 to 85 degrees.  This is good for ice cream sales to cool those who may get uncomfortable in the higher temperatures.  

To dive deeper, we decided to analyze the precipitation statistics taking the same steps we used to get the temperature stats.  Per wikipedia "Heavy rain is when the precipitation rate is > 7.6 mm (0.30 in) per hour."  Rain can reduce foot traffic and compromise ice cream sales, or worse, skiers may sit the day out.

Precipitation in June averages 0.14 mm and can range from 0-4.43 mm. We can conclude that there is at least one slightly rainy day per month that may deter skiers. However, majority of the month, precipitation is less than 0.12 mm.

![June_Prcp](https://github.com/ashley-green1/surfs_up/blob/main/June_Precipitation_Stats.png)

Precipitation in December averages 0.21 mm, but can range from 0-6.42 mm.  We can conclude that there is at least one nearly heavy rain day per month that may deter skiers. However, majority of the month, precipitation is less than 0.15 mm.

![Dec_Prcp](https://github.com/ashley-green1/surfs_up/blob/main/December_Precipitation_Stats.png)

After analyzing both the temperature and precipitation for the 2 risky months of June and December, we've reveal that there are no threats to the stability of the business operating year round.  Expanding to the Oahu, Hawaii location would be a great addition to the Surfs Up retail ventures.