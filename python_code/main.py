import ctypes

# Load our compiled C library
lib = ctypes.CDLL("./c_code/libmylibrary.dylib")

# Set up add_numbers
lib.add_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add_numbers.restype = ctypes.c_int

# Set up calculate_average
lib.calculate_average.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int
]
lib.calculate_average.restype = ctypes.c_double

# Test the addition function
result = lib.add_numbers(5, 10)
print("Addition result:", result)

# Create an array of integers in Python
numbers = (ctypes.c_int * 4)(10, 20, 30, 40)

# Pass the array to our C function
average = lib.calculate_average(numbers, 4)

print("Average:", average)