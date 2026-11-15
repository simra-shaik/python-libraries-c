import ctypes

# Load compiled C library
lib = ctypes.CDLL("./c_code/libmylibrary.dylib")

# Tell Python C function's argument types
lib.add_numbers.argtypes = [ctypes.c_int, ctypes.c_int]

# Tell Python C function's return type
lib.add_numbers.restype = ctypes.c_int

# Call C function
result = lib.add_numbers(5, 10)

print("Result from C:", result)