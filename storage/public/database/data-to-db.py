import mysql.connector
import pandas as pd


mydb=mysql.connector.connect(
    host='localhost',
    user='homestead',
    passwd='secret',
    database='masonite',
    port=33060
)

csv=pd.read_csv('database.csv')

mycursor = mydb.cursor()
csv_data=csv.values.tolist()

sql='INSERT INTO stats (country,longitude,latitude,total_cases,active_cases,recovered_cases,total_deaths) VALUES (%s,%s,%s,%s,%s,%s,%s)'
val=[]

for temp in csv_data:
    total_cases=temp[3]
    active_cases=temp[4]
    total_deaths=temp[5]
    total_recoveries=temp[6]
    longitude=temp[1]
    latitude=temp[2]
    val.append((str(temp[0]),str(longitude),str(latitude),str(total_cases),str(active_cases),str(total_recoveries),str(total_deaths)))

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")