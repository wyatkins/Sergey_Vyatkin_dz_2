def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    list_in = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    length_of_list: int = len(list_in)

    for _ in range(length_of_list):

        elem = list_in.pop(0)

        if elem.isdigit() and elem.isalnum():
            list_in.append(f'"{int(elem):02d}"')

        elif elem[0] == "+" and elem[1].isdigit():
            list_in.append(f'"+{int(elem):02d}"')

        else:
            list_in.append(elem)
    str_out = ' '.join(list_in)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)