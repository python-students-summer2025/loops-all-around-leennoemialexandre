'''
FUNCTIONS
- `get_starting_number` - this function asks the user how many bottles of beer 
on the wall they want to start singing with, e.g. "How many bottles of beer on the wall?" 
The function asks this question as many times as necessary until the user enters a valid response, 
which is considered to be any integer 1 or greater. 


The function then returns the integer equivalent of the value the user entered. 
The code for this function can be the same for all three versions of the program, 
but must be copied into each file.


- `sing` - this function takes an argument specifying how many bottles of 
beer to start with, and then outputs the lyrics to the song, starting from that number of bottles.



'''


def get_starting_number():

    # when this is true....
    while True:

        #keep looping 
        start_bottles_num = input("How many bottles of beer on the wall?")

        if start_bottles_num.isnumeric():
            start_bottles_num = int(start_bottles_num)

            if start_bottles_num >= 1:
                return start_bottles_num



def sing(starting_number):
    '''
     `sing` - this function takes an ARGUMENT specifying how many bottles of 
beer to start with, and then outputs the lyrics to the song, starting from that number of bottles.

    2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall.

    '''

    # bottles = get_starting_number()
    

    for bottle in range(starting_number,0,-1):

        
        if bottle == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer. Take one down, pass it around, 1 bottle of beer on the wall!")
        
        elif bottle == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer. Take it down, pass it around, no more bottles of beer on the wall!")
        
        else:
            print(f"{bottle} bottles of beer on the wall, {bottle} bottles of beer. Take one down, pass it around, {bottle - 1} bottles of beer on the wall.")

        








    
    
    
   
        
            

 




            


   



