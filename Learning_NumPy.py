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

        print("This is the shape of the 2D array ", end ="")
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




