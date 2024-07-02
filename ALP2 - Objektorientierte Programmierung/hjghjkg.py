def charPicture(chooseChar, size):

    for y in range( 0, size):

        for x in range( 0, size):

           print( chooseChar( x, y, size), end='')

        print()

def rect (x, y, size):
    quarter = size / 4
    if x >= quarter * (-2) and y >= quarter * (-2):
        if ( y > x ):
            return '-'
        else:
            return '0'
    else:
        if y >= -(quarter / 4) and x >= -(quarter / 4):
            return '|'
        else:
            return '.'

charPicture(rect, 30)
