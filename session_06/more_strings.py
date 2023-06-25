#!/usr/bin/env python3

# Indexing strings
strings_to_index = "Index Arrays"

first_A = strings_to_index[6]
print(first_A)

first_word = strings_to_index[0:5]
print(first_word)

last_word = strings_to_index [6:12]
print(last_word)

last_index = strings_to_index [-1]
print(last_index)

#Strides 
every_2nd_value = strings_to_index [::2]
print(every_2nd_value)

complicated_stride = strings_to_index[0:5:2]
print(complicated_stride)

#length function 
strings_to_index = "Index Arrays"
print(len(strings_to_index))