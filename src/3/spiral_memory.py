
def find_square_number(number):
    spiral_end = 1
    square_number = 0
    corners = [0,0,0,0]
    while spiral_end < number:
        print(spiral_end,square_number)
        print(corners,'\n')
        square_number += 1
        spiral_end += square_number*8
        corners = [6*square_number,4*square_number,2*square_number,0]
        corners[:] = [spiral_end-corner for corner in corners]

    return square_number,spiral_end,corners

print(find_square_number())

