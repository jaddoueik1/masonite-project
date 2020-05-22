from covid import Covid
import pandas as pd 


covid = Covid()
data=covid.get_data()
i=0
channels_list=[]
channels=['countryName','longitude','lattitude','total_cases','active_cases','total_deaths','total_recoveries']
counter=0
for temp in data:
    if  temp['longitude']:
        channels_list.append([temp['country'],temp['longitude'],temp['latitude'],temp['confirmed'],temp['active'],temp['deaths'],temp['recovered']])
        counter+=1
    i+=1
dataset=pd.DataFrame(channels_list,columns=channels)
dataset.to_csv('masonite/storage/public/database/database.csv',index=False)

print('congrats you have fetched :'+str(counter))