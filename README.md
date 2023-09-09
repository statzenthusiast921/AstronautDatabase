# AstronautDatabase

### Description

The purpose of this project was to visualize the networks of all astronauts connected by each mission for which they participated. 

### Data

The data used for this analysis was scraped from the [SuperCluster Astronaut Database](https://www.supercluster.com/astronauts).

### Application
[Click here] (https://astro-db-jz.onrender.com/).  The app might need a few minutes to "wake up".

### Challenges

Scraping the data proved to be tricky as the countries of origin did not populate appropriately for many astronauts.  Because of this, manual research was required to fill out this portion of the dataset.  Two problems arose through this process:
- How to assign countries to astronauts with dual citizenship
- How to assign countries to cosmonauts around the fall of the Soviet Union (USSR vs. Russia)

The first problem was resolved by assigning a country based on where the mission originated (eg: Astronaut born in UK, but participated in NASA mission was listed under United States of America).  The second problem was resolved by assigning the first country listed under the astronaut profile on the SuperCluster website.

Another challenge involved the speed at which the dashboard was loading.  Initially, the entire scraping process was performed from scratch to construct a dataset each time the dashboard was loaded.  Building the dashboard in this way slowed the processing speed down immensely. Thus, a static version of the dataset was downloaded after scraping and all records were cut off after December 31, 2021.
