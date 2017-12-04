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

def print_out(sq,j,elements):
    print('sq: {}, j: {}'.format(sq,j))
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
    corner_indicies = [3,7,11]
    b_corners = [i-1 for i in corner_indicies]
    a_corners = [i+1 for i in corner_indicies]
    for sq in range(2,5):
        number_of_elements = sq*8
        print(corner_indicies)
        print(b_corners)
        print(a_corners)
        print('First')
        ns = [print_out(sq,0,[os[-1],os[0]])]
        for j in range(1,number_of_elements):
            i = j//(sq*2)*2
            if j in b_corners:
                print('Before corner')
                ns.append(print_out(sq,j,[ns[-1], os[j-i-2], os[j-i-1]]))
            elif j in corner_indicies:
                print('Corner')
                ns.append(print_out(sq,j,[ns[-1], os[j-i-2]]))
            elif j in a_corners:
                print('After corner')
                ns.append(print_out(sq,j,[ns[-1], ns[-2], os[j-i], os[j-i-1]]))
            elif j+2==number_of_elements:
                print('Before last corner')
                ns.append(print_out(sq,j,[ns[-1],ns[0],os[-1],os[-2]]))
            elif j+1==number_of_elements:
                print('Last corner')
                ns.append(print_out(sq,j,[ns[-1],ns[0],os[-1]]))
            else:
                print('Middle')
                ns.append(print_out(sq,j,[ns[-1], os[j-i-2], os[j-i-1], os[j-i]]))
            if ns[-1]>number:
                print('Found it!')
                print(ns[-1])
                break
        os = ns
        for j in range(len(corner_indicies)):
            corner_indicies[j] = corner_indicies[j]+2*(j+1)
        b_corners = [i-1 for i in corner_indicies]
        a_corners = [i+1 for i in corner_indicies]
        print(corner_indicies)
             
        

#for number in [1,12,23,1024,368078]:
#    square_number, corners, distance = taxicab_geometry(number)
#    print('Number: {}\nSquare number: {}\nCorners: {}\nDistance: {}\n'\
#            .format(number,square_number, corners, distance))

stress_test(368078)


