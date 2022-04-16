import numpy as np
import time
import random
from PIL import Image
from sklearn.datasets import load_sample_images


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
    b = b.reshape((4, 10))
    print(b)
    print("Since its 40 elements you can do 4 by 10, since 4 * 10 = 40.")
    print("You could also do in orientation as long as it multiplies to the number of elements")

    # With different shaped matrices you can be explicit and tell it where to slice
    print("Here is a sliced matrix printed out")
    print(b[3:, 2:])
    print(b[0:1, :])
    # Not 100% sure what the comma means.


def the_ellipsis():
    c = np.arange(27).reshape((3, 3, 3))
    # 3 * 3 * 3 = 27 so reshape is possible
    print("a 3d array 0-26  reshaped into 3, 3, 3")
    print(c)

    a = np.ones((3, 3))
    print("a 2 by 2 matrix of ones")
    print(a)

    # since the C matrix is 3 matrixs of 3 by 3 stacked on top you can change one of the 3 by 3s like the following

    c[1, :, :] = a
    print(" setting the 2nd 3 by 3 into all ones")
    print(c)

    # we can use [0,...] to specify all the other indices of the tensor like this
    c[0, ...] = a
    print(c)


def operations_and_broadcasting():
    # Broadcasting is the use of an operation on the enitre array or matrix
    a = np.arange(5)
    print(a)
    # array A but backwards
    c = a[::-1]
    print("backwards")
    print(c)

    # you can do broadcasting like the following
    print("array A * 3.14")
    print(a * 3.14)

    print("array A * A, or A^2")
    print(a * a)

    print("array A * C")
    print(a * c)

    print("Scales C by +1 then use integer division ")
    print(a // (c + 1))

    # Broadcasting also applies to multipling vectors by matrixs, although the way its done is slightly different
    b = np.arange(25).reshape(5, 5)
    print(a)
    print("multiplied by")
    print(b)
    print("is equal to the following")
    print(a * b)

    # Dot multiplication is of the vectors then those elements added together
    # [0,1,2,3,4,5] * [0,1,2,3,4,5] = [0,1,4,9,16] = > 0 + 1 + 4 +9 + 16 = 30

    x = np.arange(5)
    print(np.dot(x, x))

    # Dot can also be done on matrices like the following
    z = np.arange(16).reshape(4, 4)
    y = np.arange(16).reshape(4, 4)
    v = np.dot(z, y)
    print(v)


def array_input_and_output():
    # With Python, you can load arrays from files in numerous ways
    # using a standard text files with spaces
    a = np.loadtxt("test.txt")
    print("text file with spaces")
    print(a)

    # using a text fies separated by tab spaces
    b = np.loadtxt("test_tab.txt")
    print("text file with tabs")
    print(b)

    # using a CSV, comma separated file but you have to tell it what is repeating the indexes
    c = np.loadtxt("test_comma.csv", delimiter=",")
    print("CSV, comma separated file.")
    print(c)

    # you can also save numpy matrixes to a file with.
    # Use .save if you want to save it as a numpy matrix, they are loaded but with .load not .loadtxt
    d = np.arange(25).reshape(5, 5)
    np.save("test_d.npy", d)
    # use .savetxt if you want  to save as a text file
    np.savetxt("test_d.txt", d)

    # you can also store multiple matrix in one file with .savez
    np.savez("test_multiple_matrices", a=a, b=b, d=d)
    # then you can access the individual matrix like a dictionary
    r = np.load("test_multiple_matrices.npz")
    # get a list of all the keys in the multiple matrix file called r
    print("A list of the matrices in the file")
    print(list(r.keys()))
    print(r["d"])


def numpy_and_images():
    # using numpy you can convert images to matrices
    # using PIL you can read and write images

    china = load_sample_images().images[0]
    flower = load_sample_images().images[1]

    # Using .shape of an array you can see the resolution of the image and the RGB vaules of the pixels
    print(" The resolution is 427 pixels by 640 pixels and the 3 is the RGB of each pixel")
    print(str(china.shape))
    print(str(flower.shape))

    # makes sure its in the right format to convert to an image
    imchina = Image.fromarray(china)
    imflower = Image.fromarray(flower)

    # displays images
    # imchina.show()
    # imflower.show()

    # saving an image to your files
    imflower.save("flower.png")
    imchina.save("china.png")

    # reading image from a file
    im = Image.open("china.png")
    img = np.array(im)
    # you can convert the image to other formats in this case to a gray scale.
    grayim = im.convert("L")
    # grayim.show()

    # convert the gray image to a array
    g = np.array(grayim)
    print("here is the same china image but in gray, notice the image loses the 3 rgb vaules.")
    print(str(g.shape))
