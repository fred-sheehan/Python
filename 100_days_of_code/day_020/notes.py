# slicing
# [start:stop:step]
# start: starting index of the slice
# stop: ending index of the slice
# step: the amount by which the index increases

piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# slice from index 2 to index 5
print(piano_keys[2:6])
# ['c', 'd', 'e', 'f']

# slice from index to end of the list
print(piano_keys[2:])
# ['c', 'd', 'e', 'f', 'g']

# slice from start to index 4
print(piano_keys[:5])
# ['a', 'b', 'c', 'd', 'e']

# slice from index to index specified by step.
# here we are slicing entire list with step 2
print(piano_keys[::2])
# ['a', 'c', 'e', 'g']

# slice from index 1 to end of the list with step 2
print(piano_keys[1::2])
# ['b', 'd', 'f']

# slice from index 1 to index 6 with step 2
print(piano_keys[1:7:2])
# ['b', 'd', 'f']
