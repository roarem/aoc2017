def find_largest_register(filename):
    with open(filename,'r') as in_data:
        register = {}
        instructions = []
        inc_or_dec = {'inc':1,'dec':-1}
        for line in in_data.readlines():
            line = line.strip().split()
            if not line[0] in register:
                register[line[0]] = 0 
            instructions.append(line[:3]+[line[4]]+[" ".join(line[-2:])])

        highest_value = 0
        for ins in instructions:
            if eval(str(register[ins[3]]) + ins[4]):
                register[ins[0]] += int(ins[2])*inc_or_dec[ins[1]]
                highest_value = highest_value if highest_value>register[ins[0]]\
                                              else register[ins[0]]

    largest_register = max(register, key=lambda i: register[i])              
    return highest_value,largest_register, register[largest_register]

print(find_largest_register('in_test.data'))
print(find_largest_register('in.data'))
