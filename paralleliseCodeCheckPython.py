# parallelise code check python.py

# import multiprocessing as mp ###installation required

def calculate_square(number):
    result = number * number
    print(f"The square of {number} is {result}")
    return result

def parallel_square(numbers):
    pool = mp.Pool(mp.cpu_count())
    results = pool.map(calculate_square, numbers)
    pool.close()
    pool.join()
    return results

def sequential_square(numbers):
    results = []
    for number in numbers:
        result = calculate_square(number)
        results.append(result)
    return results

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    expected_results = sequential_square(numbers)
    actual_results = parallel_square(numbers)

    assert expected_results == actual_results, "The parallelized code did not produce the expected results"
    print("The parallelized code produced the expected results")
