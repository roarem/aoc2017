def captcha_1(filename):
    with open(filename,'r') as in_data:
        captcha = []
        for row in in_data.readlines():
            number_list = [int(i) for i in row.strip()]
            multiples = \
                {} if number_list[0]!=number_list[-1] else {number_list[0]:1}
            for v1,v2 in zip(number_list[:-1],number_list[1:]):
                if v1==v2:
                    try:
                        multiples[v1] += 1
                    except:
                        multiples[v1] = 1

            captcha.append([key*value for key,value in multiples.items()])
    return [sum(cap) for cap in captcha]

def captcha_2(filename):
    with open(filename,'r') as in_data:
        captcha = []
        for row in in_data.readlines():
            original = [int(i) for i in row.strip()]
            size_2 = len(original)//2
            mirrored = original[size_2:] + original[:size_2]

            multiples = {} if original[0]!=mirrored[0] \
                           else {original[0]:1}
            for o,m in zip(original[1:],mirrored[1:]):
                if o==m:
                    try:
                        multiples[o] += 1
                    except:
                        multiples[o] = 1
            
            captcha.append([key*value for key,value in multiples.items()])
    return [sum(cap) for cap in captcha]


print('{} {}'.format('Solution:',[3,4,0,9]))
print('{} {}'.format('Test run part 1:',captcha_1('in_test_1.data')))
print('{} {}\n'.format('Run part 1:',captcha_1('in_1.data')))
print('{} {}'.format('Solution:',[6,0,4,12,4]))
print('{} {}'.format('Test run part 2:',captcha_2('in_test_2.data')))
print('{} {}'.format('Run part 2:',captcha_2('in_2.data')))
