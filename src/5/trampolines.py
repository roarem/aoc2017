
#with open('in_test_1.data','r') as in_data:
#    jump_offsets = [int(jump) for jump in in_data.readlines()]
#    print(jump_offsets)
#    i = 0
#    counter = 0
#    while i<len(jump_offsets):
#        temp_offset = jump_offsets[i]
#        jump_offsets[i] += 1
#        i += temp_offset
#        counter += 1
#    print(counter)
with open('in_2.data','r') as in_data:
    jump_offsets = [int(jump) for jump in in_data.readlines()]
    print(jump_offsets)
    i = 0
    counter = 0
    while i<len(jump_offsets):
        temp_offset = jump_offsets[i]
        if temp_offset>2:
            jump_offsets[i] -= 1
        else:
            jump_offsets[i] += 1
        i += temp_offset
        counter += 1
    print(counter)
