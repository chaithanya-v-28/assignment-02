#Ask for exact birth input
birth_input = input("enter your birth date(DD/MM/YYYY): ")
#split input and convert to int
day,month,year = map(int,birth_input.split("/"))
from datetime import date
#creat a birth date object
birth_date = date(year,month,day)
#get todays date
today = date.today()
#calculate exact age in days
age_days = (today - birth_date).days
#convert days into years
age_years = age_days // 365            # used floor division so it can give only integer value or whole number
#convert years to month
age_months = age_years * 12
#convert days to hours
age_hours = age_days * 24
#convert days to hours
age_minutes = age_hours * 60
#calculate years until 100
years_to_100 = 100 - age_years
#Display outputs
print("Exact age details")
print("Current age: ",age_years,"years")
print("Age in months: ",age_months,"months")
print("Age in days: ",age_days,"days")
print("Age in hours: ",age_hours,"hours")
print("Age in minutes: ",age_minutes,"minutes")
print("Years until 100:",years_to_100,"years")
