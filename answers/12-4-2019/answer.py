def main():
    test_array = [1, 2, 3, 4, 5]
    actual_results = number_array_multiplier(test_array)


def number_array_multiplier(number_array):
    results_array = []
    ignore_index = 0
    loop = 0
    product = 1

    while len(results_array) < len(number_array):
        if loop != ignore_index:
            product = product * number_array[loop]
        
        if loop == len(number_array) - 1:
            loop = 0
            ignore_index += 1
            results_array.append(product)
            product = 1
            continue
        
        loop += 1
    
    return results_array



if __name__ == "__main__":
    main()