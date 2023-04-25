# Домашнее задание №1

# Цикл for: Продажи товаров
# Дан список словарей с данными по колличеству проданных телефонов
#   [
#     {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
#     {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
#     {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
#   ]
# 1.Посчитать и вывести суммарное количество продаж для каждого товара
# 2.Посчитать и вывести среднее количество продаж для каждого товара
# 3.Посчитать и вывести суммарное количество продаж всех товаров
# 4.Посчитать и вывести среднее количество продаж всех товаров


sales = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]


def get_sales_of_one_product(number_of_sales):
    average_sales = 0
    for phones in number_of_sales:
        average_sales += phones
    return average_sales


for separate_sale in sales:
    average_sales = get_sales_of_one_product(separate_sale['items_sold'])
    print(f'Общее количество продаж {separate_sale["product"]}: {average_sales}')


def avg_product_sales(number_of_sales):
    average_sales = 0
    for phones in number_of_sales:
        average_sales += phones
    return round(average_sales / len(number_of_sales), 2)


average_sales_of_all_products = 0
for separate_sale in sales:
    average_sales = avg_product_sales(separate_sale['items_sold'])
    print(f'Средние количество продаж {separate_sale["product"]}: {average_sales}')
    average_sales_of_all_products += average_sales


def get_total_sales():
    total = 0
    for sale in sales:
        product_sales = get_sales_of_one_product(sale['items_sold'])
        total += product_sales
    return total


print(f'Общее колличество продаж всех товаров {get_total_sales()}')
avg = round(average_sales_of_all_products / len(sales), 2)
print(f'Средние количество продаж всех товаров: {avg}')
