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

print(captcha_1('in_test_1.data'))
print(captcha_1('in_1.data'))
