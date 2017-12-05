def jump_around(part,filename):
    condition = float('inf') if part==1 else 2
    jump_dict = {0:1,1:-1}
    with open(filename,'r') as in_data:
        jump_offsets = [int(jump) for jump in in_data.readlines()]
        i = 0
        counter = 0
        while i<len(jump_offsets):
            temp_offset = jump_offsets[i]
            jump_offsets[i] += jump_dict[temp_offset>condition]
            i += temp_offset
            counter += 1
        print(counter)

#jump_around(part=1,filename='in_test.data')
#jump_around(part=1,filename='in.data')
#jump_around(part=2,filename='in_test.data')
jump_around(part=2,filename='in.data')
