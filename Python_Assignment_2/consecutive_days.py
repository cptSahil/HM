"""
   A list of tuples which has the two consequtive days grouped together
"""
def two_consecutive_days():
    """
       Return a list of tuples containing consecutive pairs of days. 
    """
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    consecutive_day = []

    for i in range(len(days)-1):
        consecutive_day.append((days[i], days[i+1]))
    return consecutive_day

if __name__ == "__main__":
    consecutive_days = two_consecutive_days()
    print(consecutive_days)
