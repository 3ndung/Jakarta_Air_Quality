import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request as uri 
import ssl

context = ssl._create_unverified_context()


ur2 = 'https://website-api.airvisual.com/v1/places/map?bbox=106.3936123144531,-6.493973274280337,107.19286768554684,-5.979308421415107&units.temperature=celsius&units.distance=kilometer&AQI=US&language=en'
urly = uri.urlopen(ur2, context=context)
data = (urly.read())

data2 = str(data)
data2 = data2.split('[')[1].split(']')[0]
data2 = data2.replace('{name','').replace('name','').replace('id','').replace('aqi','').replace('type','').replace('coordinates','').replace('latitude','').replace('longitude','').replace('"','').replace(':','').replace('{','').replace('}}',':')

endung = []
data4 = []

data3 = data2.split(':,')
for i in range(len(data3)):
  #print(data3[i])
  endung.append(data3[i])
  data4.append(data3[i].split(','))
  
  
ADATA = pd.DataFrame(data4,columns=['Name','Id','AQI','Type','Latitude','Longitude'])
ADATA = ADATA[['Name','AQI','Latitude','Longitude']]
ADATA  

ADATA['Longitude'] = ADATA['Longitude'].replace(':','',regex=True)

ADATA['AQI'] = ADATA['AQI'].astype(int)
ADATA['Longitude'] = ADATA['Longitude'].astype(float)
ADATA['Latitude'] = ADATA['Latitude'].astype(float)


ADATA.loc[(ADATA.AQI >=0) & (ADATA.AQI <=50), 'Health Condition'] = 'Health'
ADATA.loc[(ADATA.AQI >=51) & (ADATA.AQI <=100), 'Health Condition'] = 'Moderate'
ADATA.loc[(ADATA.AQI >=101) & (ADATA.AQI <=150), 'Health Condition'] = 'Unhealthy for Sensitive Groups'
ADATA.loc[(ADATA.AQI >=151) & (ADATA.AQI <=200), 'Health Condition'] = 'Unhealthy'
ADATA.loc[(ADATA.AQI >=201) & (ADATA.AQI <=300), 'Health Condition'] = 'Very Unhealthy'
ADATA.loc[(ADATA.AQI >=301) & (ADATA.AQI >=500), 'Health Condition'] = 'Hazardous'



print(ADATA)

ADATA.to_csv('Air_Q.csv')

# or you can Print(ADATA)