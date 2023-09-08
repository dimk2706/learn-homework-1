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
def summ(list1):
    sum1 = 0
    for i in list1:
        sum1 = sum1 + i
    return sum1

def mean(list1):
    sum = 0
    for i in list1:
        sum = sum + i
    mean1 = sum/len(list1)
    return mean1

def main():
    Phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    sum_main = 0
    mean_main = 0
    for one_product in Phones:
        product_sum = summ(one_product['items_sold'])
        print(f"Суммарное количество продаж для {one_product['product']}: {product_sum}")
        sum_main = sum_main + product_sum
    for one_product in Phones:
        product_mean = mean(one_product['items_sold'])
        product_mean1 = int(product_mean)
        print(f"Среднее количество продаж для {one_product['product']}: {product_mean1}")
        mean_main = mean_main + product_mean
    mean_main = int(mean_main/len(Phones))
    print(f"Суммарное количество продаж для всех товаров: {sum_main}")
    print(f"Среднее количество продаж для всех товаров: {mean_main}")

    
    
if __name__ == "__main__":
    main()
