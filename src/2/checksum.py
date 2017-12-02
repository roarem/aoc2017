def checksum_1(filename):
    with open(filename,'r') as in_data:
        return sum([max(list(map(int,row.strip().split())))-\
                    min(list(map(int,row.strip().split()))) \
                    for row in in_data.readlines()])
                   
        #checksum = 0
        #for row in in_data.readlines():
        #    num_list = list(map(int, row.strip().split()))
        #    max_in_row = max(num_list)
        #    min_in_row = min(num_list)
        #    checksum += max_in_row-min_in_row
        #return checksum

def checksum_2(filename):
    with open(filename,'r') as in_data:
        divisibles = []
        for row in in_data.readlines():
            num_list = list(map(int,row.strip().split()))
            divisibles.append(\
                         sum([num1//num2 if (num1%num2==0 and num1!=num2) else 0\
                              for num1 in num_list for num2 in num_list]))
                              
        return sum(divisibles)
        #    for num1 in num_list:
        #        for num2 in num_list:
        #            if num1==num2:
        #                continue
        #            elif num1%num2==0:
        #                divisibles.append(num1//num2)
        #                break
        #return sum(divisibles)

print('{:12} {}'.format('Test part 1:',checksum_1('in_test_1.data')))
print('{:12} {}'.format('Run part 1:',checksum_1('in_1.data')))
print('{:12} {}'.format('Test part 2:',checksum_2('in_test_2.data')))
print('{:12} {}'.format('Run part 2:',checksum_2('in_2.data')))

