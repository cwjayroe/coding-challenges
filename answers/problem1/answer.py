def main():
    test_array = [5,8,12]
    test_k = 18

    check_if_matches(test_array, test_k)

def check_if_matches(number_array, k):

    number_array_index = 0
    number_array_length = len(number_array)

    for loop_number in number_array:
        for range_number in range(number_array_index, number_array_length):
            number_addition = loop_number + number_array[range_number]

            if number_addition == k:
                return True

        number_array_index += 1
    

    return False


if __name__ == "__main__":
    main()