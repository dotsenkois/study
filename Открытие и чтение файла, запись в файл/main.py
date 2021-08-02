# Открытие файла
def load_cook_book(file_name):

    cook_book_dict = {}
    with open(file_name, 'r', encoding="utf-8") as cook_book:
        while True:
            data = cook_book.readline()
            try:
                number_of_ingredients = int(data)
            except:
                if '|' not in data:
                    name_of_the_dish = data.rstrip()
                    cook_book_dict.setdefault(name_of_the_dish, [])
                else:
                    ingredients = data
                    ingredient_name, quantity, measure = ingredients.split(' | ')
                    cook_book_dict[name_of_the_dish].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.rstrip()})
            if not data:
                    break

    return cook_book_dict

def get_shop_list_by_dishes(dishes, person_count):
    new_dict = {}
    cook_book = load_cook_book('CookBook.txt')
    for d in dishes:
        for i in range(len(cook_book[d])):
            temp_dict = {}
            temp_dict.setdefault('measure', cook_book[d][i]['measure'])
            temp_dict.setdefault('quantity', int(cook_book[d][i]['quantity']) * person_count)
            new_dict.setdefault(cook_book[d][i]['ingredient_name'], temp_dict)
    print(new_dict)



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 10)