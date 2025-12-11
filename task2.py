from functools import reduce

def merge(left, right):
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

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def merge_k_lists(lists):
    """
    Uses a sequential merging approach (similar to reduce).
    """
    if not lists:
        return []
    
    result = lists[0]    
    for i in range(1, len(lists)):
        result = merge(result, lists[i])
        
    return result

    # OR
    # return reduce(merge, lists)


if __name__ == '__main__':
    lists_to_merge = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(f"Input lists: {lists_to_merge}")
    
    merged_list = merge_k_lists(lists_to_merge)
    print("Sorted list:", merged_list)

    # Additional test
    lists_2 = [[10, 20], [5, 15, 25], [1], []]
    print(f"\nInput lists 2: {lists_2}")
    print("Sorted list 2:", merge_k_lists(lists_2))
