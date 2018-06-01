import json

with open('states.json') as jf:
    old_states_json = json.load(jf)

for state in old_states_json['states']:
    # print(state['name'], state['abbreviation'])
    del state['abbreviation']

with open('new_states_json.json', 'w') as jwf:
    json.dump(old_states_json, jwf, indent=2)
