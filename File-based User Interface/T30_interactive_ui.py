from Cimpl import*
from T30_Image_Filters import *

print("Hello User and welcome to ShopPhoto photo editing software there are twelve different options listed below load an image before you attempt to use the filters")

print("L)oad image S)ave-as \n2)-tone 3)-tone X)treme contrast T)int sepia P)osterize \nE)dge detect I)mproved edge detect V)ertical flip H)orizontal flip \nQ)uit")

def interactive_Ui():
    """The function demonstrates a user interface program which neither takes in arguments nor returns them but acts as a skeleton for all the codes created
    """
    
    command_list = ["2","3","E","I","X","T","P","V","H","S"]
    while command != "Q":
            command = input("L)oad image S)ave-as \n2)-tone 3)-tone X)treme contrast" 
            " T)int sepia P)osterize \nE)dge detect I)mproved edge detect V)ertical flip" 
            " H)orizontal flip \nQ)uit \n \n: ")
            command = command.capitalize()
            if command == "Q":
                print("")
            elif command == "L": 
                image = load_image(choose_file())
                show(image)
            elif command not in command_list:
                print("No such command")            
            elif image == "":
                print("No image loaded")
            elif command == "S":
                save_as(image,"new_image.jpg")
            else:
                if command == "2":
                    image = two_tone(image,"yellow","cyan")
                if command == "3":
                    image = three_tone(image,"yellow","magenta","cyan")
                if command == "E":
                    threshold = int(input("Threshold?: "))
                    image = detect_edges(image,threshold)
                if command == "I":
                    threshold = int(input("Threshold?: "))
                    image = detect_edges_better(image,threshold)
                if command == "X":
                    image = extreme_contrast(image)
                if command == "T":
                    image = sepia(image)
                if command == "P":
                    image = posterize(image)
                if command == "V":
                    image = flip_vertical(image)    
                if command == "H":
                    image = flip_horizontal(image)
                show(image)
    user_interface()        