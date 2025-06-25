'''
5 bottles of beer on the wall, 5 bottles of beer.
Take one down, pass it around, 4 bottles of beer on the wall.

4 bottles of beer on the wall, 4 bottles of beer.
Take one down, pass it around, 3 bottles of beer on the wall.

3 bottles of beer on the wall, 3 bottles of beer.
Take one down, pass it around, 2 bottles of beer on the wall.

2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take it down, pass it around, no more bottles of beer on the wall!

'''



def get_starting_number():

    while True:
        start_bottles_num = input("How many bottles of beer on the wall?")

        if start_bottles_num.isnumeric():
            start_bottles_num = int(start_bottles_num)

            if start_bottles_num >= 1:
                return start_bottles_num
            


def sing(starting_number):


    keep_looping = True
    

    while keep_looping:

        if starting_number > 2:
            print(f"{starting_number} bottles of beer on the wall, {starting_number} bottles of beer. Take one down, pass it around, {starting_number - 1} bottles of beer on the wall.")
            starting_number = starting_number - 1
            
        if starting_number == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer. Take one down, pass it around, 1 bottle of beer on the wall!")
            starting_number = starting_number - 1
            
        elif starting_number == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer. Take it down, pass it around, no more bottles of beer on the wall!")
            starting_number = starting_number - 1
            
        elif starting_number == 0:   
            keep_looping = False
            




