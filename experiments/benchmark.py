import time
import statistics
import numpy as np

# Create one million numbers
numbers = list(range(1_000_000))
numpy_numbers = np.arange(1_000_000)

python_times = []
numpy_times = []

# Run each experiment 5 times
for i in range(5):

    # Python benchmark
    start = time.perf_counter()

    python_total = 0
    for number in numbers:
        python_total += number

    python_times.append(time.perf_counter() - start)

    # NumPy benchmark
    start = time.perf_counter()

    numpy_total = np.sum(numpy_numbers)

    numpy_times.append(time.perf_counter() - start)

# Calculate average times
python_average = statistics.mean(python_times)
numpy_average = statistics.mean(numpy_times)

print("Python total:", python_total)
print("NumPy total:", numpy_total)

print("Python average:", python_average)
print("NumPy average:", numpy_average)

print("Speedup:", python_average / numpy_average)