#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:57:38 2020

@author: timallan
"""

import random
import time




def randNumList():

    pixel_config = []                        # list of possible pixel configurations
    startTime = time.time()
    
    num_of_rows = 4                          # How many rows in the chracter grid ?
    
    #while len(pixel_config) < 70:          
    for i in range (100000000):                
        

        total_num_pixels = 16                # number of pixels in array
        target_num_pixels_on = 6             # number of pixels in we want to be ON
        
        num_pixels_on = 0           

        random_configuration = []            # list contains a random confuration of pixels ON

        
        for pixels in range (total_num_pixels):     
            
            randNum = random.randrange (0, 2)
            random_configuration.append (randNum)
            
            num_pixels_on += randNum
            
        if num_pixels_on == target_num_pixels_on:               # have we found a configuration that equals target_num_pixels_on
            
            if random_configuration not in pixel_config:
                
                pixel_config.append(random_configuration)       # Add to list of pixel configurations
                #break
                
   
    

    
    # convert each configuration to *char_width* rows for Processing (eg - 3 rows, 4 columns)
    
    split_pixel_config = []
    for config in pixel_config:
    
        temp_pixel_config = [ config [i:i + num_of_rows] for i in range(0, len(config), num_of_rows) ]
        split_pixel_config.append(temp_pixel_config)
        pixel_config = split_pixel_config
        
        
    endTime = time.time()
    elapsedTme = endTime - startTime
    
    #print (pixel_config)

    print (len(pixel_config))
    
    print (elapsedTme)
    
    
    # ************** Convert Python list to String *************** 
#    
#    pixel_config_string = str(pixel_config)
#    
#   
#    # replace [ ] with { } for Processing Array  
#    processingArray = pixel_config_string.replace( "[", "{")             
#    processingArray = processingArray.replace( "]", "}")
#    
#    # add newLine for readability
#    processingArray = processingArray.replace( "}}, ", "}},\n") 
#    
#    
# 
#    # write to txt file:
#    f = open ("_txt_files/write_to_file_pixelConfig__6_OF_20.txt", "w")
#    f.write (processingArray)
#    f.close()
#    
#    # read from txt file to check:
#    f = open ("_txt_files/write_to_file_pixelConfig__6_OF_20.txt", "r")
#    #print(f.read())
    
    
    # *** return final values as a Processing Array formatted as String ****** #
    
    return pixel_config
 


randNumList()
    
