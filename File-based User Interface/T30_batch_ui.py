import string
from Cimpl import show,copy,load_image,save_as,Image
from typing import List
from T30_image_filters import two_tone,three_tone,extreme_contrast,sepia,posterize,detect_edges,detect_edges_better,flip_vertical,flip_horizontal

#Global Variables
word_list = []
line_list = []

def build_word_list(filename:str)->None:
    infile = open(filename, "r")
    for line in infile:
        word_list = line.split() 
        image = copy(load_image(word_list[0]))
        
        word_length = len(word_list)
        for i in range(2, word_length):
            user_input = word_list[i]
            
            #2 tone filter set to yellow and cyan
            if user_input == "2":                       
                image = two_tone(image, "yellow", "cyan")
                show(image)
                
            #3 tone filter set to yellow, magenta and cyan       
            elif user_input == "3":                       
                image = three_tone(image, "yellow", "magenta", "cyan")
                show(image)
                
            #extreme contrast        
            elif user_input == "X":                      
                image = extreme_contrast(image)
                show(image)
                
            #Sepia tinting        
            elif user_input == "T":                      
                image = sepia(image)
                show(image)    
            
            #Posterizing       
            elif user_input == "P":                        
                image = posterize(image)
                show(image)
                
            #Edge detection with threshold set to 10       
            elif user_input == "E":                        
                image = detect_edges(image, 10)
                show(image)
                
            #Improved Edge detection with threshold set to 10
            elif user_input == "I":                        
                image = detect_edges_better(image, 10)
                show(image)
                
            #Vertical Flip        
            elif user_input == "V":                  
                image = flip_vertical(image)
                show(image)
                
            #Horizontal Flip        
            elif user_input == "H":                        
                image = flip_horizontal(image)
                show(image)
        
        #Saving the image(s)         
        save_as(image, word_list[1])
    infile.close()
    
    return None
        
    
# main
batch_name = input("Please input the batch file name with the extension(.txt): ")
build_word_list(batch_name)