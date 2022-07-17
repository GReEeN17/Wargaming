#Допустим есть фиксроаванный список из 17 элементов


class Ex_1:
    def __init__(self):
        self.mas = [0] * 17

    def added(self, new_elem):
        self.mas = self.mas[1:] + [new_elem]

class Ex_2:
    def __init__(self):
        self.mas = [0] * 17

    def added(self, new_elem):
        self.mas.append(new_elem)
        self.mas.pop(0)

'''
Плюсы первой реализации: Используется метода среза списка, аналогичный методу среза строки, что делает этот метод более 
быстро работающим.
Минусы первой реализации: Необхожимо понимать, как правильно работать со срезом строки и как правильно добавлять новый 
элемент в массив, не используя при этом метод append
Плюсы второй реализации: Понятен для человека не знакомого с программированием, поскольку идёт последовательное 
добавление элемента в список, а затем удаление последнего
Минусы второй реализации: Использование метода pop замедляет работу второй реализации, из-за чего она работает дольше 
по сравнению с первой
'''
