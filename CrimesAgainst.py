# Script to insert data into the CrimesAgainst table inside Crimes Database

import pandas as pd
import pyodbc

# Filter for the unique types of crime against types and inserts them into the database
def uq_crime_againsts():
    df = pd.read_csv('SPD_Crime_Data.csv')
    uq_crime_againsts = df['Crime Against Category'].unique()
    uq_crime_againsts_df = pd.DataFrame(
        uq_crime_againsts, columns=['CrimeAgainstCategory'])

    server = 'info430.database.windows.net'
    database = 'info430_project'
    username = 'infomemeber'
    password = 'password123!'
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)
    cursor = conn.cursor()
    for index, row in uq_crime_againsts_df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.CrimeAgainst (CrimeAgainstType) values(?)", row.CrimeAgainstCategory)
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    uq_crime_againsts()
