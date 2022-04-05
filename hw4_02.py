from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')

encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

text = content.split('><')

char_code = []
for i in text:
    if 'CharCode' in i:
        char_code.append(i)

cur_value = []
for i in text:
    if 'Value' in i:
        cur_value.append(i)

char_code = list(map(lambda x: x.replace('CharCode>', '').replace('</CharCode', ''), char_code))
cur_value = list(map(lambda x: x.replace('Value>', '').replace(',', '.').replace('</Value', ''), cur_value))

currency = dict(zip(char_code, cur_value))


def exchange_ratio(num):
    """Func returns value from dict {words}"""
    num = num.upper()
    if num in currency.keys():
        return float(currency.get(num))


exchange = input('Pls enter code of the currency you want to see exchange ratio for or \'q\' to quite: ')
while exchange != 'q':
    print(exchange_ratio(exchange))
    exchange = input('Pls enter code of the currency you want to see exchange ratio for or \'q\' to quite: ')
