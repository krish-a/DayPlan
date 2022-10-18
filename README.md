# DayPlan

For this project, I decided to use the Google Maps API. \n
I found the coordinates of indianapolis online and searched for "local stores, shops, and destinations" within a certain radius. 
I generated a dataframe of these places and their website, rating, price, and address.
I outputted this dataframe into **data.csv**
From this list, I used the sorted by the rating to find the places I'd most want to go to.
I also used the price (scale of 1-5) to find which place I'd want to spend more time at (the more expensive, the less time i'd spend here).
I then created a data frame that contained the places and the amount of time I'd spend at each from 9 AM to 9 PM and outtputted it to **plan.csv**
