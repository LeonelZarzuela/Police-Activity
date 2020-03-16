import matplotlib.pyplot as plt
import pandas as pd

ri = pd.read_csv('Police_Data.csv')
plt.style.use('fivethirtyeight')

def Clean_Data():
    ri.drop(['state', 'county_name'], axis='columns', inplace=True)
    ri.dropna(subset=['driver_gender'],inplace=True)
    ri['Arrested']= ri.is_arrested.astype(bool)
    combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
    ri['Stop Date and Time']= pd.to_datetime(combined)
    ri.set_index('Stop Date and Time', inplace=True)
    ri.to_csv('Police_Data.csv')

def Drug_Stops():
    combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
    ri['Stop Date and Time']= pd.to_datetime(combined)
    ri.set_index('Stop Date and Time', inplace=True)

    print(ri.drugs_related_stop.resample('A').mean())
    annual_drug_rate = ri.drugs_related_stop.resample('A').mean()
    annual_drug_rate.plot()
    plt.ylabel('Drug Related Stop Rate')
    plt.show()

def Search_Drug():
    combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
    ri['Stop Date and Time']= pd.to_datetime(combined)
    ri.set_index('Stop Date and Time', inplace=True)

    annual_search_rate = ri.search_conducted.resample('A').mean()
    annual_drug_rate = ri.drugs_related_stop.resample('A').mean()
    annual = pd.concat([annual_drug_rate, annual_search_rate], axis='columns')
    annual.plot(subplots=True)
    plt.show()

def District_Violation():
    print(pd.crosstab(ri.district, ri.violation))
    zones = pd.crosstab(ri.district, ri.violation)
    print(zones)
    zones.plot(kind='barh',stacked=True)
    plt.xlabel('Amount')
    plt.show()

Clean_Data()
Drug_Stops()
Search_Drug()
District_Violation()