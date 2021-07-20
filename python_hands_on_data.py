import pandas as pd
import json
data = pd.read_csv('python hands-on - dataset.csv')

obsolete = pd.DataFrame(['FALSE','TRUE','FALSE','TRUE','TRUE','TRUE','FALSE','FALSE','FALSE','TRUE'])

data.insert(4, 'obsolete', obsolete)

json_data = data.to_json(orient='columns')

print(json_data)

filename = 'new_json_data'

with open(filename, 'w') as fp:
    json.dump(json_data, fp)