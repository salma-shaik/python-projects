import json

from urllib.request import urlopen

# response = urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json")
yahoo_json_data = ''
try:
    with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
        source = response.read()

    # print(source)

    yahoo_json_data = json.loads(source)
    # print(yahoo_json_data)
except UnicodeDecodeError as e:
    print(e, 'Try Later')


if yahoo_json_data:
    yahoo_json_str = json.dumps(yahoo_json_data, indent=2)
    # print(yahoo_json_str)

    # with open('yahoo_fin_conv_data.json', 'w') as jfw:
    #     jfw.write(yahoo_json_str)


    # print(len(yahoo_json_data['list']['resources']))

    usd_rates = dict()

    for item in yahoo_json_data['list']['resources']:
        fields_dict = item['resource']['fields']
        if any(fields_dict):
            # print(fields_dict['name'])
            conv_name = item['resource']['fields']['name']
            conv_price = item['resource']['fields']['price']
            print(conv_name, conv_price)
            usd_rates[conv_name] = conv_price


    print(usd_rates['USD/INR'])

    print(50*float(usd_rates['USD/INR']))

    print(50*float(usd_rates['USD/EUR']))
else:
    print('No data obtained')