import pandas as pd
import numpy as np
import os
import requests
import time
from urllib.parse import urljoin
import regex

from bs4 import BeautifulSoup as bs
import pandas as pd
import pyodbc


# crime_data = pd.read_csv('SPD_Crime_Data__2008-Present.csv')
# print(crime_data['MCPP'].unique())
# print(crime_data.columns)
# print(crime_data['Report Number'].head())

# Filter crimes according to neighborhood
# neighborhoods = pd.read_csv('neighborhoods.csv')
# print(crime_data['MCPP'].unique())
# crime_filter = crime_data.loc[crime_data['MCPP'].isin(neighborhoods.neighborhood)]
# print(crime_filter.head())
# print(crime_filter['MCPP'].nunique())
# print(neighborhoods.shape)
# crime_filter.to_csv('crime_filtered.csv', index=False)

#
# density_data = pd.read_csv('density2.csv').dropna()
# list_of_blocks = density_data.neighborhood
# print(density_data.head(5))


# print(list_of_blocks)
# out = 'neighborhoods.csv'
# list_of_blocks.to_csv(out, index=False)
# out2 = 'density.csv'
# list_of_density = density_data['population thousand per square mile'].dropna()
# list_of_density.to_csv(out2, index=False)
# d2 = pd.read_csv('density2.csv')
# d2 = d2.dropna()
# out3 = 'density2.csv'
# d2.to_csv(out3, index=False)

# Data for crimetype and crime against
# crime = pd.read_csv('crime_filtered.csv')
# crime_against = crime['Crime Against Category'].unique()
# crime_against_df = pd.DataFrame(crime_against, columns=['crime_against'])
# crime_type = crime['Offense'].unique()
# crime_type_df = pd.DataFrame(crime_type, columns=['crime_type'])
# crime_type_df.to_csv('crime_type.csv', index=False)
# crime_against_df.to_csv('crime_against.csv', index=False)

# data = pd.read_csv('crime_filtered.csv')
# print('startTime')
# data['Offense Start DateTime'] = pd.to_datetime(data['Offense Start DateTime'], errors='coerce')
# print('endTime')
# data['Report DateTime'] = pd.to_datetime(data['Report DateTime'], errors='coerce')
# print('reportTime')
# data['Offense End DateTime'] = pd.to_datetime(data['Offense End DateTime'], errors='coerce')
# data.to_csv('crime_fixedTime.csv')


# push data to database
def push_to_db():
    print("working")
    data = pd.read_csv('crime_fixedTime.csv')
    print(data.shape)
    # test_data['d1'] = [1.0, 1.0, 1.0, 1.0, 1.0]
    server = 'info430.database.windows.net'
    database = 'info430_project'
    username = 'infomemeber'
    password = 'password123!'
    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()
    # for index, row in density_data.iterrows():
    #     cursor.execute("INSERT INTO dbo.Density(density) values (?)", row['population thousand per square mile'])
    # for index, row in data.iterrows():
    #     cursor.execute("INSERT INTO dbo.CrimeTypes(CrimeTypeName) values (?)", row['crime_type'])
    # conn.commit()
    # cursor.close()
    # for index, row in test_data.iterrows():
    #     cursor.execute(
    #         "INSERT into dbo.Test(fk) "
    #         "values((SELECT CrimeAgainstID from dbo.CrimeAgainst "
    #         "WHERE dbo.CrimeAgainst.CrimeAgainstType = ?))", row['Crime Against Category']
    #     )
    # conn.commit()
    # cursor.close()
    print('loop_starting')
    for index, row in data.iterrows():
        if index % 100 == 0:
            print('Current progress:' + str(index))
        # print(row['Offense End DateTime'])
        # print(index)
        # try:
        cursor.execute(
            "INSERT INTO dbo.Crime(reportNumber, reportTime, crimeAgainstId,"
            "crimeTypeId, densityId, neighborhoodId, longitude, latitude)"
            "values("
            "   ?,"
            "   ?,"
            "   (SELECT CrimeAgainstID FROM dbo.CrimeAgainst WHERE dbo.CrimeAgainst.CrimeAgainstType = ?),"
            "   (SELECT CrimeTypeID FROM dbo.CrimeTypes WHERE dbo.CrimeTypes.CrimeTypeName = ?),"
            "   (SELECT id FROM dbo.Neighborhood WHERE dbo.Neighborhood.name = ?),"
            "   (SELECT id FROM dbo.Neighborhood WHERE dbo.Neighborhood.name = ?),"
            "   ?,"
            "   ?"
            ")",
            row['Report Number'],
            row['Report DateTime'],
            row['Crime Against Category'],
            row['Offense'],
            row['MCPP'],
            row['MCPP'],
            row['Longitude'],
            row['Latitude']
        )
        # except:
        #     print(row['Offense End DateTime'])
        #     print(row)
    conn.commit()
    cursor.close()


#
if __name__ == '__main__':
    push_to_db()
    # data = pd.read_csv('crime_fixedTime.csv')
    # print(data['Report DateTime'].isna().values.any())
    # data = pd.read_csv('crime_filtered.csv')
    # test_data = data.head()

    # for index, row in test_data.iterrows():
    #     print(type(row['MCPP']))
    # print(test_data)
    # # print(test_data['Latitude'].dtypes)
