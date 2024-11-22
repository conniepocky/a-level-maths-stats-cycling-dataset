import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import datetime

data = pd.read_csv('data/cyclingdata.csv')

print(data.head())

# cleaning dataset, remove rows with missing values and convert all values to same format

data = data.dropna()

# put all months in same format, e.g change feb to febuary

month_map = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December',
}

data["month of accident"] = data["month of accident"].str.strip().apply(lambda x: month_map.get(x, x))

#time clean up

def convert24(time):
    timestr = time.strip().lower().replace(" ", "")

    if timestr == "noon":
        return "12:00"
    
    if re.match(r"^\d{3,4}$", timestr):
        return f"{int(timestr[:2]):02}:{timestr[2:]:02}"
    
    for format in ["%I:%M%p", "%I%p", "%H.%M", "%H:%M", "%I.%M%p", "%I.%M %p", "%H%M"]:
        try:
            return datetime.datetime.strptime(timestr, format).strftime("%H:%M")
        except ValueError:
            pass

    return ValueError(f"Cannot parse time: {timestr}")

data["time of accident"] = data["time of accident"].apply(convert24)

# exercise 15.2 q7, box plot to show ages of cyclist wearing helmets and not

sns.boxplot(x="age", y="wearing a helmet?", data=data)
plt.show()