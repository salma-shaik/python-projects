import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@fakemail.com", "john.smith@workemail.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555- 5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

# load the json string into python obj
json_data = json.loads(people_string)

print(json_data)
print(type(json_data['people']))

for person in json_data['people']:
    print(person)
    print(person['name'])


# convert python json obj to json str
for person in json_data['people']:
    del person['phone']


json_str = json.dumps(json_data, indent=2, sort_keys=True)
print(json_str)