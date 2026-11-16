# Python Libraries Implemented in C

## Overview
This project explores how Python can use code written in C to improve performance, specifically for computationally intensive operations. Here, I explored how Python can call C functions using the ctypes library, how C code can be compiled into a shared library, and how NumPy uses compiled implementations to process numerical arrays efficiently.

## Project Structure
* c_code/ — C source code and shared library compilation example.
* python_code/ — Python code that calls C functions using ctypes.
* experiments/ — Python versus NumPy performance benchmark.
* presentation/ — Presentation slides.
* resources/ — References and additional learning materials.

## What I Explored
I wrote a C function that adds two integers and called it from Python using ctypes. 
I also created a C function that calculates the average of an integer array. Python created a C-compatible array using ctypes and passed it to the C function. This demonstrated how pointers and arrays can be shared across the Python/C boundary.
I compared summing one million integers using a regular Python loop and NumPy's np.sum(). The experiment runs multiple times to compare execution times.

## Most Interesting Discoveries
1. Python can call C without rewriting it in Python. I found this interesting that Python could use code that had already been compiled into machine code.
2. Python and C can share data through pointers and arrays. I created a C function that calculated the average of an integer array and then called it from Python. Using ctypes, I created a C-compatible array and passed it to the C function. This helped me connect concepts like pointers, arrays, and function arguments from COMP211 to a real application.
3. Using C does not automatically make every operation faster. Performance is computation dependent, how data is passed between Python and C, and the overhead involved in calling functions. This made me realize why libraries like NumPy are designed to process entire arrays efficiently rather than relying on individual function calls for every element.

My biggest takeaway was that Python and C can work together, even though they are two separate languages. This allows Python to provide an accessible interface while the compiled code handles computationally intensive operations.

## References
Python ctypes documentation: https://docs.python.org/3/library/ctypes.html
NumPy documentation: https://numpy.org/doc/
