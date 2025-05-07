#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num=10 
    while num >0:
        print(num)
        num = num-1
        print("Happy New Year!")
        


def square_integers(int_list):
    # code goes here!
    squared_number = []
    for number in int_list:
        squared_number.append(number*number)
    return squared_number
        

def fizzbuzz():
    # code goes here!

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
