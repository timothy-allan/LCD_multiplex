#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:57:38 2020

@author: timallan
"""

import random
import time
import matplotlib.pyplot as plt

def factorial(total_num_pixels):
    
    fact = 1
    for i in range(1, total_num_pixels + 1): 
        fact = fact * i
              
    return(fact)



def combination(total_num_pixels, target_num_pixels_on):
    # find number of distinct configurations
    
    numerator = factorial(total_num_pixels)
    denominator = factorial(target_num_pixels_on) * factorial(total_num_pixels - target_num_pixels_on)
    num_possible_configs = int(numerator / denominator)

    return(num_possible_configs)
    
    

def generate_random_configs(total_num_pixels, target_num_pixels_on):

    pixel_config = []                        # list to contain possible pixel configurations
    
    num_distinct_configs = combination(total_num_pixels, target_num_pixels_on)
    print(num_distinct_configs)
    
    while len(pixel_config) < combination(total_num_pixels, target_num_pixels_on): 
        
        num_pixels_on = 0           

        random_configuration = []            # list contains a random confuration of pixels ON

        
        for pixels in range (total_num_pixels):     
            
            randNum = random.randrange (0, 2)
            random_configuration.append (randNum)
            
            num_pixels_on += randNum
            
        if num_pixels_on == target_num_pixels_on:               # have we found a configuration that equals target_num_pixels_on
            
            if random_configuration not in pixel_config:
                
                pixel_config.append(random_configuration)       # Add to list of pixel configurations
   
    print(pixel_config)
    return pixel_config


    


def split_configs(configs_to_split):
    
    # convert each configuration to *char_width* rows for Processing (eg - 4 rows, 3 columns)
    
    num_of_rows = 4  
    
    split_pixel_config = []
    for config in configs_to_split:
    
        split_pixel_config = [ config [i:i + num_of_rows] for i in range(0, len(config), num_of_rows) ]
        split_pixel_config.append(split_pixel_config)
        
    return (split_pixel_config)

    


def convert_list_to_ProcessingArray(configs_to_convert):
    
    # Convert Python list to String  
    pixel_config_string = str(configs_to_convert)
    
    # replace [ ] with { } for Processing Array  
    processingArray = pixel_config_string.replace( "[", "{")             
    processingArray = processingArray.replace( "]", "}")
    
    # add newLine for readability
    processingArray = processingArray.replace( "}}, ", "}},\n") 
   
    return (processingArray) 



def write_to_file(processingArray):
    
        # write to txt file:
    f = open ("_txt_files/write_to_file_pixelConfig__6_OF_20.txt", "w")
    f.write (processingArray)
    f.close()
    
    # read from txt file to check:
    f = open ("_txt_files/write_to_file_pixelConfig__6_OF_20.txt", "r")
    #print(f.read())
    
    
    
    


total_num_pixels = 6


list_of_configs = []

for num_pixels_ON in range (1, total_num_pixels):
    print("total num pixels =", total_num_pixels, "| pixels ON =", num_pixels_ON)

    list_of_configs.append(len(generate_random_configs(total_num_pixels, num_pixels_ON)))
    print(list_of_configs, end = "\n\n")




  
