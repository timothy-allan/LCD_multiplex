#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:12:20 2020

@author: timallan
"""



from itertools import permutations 

listOne     =  [1, 0, 0, 0, 0, 0, 0, 0, 0]
listTwo     =  [1, 1, 0, 0, 0, 0, 0, 0, 0]
listThree   =  [1, 1, 1, 0, 0, 0, 0, 0, 0]
listFour    =  [1, 1, 1, 1, 0, 0, 0, 0, 0]
listFive    =  [1, 1, 1, 1, 1, 0, 0, 0, 0]
listSix     =  [1, 1, 1, 1, 1, 1, 0, 0, 0]
listSeven   =  [1, 1, 1, 1, 1, 1, 1, 0, 0]
listEight   =  [1, 1, 1, 1, 1, 1, 1, 1, 0]


all_lists = [listOne, listTwo, listThree, listFour, listFive, listSix, listSeven, listEight]


def generate_permutations(list_to_permute):
    

    
    permutation_list = list(permutations(list_to_permute))           # 'permutations' is a fuction of iterTools
    
    permutation_list = list(dict.fromkeys(permutation_list))         # use 'dict' trick to remove duplicates 

    print(len(permutation_list)) 
    
    # convert each configuration to *char_width* rows for Processing (eg - 3 rows, 4 columns)
    
    num_of_rows = 3

    split_permutation = []
    
    for config in permutation_list:

        temp_config = [ config [i:i + num_of_rows] for i in range(0, len(config), num_of_rows) ]
        
        
        split_permutation.append(temp_config)
        permutation_list = list(split_permutation)

    
    return(permutation_list)   





def generate_ALL_permutations(list_of_lists_to_permute):
    
    all_permutations = []
    
    for permutation_list in list_of_lists_to_permute:
        
        tempList = generate_permutations(permutation_list)
        all_permutations.append(tempList)


    return all_permutations
    



def convert_for_Processing(list_to_convert):
    
    # ************** Convert Python list to Processing Array *************** 
    
    permutation_string = str(list_to_convert)              # convert to string
    
   
    # replace [ ] with { } for Processing Array  
    permutation_string = permutation_string.replace( "[", "{")             
    permutation_string = permutation_string.replace( "]", "}")

    
    # replace ( ) with { } for Processing Array  
    permutation_string = permutation_string.replace( "(", "{")             
    permutation_string = permutation_string.replace( ")", "}")
    
    # add newLine(s) for readability
    permutation_string = permutation_string.replace( "}}," , "}},\n") 
    permutation_string = permutation_string.replace( "}}}," , "}}},\n\n") 
    
    return permutation_string
    


def write_to_file(permutation_string_to_write):

    
    # write to txt file:
    f = open ("_txt_files/write_to_file_pixelConfig__multiPermutations_9x9.txt", "w")
    f.write (permutation_string_to_write)
    f.close()
    
    # read from txt file to check:
    f = open ("_txt_files/write_to_file_pixelConfig__multiPermutations_9x9.txt", "r")
    #print(f.read())
    
    
    return permutation_string_to_write




#-------- MAIN --------#   


all_permutations = generate_ALL_permutations(all_lists)


all_permutations = convert_for_Processing(all_permutations)



#print(write_to_file(all_permutations))













  
