def test_cases():
    sequences = [[1,2,1,2],[1,2,2,1],[1,2,3,4,2,5],[1,2,3,1,2,3],[1,2,1,3,1,4,1,5]]
    totals = [6,0,4,12,4]
    for seq,tot in zip(sequences,totals):
        a1,a2 = get_lists(seq)
        mult, capt = count(a1,a2)
        print('Sequence: ',seq)
        print('a1: ',a1)
        print('a2: ',a2)
        print('Multiplicites: ',mult)
        print('Solution: ',tot,' Answer: ',capt)

        if capt==tot:
            print('success\n')
        else:
            print('YOU FUCKED UP!\n')

    
def get_lists(a):
    size = len(a)
    size_2 = size//2
    a2 = a[size_2:] + a[:size_2]
    return a, a2

def real_case():
    with open('in_2.data','r') as in_data:
        a = [int(i) for i in in_data.read().strip()]
    return get_lists(a)

def count(a1,a2):
    multiples = {} if a1[0]!=a2[0] else {a1[0]:1}
    for v1,v2 in zip(a1[1:],a2[1:]):
        if v1==v2:
            try:
                multiples[v1] += 1
            except:
                multiples[v1] = 1
    
    captcha = 0
    for key,value in multiples.items():
        captcha += key*value
    return multiples, captcha
    
#test_cases()
a1,a2 = real_case()
mult, cap = count(a1,a2)
print(mult)
print(cap)
