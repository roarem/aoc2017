def test_case_1():
    with open('in_test.data','r') as in_test:
        checksum = 0
        for row in in_test.readlines():
            num_list = list(map(int, row.strip().split()))
            max_in_row = max(num_list)
            min_in_row = min(num_list)
            checksum += max_in_row-min_in_row
        print(checksum)


def checksum_1():
    with open('in_1.data','r') as in_1:
        checksum = 0
        for row in in_1.readlines():
            num_list = list(map(int, row.strip().split()))
            max_in_row = max(num_list)
            min_in_row = min(num_list)
            checksum += max_in_row-min_in_row
        print(checksum)




#test_case_1()
checksum_1()

