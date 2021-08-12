import pandas as pd 

dataset = pd.read_csv("resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv")
dataset['year'] = dataset.apply(lambda row: row.month[:4],axis=1)

sales = dataset.groupby(by = 'town').count()
sales = sales.filter(like = 'month')
sales = sales.rename(columns = {'month':'no. of sales'})
sales = sales.sort_values(by = ['no. of sales'], ascending = False)

dataset.loc[dataset['street_name'] == 'BAIN ST', 'town'] = 'DOWNTOWN CORE'
dataset.loc[dataset['street_name'] == 'BUFFALO RD', 'town'] = 'ROCHOR'
dataset.loc[dataset['street_name'] == 'CANTONMENT RD', 'town'] = 'OUTRAM'
dataset.loc[dataset['street_name'] == 'CHANDER RD', 'town'] = 'ROCHOR'
dataset.loc[dataset['street_name'] == 'CHIN SWEE RD', 'town'] = 'OUTRAM'
dataset.loc[dataset['street_name'] == 'JLN BERSEH', 'town'] = 'ROCHOR'
dataset.loc[dataset['street_name'] == 'JLN KUKOH', 'town'] = 'ROCHOR'
dataset.loc[dataset['street_name'] == 'KELANTAN RD', 'town'] = 'ROCHOR'
dataset.loc[dataset['street_name'] == 'KLANG LANE', 'town'] = 'ROCHOR'
dataset.loc[dataset['street_name'] == 'KRETA AYER RD', 'town'] = 'OUTRAM'
dataset.loc[dataset['street_name'] == 'NEW MKT RD', 'town'] = 'OUTRAM'
dataset.loc[dataset['street_name'] == 'QUEEN ST', 'town'] = 'ROCHOR'
dataset.loc[dataset['street_name'] == 'ROWELL RD', 'town'] = 'ROCHOR'
dataset.loc[dataset['street_name'] == 'SAGO LANE', 'town'] = 'OUTRAM'
dataset.loc[dataset['street_name'] == 'SELEGIE RD', 'town'] = 'ROCHOR'
dataset.loc[dataset['street_name'] == 'SMITH ST', 'town'] = 'OUTRAM'
dataset.loc[dataset['street_name'] == 'TG PAGAR PLAZA', 'town'] = 'OUTRAM'
dataset.loc[dataset['street_name'] == 'UPP CROSS ST', 'town'] = 'OUTRAM'
dataset.loc[dataset['street_name'] == 'VEERASAMY RD', 'town'] = 'ROCHOR'
dataset.loc[dataset['street_name'] == 'WATERLOO ST', 'town'] = 'ROCHOR'

dataset['town name'] = dataset['town']

dataset.to_csv('Updated Data.csv',index=False)
dataset.to_csv('Resales by Town.csv', index = False)
