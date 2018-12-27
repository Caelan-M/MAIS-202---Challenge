import pandas as pd
import matplotlib.pyplot as plt
import csv

member_list = pd.read_csv('../MAIS 202 - Challenge/mais-202-coding-challenge-master/data.csv', index_col=None)
purposes = list()
formatted_purposes = list()
new_purpose = True
labels = ['purpose', 'avg_rate']

# purposes.columms = ['Purpose', 'Total', 'Number', 'Average']

# sum the rate for eac purpose
for index, member in member_list.iterrows():
    new_purpose = True
    for purpose in purposes:
        if purpose[0] == member['purpose']:
            purpose[1] = purpose[1] + member['int_rate']
            purpose[2] = purpose[2] + 1
            new_purpose = False;
    if new_purpose is True:
        purposes.append([member['purpose'], member['int_rate'], 1, 0])
        new_purpose = False


# Find average rate for each purpose
for purpose in purposes:
    purpose[3] = purpose[1] / purpose[2]

# Create new list formatted for table
for purpose in purposes:
    formatted_purposes.append([purpose[0], purpose[3]])

# Plot graph and display it
df = pd.DataFrame.from_records(formatted_purposes, columns=labels)
plt.rcParams.update({'font.size': 10})
df.plot.bar(x='purpose', y='avg_rate')
plt.show()
