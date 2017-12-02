def checksum_1(filename):
    with open(filename,'r') as in_1:
        checksum = 0
        for row in in_1.readlines():
            num_list = list(map(int, row.strip().split()))
            max_in_row = max(num_list)
            min_in_row = min(num_list)
            checksum += max_in_row-min_in_row
        print(checksum)

def checksum_2(filename):
    with open(filename,'r') as in_test:
        evenly_divisible_sum = 0
        for row in in_test.readlines():
            num_list = list(map(int,row.strip().split()))
            for num1 in num_list:
                for num2 in num_list:
                    if num1==num2:
                        continue
                    elif num1%num2==0:
                        evenly_divisible_sum += num1//num2
        print(evenly_divisible_sum)




#checksum_1('in_test_1.data')
#checksum_1('in_1.data')
#checksum_2('in_test_2.data')
checksum_2('in_2.data')

