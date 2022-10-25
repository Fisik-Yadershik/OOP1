#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json


# Поле first — целое положительное число, номинал купюры; номинал может принимать
# значения 1, 2, 5, 10, 50, 100, 500, 1000, 5000. Поле second — целое положительное число,
# количество купюр данного достоинства. Реализовать метод summa() — вычисление
# денежной суммы.


class TaskOne:
   const_list = [1, 2, 5, 10, 50, 100, 500, 1000, 5000]
   def __init__(self):
      self.__summ = 0
      self.__first = 0
      self.__second = 0

   @property
   def first(self):
      return self.__first

   @property
   def second(self):
      return self.__second

   @property
   def summ(self):
      return self.__summ

   def read(self, prompt=None):
      self.__first = int(input('Введите номинал купюры: ')) if prompt is None else input(prompt)
      if int(self.__first) in TaskOne.const_list:
         self.__second = int(input('Введите количество купюр данного номинала: ')) if prompt is None else input(prompt)
      else:
         print("Такого номинала нет в списке")

   def display(self):
      print("Сумма: ", (self.__first*self.__second))


   #def make_summa(self):
      #return self.__summ(self.__first*self.__second)


if __name__ == '__main__':
   print("Список доступных номиналов: 1, 2, 5, 10, 50, 100, 500, 1000, 5000")
   while True:
      r2 = TaskOne()
      r2.read()
      r2.display()
