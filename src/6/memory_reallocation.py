with open('in.data','r') as banks:
    blocks = [int(block) for block in banks.read().strip().split()]
    print(blocks)
    number_of_banks = len(blocks)
    block_string = ''.join(str(i) for i in blocks)
    old_permutations = [block_string]
    loop_number = 1
    loop_counter = 0
    while 1:
        largest_block = max(blocks)
        max_index = blocks.index(largest_block)
        blocks[max_index] = 0
        blocks = blocks[max_index:]+blocks[:max_index]
        for i in range(1,largest_block+1):
            blocks[i%number_of_banks] += 1

        blocks = blocks[number_of_banks-max_index:]\
               + blocks[:number_of_banks-max_index]
        block_string = ''.join(str(i) for i in blocks)
        if block_string in old_permutations and loop_number==1:
            repeated_block_string = block_string
            loop_number = 2
            print('Number of permutations until repeating: {}'\
                    .format(len(old_permutations)))
        elif loop_number == 2:
            loop_counter += 1
            if block_string==repeated_block_string:
                print('Number of permutations before repeating again {}'\
                        .format(loop_counter))
                break
            
        else:
            old_permutations.append(block_string)
