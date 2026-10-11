import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/pogoda/ru/lipetsk?lat=52.60882&lon=39.59922'
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
pars = soup.find('span', class_='AppFactTemperature_value__2qhsG')
if pars is not None:
    text = pars.get_text(strip=True)
    temperature = f'\nСейчас в Липецке: {text} градусов по Цельсию.\n\nВот прогноз ⛅ на 10 дней:'
    print(temperature)
else:
    print('Температура не найдена')

days_names = soup.find_all('span', class_='AppShortForecastDay_title__2NpIg')
if not days_names:
    print('Дни недели не найдены')
else:
    text1_names = [tag.get_text(strip=True).upper() for tag in days_names]
days_names_first_10 = text1_names[:10]
# print(days_names_first_10)

days_numb = soup.find_all('span', class_='AppShortForecastDay_subtitle__hv_2V')
if not days_numb:
    print('Числа не найдены')
else:
    text1_numb = [tag.get_text(strip=True).upper() for tag in days_numb]
    days_numb_first_10 = text1_numb[:10]
# print(days_numb_first_10)

res_days = []
for name, numb in zip(days_names_first_10, days_numb_first_10):
    res_days.append(name + ' ' + numb)
# print(res_days)

temp_max = soup.find_all('span', class_='AppShortForecastDay_temperature__DV3oM')
if not temp_max:
    print('Макс темпа не найдена (возможно, класс изменился)')
else:
    text1_temp_max = [tag.get_text(strip=True).upper() for tag in temp_max]
    temp_max_first_10 = text1_temp_max[:20]
# print(temp_max_first_10)

temp_max1 = temp_max_first_10[::2]
temp_min1 = temp_max_first_10[1::2]
# print(f'{temp_max1}\n{temp_min1}')

all_results = {}
for r,tmin,tmax in zip (res_days, temp_min1, temp_max1):
    all_results[r] = {'От':tmin,'До':tmax}
# print(all_results)

for key, value in all_results.items():
    print(key)
    for sub_key, sub_value in value.items():
        print(f"  {sub_key}: {sub_value}")
    print()


























