import requests


# 获取国家相关的名词
def write_in_file(countries):
    english_names = []
    english_code2 = []
    english_code3 = []

    for country in countries:
        english_names.append(country['name'])
        english_code2.append(country['alpha2Code'])
        english_code3.append(country['alpha3Code'])
    with open('other_file/country_names.txt', 'w', encoding='utf-8') as f:
        for name in english_names:
            f.write(name + ',')
        for key2 in english_code2:
            f.write(key2 + ',')
        for key3 in english_code3:
            f.write(key3 + ',')


if __name__ == "__main__":
    response = requests.get('https://restcountries.com/v2/all')
    write_in_file(response.json())
