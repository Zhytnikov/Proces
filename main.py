from time import perf_counter
from multiprocessing import Pool, cpu_count

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def synchronous(numbers):
    start_time = perf_counter()
    for number in numbers:
        factorize(number)
    end_time = perf_counter()
    return end_time - start_time

def multiprocessing(numbers):
    start_time = perf_counter()
    with Pool(processes=cpu_count()) as pool:
        pool.map(factorize, numbers)
    end_time = perf_counter()
    return end_time - start_time

if __name__ == '__main__':
    numbers = (10651060, 10651060, 10651060, 10651060)

    time_sync = synchronous(numbers)
    print(f'Time for synchronous: {time_sync:.2f} seconds.')

    time_multi = multiprocessing(numbers)
    print(f'Time for multiprocessing: {time_multi:.2f} seconds.')
