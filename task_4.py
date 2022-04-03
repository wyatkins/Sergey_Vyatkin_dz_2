def convert_name_extract(list_in: list) -> list:
    list_in = ['инженер-конструктор Игорь',
               'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАй',
               'директор аэлита']


    for items in list_in:
        convert_name = items.split()[-1].capitalize()
        list_out = f'Привет, {convert_name}'

    return list_out

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)