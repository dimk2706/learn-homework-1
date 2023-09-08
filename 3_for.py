"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def get_average(list1):
    average = sum(list1)/len(list1)
    return average

def main():
    Phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    sum_main = 0
    average_main = 0
    sum_list = []
    average_list = []
    for one_product in Phones:
        product_sum = sum(one_product['items_sold'])
        sum_list.append(f"Суммарное количество продаж для {one_product['product']}: {product_sum}")
        sum_main = sum_main + product_sum
        product_average = get_average(one_product['items_sold'])
        product_average1 = int(product_average)
        average_list.append(f"Среднее количество продаж для {one_product['product']}: {product_average1}")
        average_main = average_main + product_average
    average_main = int(average_main/len(Phones))
    print("\n".join(sum_list))
    print("\n".join(average_list))
    print(f"Суммарное количество продаж для всех товаров: {sum_main}")
    print(f"Среднее количество продаж для всех товаров: {average_main}")

    
    
if __name__ == "__main__":
    main()
