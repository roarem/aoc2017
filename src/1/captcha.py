#a = [1,1,1,1]
#a = [1,2,3,4]
#a = [9,1,2,1,2,1,2,9]
#a = [1,1,2,2]
with open('in.data','r') as in_data:
    a = [int(i) for i in in_data.read().strip()]

multiples = {} if a[0]!=a[-1] else {a[0]:1}
for v1,v2 in zip(a[:-1],a[1:]):
    if v1==v2:
        try:
            multiples[v1] += 1
        except:
            multiples[v1] = 1

captcha = 0
for key,value in multiples.items():
    captcha += key*value
print(multiples)
print(captcha)
    
