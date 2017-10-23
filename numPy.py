import numpy as np
my_list = [1,2,3,4,5,6]

print(my_list)

#creating single dimension array of vector by casting python list to numPy array
npvector = np.array(my_list)

print(npvector)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]

nptwodarray = np.array(my_mat)

print(nptwodarray)

print(np.arange(0,10))# python range like function to generate vector array

print(np.arange(0,10, 2))#with step

print(np.zeros(3))#generate single/vector array using zeros

print(np.zeros((3,3)))#generate 2d/matrix array using zeros or ones and passing arg as tuple

print(np.ones((3,3)))

print(np.linspace(0,5,10))

print(np.eye(3))

print(np.random.rand(5))

print(np.random.rand(3,3))

print(np.random.randn(3,3))

print(np.random.randn(3))

print(np.random.randint(0,10,3))

rangearr = np.arange(0,25)
print(rangearr)
print(rangearr.reshape((5,5)))
print(rangearr.min())
print(rangearr.max())
print(rangearr.argmax())
print(rangearr.argmin())

print("Index and Selection")
#numpy indexing and selection
indexarr = np.arange(0,11)
print(indexarr)
#indexing
print(indexarr[7])
#slicing
print(indexarr[2:4])
#slicing will change original instance as below
slice_of_arr = indexarr[0:5]
print(slice_of_arr)
slice_of_arr[:] = 0
print(slice_of_arr)
print(indexarr)
#to avoid use copy
indexarr_copy = indexarr.copy()
print(indexarr)
print(indexarr_copy)
indexarr_copy[:]=1
print(indexarr_copy)
print(indexarr)

arr_2d = np.array([[5,10,15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)
print(arr_2d[1][1])
print(arr_2d[1,1])

#grabbing sub matrix from matrix
print(arr_2d[:2,1:])
print(arr_2d[:2,:2])

#boolean array using comparator operator
normal_arr = np.arange(1, 11)
print(normal_arr)
bool_arr = normal_arr > 3
print(bool_arr)

#grabbing from normal array from bool_arr
print(normal_arr[bool_arr])
print(normal_arr[normal_arr>4])

new_2d_array = np.arange(50).reshape(5,10)
print(new_2d_array)
print(new_2d_array[2:4,2:4]) #new_2d_array([from_row:to_row,from_col,to_col])

#numpy operation
print("numpy operation")

op_arr = np.arange(0,10)
print(op_arr + op_arr)
print(op_arr - op_arr)
print(op_arr * op_arr)
print(op_arr / 2)
print(op_arr / op_arr)
