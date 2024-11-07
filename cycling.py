import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

print(data["month of accident"].unique())