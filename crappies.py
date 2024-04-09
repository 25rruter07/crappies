
##############################################################################
#   p324_honey_production_3.py
#  
#      create first graph with all states - this results in too much data
#      to analyze
##############################################################################
import matplotlib.pyplot as plt
import pandas as pd

# Load in the data with read_csv()
df = pd.read_csv("crappie.csv", header=0)

# data cleansing
#print(df['Value'])
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df.dropna(subset=['Value'], inplace=True) 
#print("----- CLEAN DATA -----")
#print(df['Value'])

# get list of unique state names
unique_states = df['State'].unique()

# parse and store pandas data
all_honey = []
all_states = []
for state in unique_states:
  # match this state in the State column, 
  # group each years worth of data for that state,
  # and retreive values from the Value column
  honey_data =  df[df['State'] == state].groupby('Year')['Value']
  # sum the values and store in an array
  all_honey.append(honey_data.sum())
  # store the state
  all_states.append(state)

# show all states - too much data!
for i in range(len(all_honey)):
  # get the state and its honey values
  honey = all_honey[i]
  state = all_states[i]
  # the keys in the honey data structure are the years
  years = honey.keys()
  if sum(honey) < small_vol:
    plt.plot(honey.keys(), honey, label=state, marker="o")
    plt.plot(honey.keys(), honey, label=state)
plt.xlabel('Year')
plt.ylabel('Production levels')
plt.title('LOW HONEY PRODUCERS')
plt.legend()
plt.show()

for i in range(len(all_honey)):
  # get the state and its honey values
  honey = all_honey[i]
  state = all_states[i]
  # the keys in the honey data structure are the years
  years = honey.keys()
  if sum(honey) <= mid_vol and sum(honey) >= small_vol:
    plt.plot(honey.keys(), honey, label=state, marker="o")
    plt.plot(honey.keys(), honey, label=state)
plt.xlabel('Year')
plt.ylabel('Production levels')
plt.title('MID-LEVEL HONEY PRODUCERS')
plt.legend()
plt.show()

for i in range(len(all_honey)):
  # get the state and its honey values
  honey = all_honey[i]
  state = all_states[i]
  # the keys in the honey data structure are the years
  years = honey.keys()
  if sum(honey) > mid_vol:
    plt.plot(honey.keys(), honey, label=state, marker="o")
    plt.plot(honey.keys(), honey, label=state)
plt.xlabel('Year')
plt.ylabel('Production levels')
plt.title('LARGE HONEY PRODUCERS')
plt.legend()
plt.show()

for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  honey_mean = honey_data.mean()
  plt.plot(honey_mean.keys(), honey_mean, label=state, marker="o")
  plt.plot(honey_mean.keys(), honey_mean, label=state)
plt.ylabel('Production Levels')
plt.xlabel('Year')
plt.title('STATE AVERAGES')
plt.show()

unique_years = df['Year'].unique()
for year in unique_years:
  totals = df[df['Year'] == year].groupby('Year')['Value']
  totals_sum = totals.sum()
  plt.bar(totals_sum .keys(), totals_sum, label=year)
plt.ylabel('Production levels')
plt.xlabel('Year')
plt.title('US TOTAL PRODUCTION')
plt.show()
