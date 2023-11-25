import pycountry

if __name__ == "__main__":

    country_list = ["Russia", "UK"]
    # 遍历pycountry.countries中的所有国家
    for country in pycountry.countries:
        # 将国家名称和简写添加到列表中
        country_list.append(country.name)
        country_list.append(country.alpha_2)
        country_list.append(country.alpha_3)

    with open("other_file/country_names.txt", "w", encoding='utf-8') as file:
        file.writelines('\n'.join(country_list))
