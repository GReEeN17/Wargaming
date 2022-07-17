from random import randint


def sorter(mas):
    if len(mas) > 1:
        l, m, elem, num_of_elems = [], [], mas[0], 1
        for i in mas:
            if i > elem: m.append(i)
            elif i < elem: l.append(i)
            else: num_of_elems += 1
        l = sorter(l)
        m = sorter(m)
        mas = l + [elem] * num_of_elems + m
    return mas


mas = [randint(0, 100) for _ in range(100)]
print(mas)
print(sorter(mas))
'''
Я считаю данный метод самым бытсрым, поскольку по сравнению с обычными методами сортировки он переставляет элементы не 
проходя через весь массив, как это может случиться, а делая это на максимально малееьком расстоянии за счёт 
последовательного разбиения массива каждый раз на две части
'''