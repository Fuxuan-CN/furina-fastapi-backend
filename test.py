import random

def quick_sort(data, mode="up"):
    if mode not in ["up", "down"]:
        raise ValueError("mode must be up or down")
    
    if len(data) <= 1:
        return data
    
    pivot = data[0]
    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]
    
    if mode == "up":
        return quick_sort(left, mode) + [pivot] + quick_sort(right, mode)
    else:
        return quick_sort(right, mode) + [pivot] + quick_sort(left, mode)

if __name__ == "__main__":
    import sys
    import time

    # 使用print()
    start_time = time.time()
    for _ in range(3):
        print("Hello, world!")
    end_time = time.time()
    print("Time taken with print():", end_time - start_time)

    # 使用sys.stdout.write()
    start_time = time.time()
    for _ in range(3):
        sys.stdout.write("Hello, world!\n")
    end_time = time.time()
    print("Time taken with sys.stdout.write():", end_time - start_time)



