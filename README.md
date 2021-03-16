Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.<br>

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.<br>

In this project, I used data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I compared the system usage between three large cities: Chicago, New York City, and Washington, DC.<br>

The Datasets Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:<br>
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Start Time (e.g., 2017-01-01 00:07:57)<br>
End Time (e.g., 2017-01-01 00:20:53)<br>
Trip Duration (in seconds - e.g., 776)<br>
Start Station (e.g., Broadway & Barry Ave)<br>
End Station (e.g., Sedgwick St & North Ave)<br>
User Type (Subscriber or Customer)<br>

The Chicago and New York City files also have the following two columns: <br>

Gender<br>
Birth Year<br>

I learnt about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, I wrote code to provide the following information:

1 Popular times of travel (i.e., occurs most often in the start time)
----------------------------------------------------------------------

most common month<br>
most common day of week<br>
most common hour of day<br>


2 Popular stations and trip
----------------------------------------------------------------------
most common start station<br>
most common end station<br>
most common trip from start to end (i.e., most frequent combination of start station and end station)<br>

3 Trip duration
------------------

total travel time average travel time

4 User info
------------

counts of each user type<br>
counts of each gender (only available for NYC and Chicago)<br>
earliest, most recent, most common year of birth (only available for NYC and Chicago)<br>
