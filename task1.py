import random
import timeit
import copy

def insertion_sort(arr):
    """
    Time Complexity: O(N^2) in average and worst cases.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """
    Time Complexity: O(N log N) in all cases.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    """Helper function to merge two sorted lists."""
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add remaining elements (if any)
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged


def generate_data(size, data_type='random'):
    """Generates data sets of different types."""
    if data_type == 'random':
        return [random.randint(0, size * 2) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(size))
    elif data_type == 'reverse':
        return list(range(size, 0, -1))
    return []

def benchmark_algorithms():
    """Performs comparative analysis of sorting algorithms."""
    sizes = [100, 1000, 5000, 10000]
    
    number_of_runs = 5 

    print(f"{'Size':<10} | {'Insertion Sort (sec)':<25} | {'Merge Sort (sec)':<20} | {'Timsort (sorted) (sec)':<25}")
    print("-" * 85)

    for size in sizes:
        # Generate random data.
        # IMPORTANT: Use a copy of data for each algorithm so they sort the same set.
        data = generate_data(size, 'random')
        
        # 1. Insertion Sort
        # Use lambda function to pass a copy of data
        stmt_insertion = lambda: insertion_sort(copy.copy(data))
        time_insertion = timeit.timeit(stmt_insertion, number=number_of_runs)

        # 2. Merge Sort
        stmt_merge = lambda: merge_sort(copy.copy(data))
        time_merge = timeit.timeit(stmt_merge, number=number_of_runs)

        # 3. Timsort (Built-in sorted() function)
        # sorted() creates a new list, so copy() is not strictly necessary here, 
        # but added for experiment consistency.
        stmt_timsort = lambda: sorted(copy.copy(data)) 
        time_timsort = timeit.timeit(stmt_timsort, number=number_of_runs)

        print(f"{size:<10} | {time_insertion:<25.5f} | {time_merge:<20.5f} | {time_timsort:<25.5f}")

if __name__ == '__main__':
    print("Starting sorting algorithms benchmarking (Random Data)...")
    print("Time shown is cumulative for 5 runs for each size.\n")
    benchmark_algorithms()
    print("\nBenchmarking completed.")