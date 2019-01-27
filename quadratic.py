from math import sqrt
from time import clock


def discriminant(delta):
    # Defines how many real roots the equation has based on delta
    # print('The discriminant is ' + str(delta) + ' therefore ')
    print('The discriminant is {}, therefore '.format(str(delta)), end='')

    if delta < 0:
        print('there are no real roots')
    elif delta == 0:
        print('there is exactly 1 real root')
    else:
        print('there are exactly 2 real roots.')


def PosOrNeg(a):
    # Determines whether the function is positive, negative, or neither
    if a < 0:
        print('The parabola opens down and has a maximum')
    elif a > 0:
        print('The parabola opens up and has a minimum')
    else:
        print('The function is a line, not a parabola!')


# --------------------------------------------------------------------------------
def Vertex(a, b, delta):
    # Determines maximum or minimum of Quadratic Equation
    x = round((-b / (2 * a)), 2)
    if x == -0.0:
        x = 0.0
    y = round((-delta / (4 * a)), 2)
    if y == -0.0:
        y = 0.0

    # print('The Vertex is ' + '(' + str(x) + ',' + str(y) + ')')
    print('The Vertex is ({},{})'.format(str(x), str(y)))


def VertexVF(h, k):
    print('The Vertex is ({},{})'.format(str(h), str(k)))


# -------------------------------------------------------------------------------

def HorizTrans(h):
    # Determines the Horizontal Translation, if any
    if h > 0:
        print('The Horizontal Translation is {} units right'.format(str(abs(h))))
    elif h < 0:
        print('The Horizontal Translation is {} units left'.format(str(abs(h))))
    else:
        print('There is no Horizontal Translation')


def VertTrans(k):
    # Determines the Vertical Translation, if any
    if k > 0:
        print('The Vertical Translation is {} units up'.format(str(abs(k))))
    elif k < 0:
        print('The Vertical Translation is {} units down'.format(str(abs(k))))
    else:
        print('There is no Vertical Translation')

def yInt(c):
    # Determines y intercept based on the given c paramter
    print('The Y-Intercept is {}'.format(str(c)))


def Roots(a, b, delta):
    # Calculates the roots (zeros) of the equation
    if delta < 0:
        print('Both roots are imaginary!\n')
    elif delta == 0:
        Root1 = round(((-b) + sqrt(delta)) / (2 * a), 2)
        print('The real root is: {}, the other is imaingary\n'.format(str(Root1)))
    else:
        Root1 = round(((-b) + sqrt(delta)) / (2 * a), 2)
        Root2 = round(((-b) - sqrt(delta)) / (2 * a), 2)
        # print('The roots are: ' + str(Root1)+ ' ' + 'and ' + str(Root2))
        print('The real roots are: {} and {}\n'.format(str(Root1), str(Root2)))

def RootsVF(a, h, k):
    #base = sqrt((-k) / a)
    if delta < 0:
        print('Both roots are imaginary!\n')
    elif delta == 0:
        Root1 = round(h + sqrt((-k) / a), 2)
        print('The real root is: {}, the other is imaingary\n'.format(str(Root1)))
    else:
        Root1 = round(h + sqrt((-k) / a), 2)
        Root2 = round(h - sqrt((-k) / a), 2)
        print('The real roots are: {} and {}\n'.format(str(Root1), str(Root2)))

    # if a((Root1 - h)**2) + k == True and a((Root2 - h)**2) + k == True:
    #     print('The Roots are {} snd {}'.format(str(Root1), str(Root2)))

def main():
    while True:

        try:
            FormofFunction = int(input("""What form is the Quadratic Equation in?
            1. Standard form (Y = Ax^2+Bx+C)
            2. Vertex form (Y = a(X-h)^2 +k)
            3. Conic form ()
            """))
        except Exception as e:
            print('Please input a number\n')
            main()

        if FormofFunction == 1: #(standard form)
            # Takes user input to store the a, b, and c parameters in a quadratic equation (standard form)
            try:
                a = float(input('What is the \'a\' parameter? '))
                b = float(input('What is the \'b\' parameter? '))
                c = float(input('What is the \'c\' parameter? '))
            except Exception as e:
                print('Please input a number\n')
                main()

            tick = clock()
            # Calculates the discriminant based on the given a, b, and c parameters
            global delta
            delta = round((b ** 2) - 4 * a * c, 2)

            #discriminant(delta)
            PosOrNeg(a)
            Vertex(a, b, delta)
            yInt(c)
            Roots(a, b, delta)
            tock = clock()
            print('The program took {} seconds \n'.format(tock - tick))
        elif FormofFunction == 2: #(Vertex form)
            # Takes user input to store the a, h, and k parameters in a quadratic equation (Vertex form)
            try:
                a = float(input('What is the \'a\' parameter? '))
                h = float(input('What is the \'h\' parameter? '))
                k = float(input('What is the \'k\' parameter? '))

            except Exception as e:
                print('Please input a number\n')
                main()

            delta = ((-k) / a)

            tick = clock()

            PosOrNeg(a)
            VertexVF(h, k)
            HorizTrans(h)
            VertTrans(k)
            RootsVF(a, h, k)

            tock = clock()
            print('The program took {} seconds \n'.format(tock - tick))

        elif FormofFunction == 3: #(Conic form)
            main()
        else:
            print('Please make a proper selection\n')


if __name__ == "__main__":
    main()
