from Cimpl import show,copy,load_image,save_as,Image,choose_file
from T30_image_filters import two_tone,three_tone,extreme_contrast,sepia,posterize,detect_edges,detect_edges_better,flip_vertical,flip_horizontal

print("Hello User and welcome to Microsoft 2.0 photo editing software. There are twelve different options listed below. Load an image before you attempt to use the filters")

def menu_of_commands()->str:
    """menu of commands"""
    print("L)oad image S)ave-as \n2)-tone 3)-tone X)treme contrast T)int sepia P)osterize \nE)dge detect I)mproved edge detect V)ertical flip H)orizontal flip \nQ)uit")
    print("")
    return (input(": ")).capitalize()

def image_processing(image:Image, function:str)->Image:
    if function == "2":
        image = two_tone(image,"yellow","cyan")
    if function == "3":
        image = three_tone(image,"yellow","magenta","cyan")
    if function == "E":
        threshold = int(input("Threshold value: "))
        image = detect_edges(image,threshold)
    if function == "I":
        threshold = int(input("Threshold value: "))
        image = detect_edges_better(image,threshold)
    if function == "X":
        image = extreme_contrast(image)
    if function == "T":
        image = sepia(image)
    if function == "P":
        image = posterize(image)
    if function == "V":
        image = flip_vertical(image)    
    if function == "H":
        image = flip_horizontal(image)    
    return image

def interactive_ui()->None:
    command = ""
    image = ""
    command_list = ["L","S","2","3","X","T","P","E","I","V","H","Q"]
    filter_list = ["2","3","X","T","P","E","I","V","H"]
    
    while command != "Q":
        command = menu_of_commands()
        if command not in command_list:
            print("No such command")        
        elif command == "L":
            image = load_image(choose_file())
            show(image)
        elif command == "S":
            save_as(image,input("Please input the name you want to save it as with the extension (.jpg or .png): "))
        elif command in filter_list:
            if image == "":
                print("No image loaded")
            else:
                image = image_processing(image,command)
                show(image)
        elif command == "Q":
            return

interactive_ui()