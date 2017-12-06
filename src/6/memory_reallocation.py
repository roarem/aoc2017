from itertools import cycle

with open('in_test_1.data','r') as banks:
    blocks = [int(block) for block in banks.read().strip()]
    number_of_banks = len(blocks)
    old_permutations = []
    block_string = ''.join(str(i) for i in blocks)
    while 1:
        temp_blocks = cycle(blocks)
        largest_block = max(blocks)
        max_index = blocks.index(largest_block)
        blocks[max_index] = 0
        print(blocks)
        print(max_index,largest_block)
        for _ in range(largest_block):
            #index = (i+largest_block)%number_of_banks
            #print(index)
            blocks[index] = 1
        block_string = ''.join(str(i) for i in blocks)
        print(blocks)
        if block_string in old_permutations:
            print(block_string)
            break
        else:
            old_permutations.append(block_string)
    print(len(old_permutations),old_permutations)


    
