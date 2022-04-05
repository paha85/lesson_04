from requests import get, utils
import datetime as dt

response = get('http://www.cbr.ru/scripts/XML_daily.asp')

encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

text = content.split('><')

exchange_time = []
for i in text:
    if 'ValCurs Date' in i:
        exchange_time.append(i)
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
exchange_time = list(map(lambda x: x.replace('ValCurs Date="', '')
                         .replace('" name="Foreign Currency Market"', '').replace('.', ' '), exchange_time))

currency = dict(zip(char_code, cur_value))


def exchange_ratio(num):
    """Func returns value of the currency in Rubles"""
    num = num.upper()
    if num in currency.keys():
        print(dt.datetime.strptime(exchange_time[0], '%d %m %Y').date())
        return float(currency.get(num))
