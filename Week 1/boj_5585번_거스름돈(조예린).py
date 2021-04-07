# -*- coding: utf-8 -*-
"""BOJ_5585번_거스름돈(조예린)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aKEBEQKSO7dEoEuF2WOra9PkVZ-cNhtQ
"""

moneyArray = [500, 100, 50, 10, 5, 1]
change = 1000 - int(input())
answer = 0
for money in moneyArray :
  if change >= money :
    answer += change//money
    change%=money

print(answer)