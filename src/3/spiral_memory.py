
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


def stress_test(number):
    '''
    finding index of corners
    '''
    corners = [0,0,0,1]
    fourth_corner = 1
    for square in range(1,10):
        for i in range(len(corners)):
            corners[i] = corners[i-1]+square*2
        print(corners)
        

#for number in [1,12,23,1024,368078]:
#    square_number, corners, distance = taxicab_geometry(number)
#    print('Number: {}\nSquare number: {}\nCorners: {}\nDistance: {}\n'\
#            .format(number,square_number, corners, distance))

stress_test(4)


