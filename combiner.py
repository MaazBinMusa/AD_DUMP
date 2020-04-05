import os
import json

final_json = {}
for i in os.listdir('jsons'):
	final_json[i] = {}
	data = {}
	with open('jsons/{}'.format(i),'r') as file:
		data = json.load(file)
	final_json[i] = data

with open('final_json.json','w') as file:
	json.dump(final_json,file)