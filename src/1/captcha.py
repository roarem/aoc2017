a = [1,1,1,1]
a = [1,2,3,4]
a = [9,1,2,1,2,1,2,9]
a = [1,1,2,2]
captcha = 0
multiples = {} if a[0]!=a[-1] else {a[0]:1}
for v1,v2 in zip(a[:-1],a[1:]):
    print(v1,v2)
    if v1==v2:
        try:
            multiples[v1] += 1
        except:
            multiples[v1] = 1
for key,value in multiples.items():
    captcha += key*value
print(multiples)
print(captcha)
    
