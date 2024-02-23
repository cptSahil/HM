"""
    A dictionary which has the name of the day as the key and value as a tuple with following values
		i. Occurence of the day in a week (e.g. 1 for Monday, 2 for Tuesday)
		ii. Short form of the day (first three letters)
		iii. name of the day in the lower case
		iv. name of the day in the upper case
		v. length of each name
"""
def week_details():
    """
        Return the WEEK DETAILS of each days such as day_occurance, short_name, lower_casename, etc.
    """
    week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    day_details = {}
    for day in week_days:
        day_occurence = week_days.index(day)+1
        short_name = day[:3]
        lower_casename = day.lower()
        upper_casename = day.upper()
        length_of_day = len(day)
        day_details[day] = (day_occurence,short_name,lower_casename,upper_casename,length_of_day)
    return day_details

if __name__ == "__main__":
    Days_Details_Info = week_details()
    print(Days_Details_Info)
