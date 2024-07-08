# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:50:44 2024

@author: cseweb
"""

def string_to_dict(input_string):
    # Remove outer curly braces if present
    if input_string.startswith("{") and input_string.endswith("}"):
        input_string = input_string[1:-1]
    
    # Split by comma to get key-value pairs
    pairs = input_string.split(",")
    
    # Create dictionary from key-value pairs
    result_dict = {}
    for pair in pairs:
        # Split each pair into key and value
        key_value = pair.split(":")
        if len(key_value) == 2:
            key = key_value[0].strip().strip("'\"")
            value = key_value[1].strip().strip("'\"")
            result_dict[key] = value
        else:
            raise ValueError("Invalid format for key-value pair.")
    
    return result_dict

# Example usage:
input_string = input("enter the string")
result_dict = string_to_dict(input_string)
print(result_dict)
