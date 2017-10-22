rm(list = ls())
library(readr)

base_data <- read_csv("./cleanedArizona.csv")#, col_types = col_spec)
colnames(base_data) <- c("year", "month", "hour", "weekday", "zip", "long", "lat", "crime")

weekdays <- base_data$weekday
weekend_indices <- weekdays == "Friday" | weekdays == "Saturday"
sunday_indices <- weekdays == "Sunday"
workweek_indices <- !(weekend_indices | sunday_indices)

liquor_crimes <- subset(base_data, base_data$crime == "Liquor")
table(liquor_crimes$month)


#Uninteresting-the crime rate just varies with population density
zips <- as.factor(base_data$zip)
table(zips)


 table(weekdays)

 crimes <- as.factor(base_data$crime)
table(crimes)
 names(which.max(table(crimes)))



weekend_crimes <- as.factor(base_data$crime[weekend_indices])
table(weekend_crimes)
# 
not_weekend_crimes <- as.factor(base_data$crime[!weekend_indices])
table(not_weekend_crimes)
# 
sunday_crimes <- as.factor(base_data$crime[sunday_indices])
table(sunday_crimes)
# 
workweek_crimes <- as.factor(base_data$crime[workweek_indices])
table(workweek_crimes)
# 
months <- base_data$month
table(months)

years <- base_data$year
table(years)
