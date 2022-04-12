import numpy as np
import time
import random


def timing_python_vs_numpy():
    n = 1000000

    # two lists of 1,000,000 random digits.
    a = [random.random() for i in range(n)]
    b = [random.random() for i in range(n)]

    # We use list comprehenstion to multiply the two list together and store in C.
    s = time.time()
    c = [a[i] * b[i] for i in range(n)]
    print("Comprehension:", time.time() - s)

    # We use a normal for loop to multiply the two list together and store in C.
    s = time.time()
    c = []
    for i in range(n):
        c.append(a[i] * b[i])
    print("for loop:", time.time() - s)

    # We create C first then store the multiplication of the two list.
    s = time.time()
    c = [0] * n
    for i in range(n):
        c[i] = a[i] * b[i]
    print("Existing List", time.time() - s)

    # We use numPy multiply an array of the two list and store them in a new array.
    x = np.array(a)
    y = np.array(b)
    s = time.time()
    c = x * y  # there is no specific looping but numpy knows to do it.
    print("Numpy Time:", time.time() - s)


def basic_arrays():
    num = input("How many dimensions do you want the array to be?:\n")
    print(num)
    if num == str(1):

        a = np.array([1, 2, 3, 4])
        print("the array is ", end="")
        print(a)

        # .size give you the number of elements
        print("The size of the array is " + str(a.size))

        # .shape gives you the shape of the array, in this case its 1 dimensional
        print("the shape of the array is " + str(a.shape))

        # .dtype gives you the data type of the element it contains
        print("The data type of the array is " + str(a.dtype))

        # Use this if you would like to specify the data type
        b = np.array([1, 2, 3, 4], dtype="uint8")
        print("the array is ", end="")
        print(b)
        print("The data type of the array is " + str(b.dtype))

    elif num == str(2):
        # This is how we make 2d dimensional array
        c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print("the 2D array is ")
        print(c)

        print("This is the shape of the 2D array ", end="")
        print(c.shape)

        print("This is the size of the 2D array ", end="")
        print(c.size)

    elif num == str(3):

        # This is how we make 3d dimensional array
        d = np.array([[[1, 11, 111], [2, 22, 222]], [[3, 33, 333], [4, 44, 444]]])
        print("the 3d array is ")
        print(d)

        print("This is the shape of the 3D array ", end="")
        print(d.shape)

        print("This is the size of the 3D array ", end="")
        print(d.size)

    else:
        print("In order to make test arrays you can fill them with 1's or 0's")
        # the parameter of the .zero is the size you want to make the array
        # the same can be done with .ones to fill with ones.
        e = np.zeros((2, 3, 4))

        print("the Zero filled array is ")
        print(e)

        print("This is the shape of the zero filled array ", end="")
        print(e.shape)

        print("This is the size of the Zero filled array ", end="")
        print(e.size)


def accessing_elements_in_an_array():
    # creates a 2d array that has 3 vectors of 4 elements each
    b = np.zeros((3, 4), dtype='uint8')
    print(b)

    # You can change single cells in a matrix by telling which row and column
    b[0, 1] = 1
    b[1, 0] = 2
    print("Array b with cells [0,1] and [1,0] changed")
    print(b)

    # You can also print out entire vectors inside the matrix
    print("This is the second vector in the array")
    print(b[1])


def slicing_an_array():
    # You can create arrays filled up to but not including a number like this, in this case 0 - 19
    a = np.arange(20)
    print("An array filled 0-19")
    print(a)

    # You can choose to print specific number range that will include the first number but exclude the last number
    print("The following is segmented parts of array A")
    print(a[1:4])
    print(a[5:18])

    # You can also choose a specific range and the amount of steps between each number
    print("the following is the same segmented parts of array A but with different steps between each number")
    print(a[1:4:2])
    print(a[5:18:3])

    # If you skip the starting number you will start with the first number in the array
    # If you skip the ending number you will end at the last number in the array
    print("The following is sliced arrays with missing starting and then ending ranges")
    print(a[:4])
    print(a[16:])

    # In python, you can easily print arrays backwards with the use of negative numbers
    print("You can easily print the last index in the array with -1")
    print(a[-1])

    # To print the array backwards you need you skip the starting and ending of the array to print the entire array
    # but the step is -1
    print("The following is the array printed backwards")
    print(a[::-1])

    # You can even reshape the entire array into different shaped matrices
    print("Here is the array before its reshaped")
    b = np.arange(40)
    print(b)
    # The reshape method must be multiplied together to get the size of the array
    # i.e 4 * 10 = 40
    print("Here is the array after its reshaped")
    print(b.reshape((4, 10)))
    print("Since its 40 elements you can do 4 by 10, since 4 * 10 = 40.")
    print("You could also do in orientation as long as it multiplies to the number of elements")
