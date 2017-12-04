
def taxicab_geometry(number):
    square_number = 0
    corners = [0,0,0,1]
    while corners[-1] < number:
        square_number += 1
        corners[-1] += square_number*8
        corner_increase = [6*square_number,4*square_number,2*square_number,0]
        corners[:] = [corners[-1]-corner for corner in corner_increase]
     
    distance = min([square_number+abs((corner-square_number)-number) \
                    for corner in corners])
    return square_number,corners, distance


def print_out(sq,s,j,elements):
    print('sq: {}, s: {}, j: {}'.format(sq,s,j))
    temp_string = ''
    next_element = 0
    for el in elements[:-1]:
        next_element += el
        temp_string += '{} + '.format(el)
    next_element += elements[-1]
    print(temp_string+'{} = {}\n'.format(elements[-1],next_element))
    return next_element
        

def stress_test(number):
    os = [1,2,4,5,10,11,23,25]
    corners = [2,5,11,25]
    for sq in range(2,3):
        #print('sq: {}'.format(sq))
        #ns = [os[-1]+os[0]] 
        ns = [print_out(sq,1,0,[os[-1],os[0]])]
        for j in range(1,sq*2-2):
            ns.append(print_out(sq,1,j,[ns[-1], os[j-2], os[j-1], os[j]]))
            #next_element = ns[-1] + os[j-2] + os[j-1] + os[j]
            #print('Element: {}'.format(j))
            #print('{} + {} + {} + {} = {}\n'.format(\
            #               ns[-1], os[j-2], os[j-1], os[j], next_element))
            #ns.append(next_element)
        #next_element = ns[-1] + os[j-1] + os[j]
        #print('{} + {} + {} = {}\n'.format(\
        #                          ns[-1], os[j-1], os[j], next_element))
        #ns.append(next_element)
        ns.append(print_out(sq,1,j+1,[ns[-1], os[j-1], os[j]]))
        #next_element = ns[-1] + os[j]
        #print('{} + {} = {}\n'.format(\
        #                          ns[-1], os[j], next_element))
        #ns.append(next_element)
        ns.append(print_out(sq,1,j+1,[ns[-1], os[j]]))
        #next_element = ns[-1] + ns[-2] + os[j] + os[j+1]
        #print('{} + {} + {} + {} = {}\n'.format(\
        #                          ns[-1], ns[-2], os[j], os[j+1], next_element))
        #ns.append(next_element)
        ns.append(print_out(sq,1,j+1,[ns[-1], ns[-2], os[j], os[j+1]]))
        for s in range(2,4):
            #print('Side: {}'.format(side))
            for j in range(1,sq*2-1):
                next_element = ns[-1] + os[s*j] + os[j-1] + os[j]
                print('Element: {}'.format(j))
                print('{} + {} + {} + {} = {}\n'.format(\
                                          ns[-1], os[j-2], os[j-1], os[j],\
                                          next_element))
                ns.append(next_element)
            next_element = ns[-1] + os[side*(j-1)] + os[side*(j)]
            print('{} + {} + {} = {}\n'.format(\
                                      ns[-1], os[side*(j-1)], os[side*(j)],\
                                      next_element))
            ns.append(next_element)
            next_element = ns[-1] + os[side*(j)]
            print('{} + {} = {}\n'.format(\
                                      ns[-1], os[side*(j-1)], next_element))
            ns.append(next_element)
            print(ns)  
        os = ns
        #for j in range(len(corners)):
        #    corners[j] = corners[j-1]+square*2
        #print(corners)
             
        

#for number in [1,12,23,1024,368078]:
#    square_number, corners, distance = taxicab_geometry(number)
#    print('Number: {}\nSquare number: {}\nCorners: {}\nDistance: {}\n'\
#            .format(number,square_number, corners, distance))

stress_test(368078)


