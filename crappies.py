
##############################################################################
#   p324_Catch_production_3.py
#  
#      create first graph with all counties - this results in too much data
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

# get list of unique county names
unique_counties = df['county'].unique()

# parse and store pandas data
all_Catch = []
all_counties = []
for county in unique_counties:
  # match this county in the county column, 
  # group each years worth of data for that county,
  # and retreive values from the Value column
  Catch_data =  df[df['county'] == county].groupby('Year')['Value']
  # sum the values and store in an array
  all_Catch.append(Catch_data.sum())
  # store the county
  all_counties.append(county)

# show all counties - too much data!
for i in range(len(all_Catch)):
  # get the county and its Catch values
  Catch = all_Catch[i]
  county = all_counties[i]
  # the keys in the Catch data structure are the years
  years = Catch.keys()
  '''if sum(Catch) < small_vol:
    plt.plot(Catch.keys(), Catch, label=county, marker="o")
    plt.plot(Catch.keys(), Catch, label=county)
plt.xlabel('Year')
plt.ylabel('Production levels')
plt.title('LOW Catch PRODUCERS')
plt.legend()
plt.show()'''

for i in range(len(all_Catch)):
  # get the county and its Catch values
  Catch = all_Catch[i]
  county = all_counties[i]
  # the keys in the Catch data structure are the years
  years = Catch.keys()
  '''if sum(Catch) <= mid_vol and sum(Catch) >= small_vol:
    plt.plot(Catch.keys(), Catch, label=county, marker="o")
    plt.plot(Catch.keys(), Catch, label=county)
plt.xlabel('Year')
plt.ylabel('Production levels')
plt.title('MID-LEVEL Catch PRODUCERS')
plt.legend()
plt.show()'''

for i in range(len(all_Catch)):
  # get the county and its Catch values
  Catch = all_Catch[i]
  county = all_counties[i]
  # the keys in the Catch data structure are the years
  years = Catch.keys()
'''if sum(Catch) > mid_vol:
    plt.plot(Catch.keys(), Catch, label=county, marker="o")
    plt.plot(Catch.keys(), Catch, label=county)
plt.xlabel('Year')
plt.ylabel('Production levels')
plt.title('LARGE Catch PRODUCERS')
plt.legend()
plt.show()'''

for county in unique_counties:
  Catch_data = df[df['county'] == county].groupby('Year')['Value']
  Catch_mean = Catch_data.mean()
  plt.plot(Catch_mean.keys(), Catch_mean, label=county, marker="o")
  plt.plot(Catch_mean.keys(), Catch_mean, label=county)
plt.ylabel('Production Levels')
plt.xlabel('Year')
plt.title('county AVERAGES')
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
