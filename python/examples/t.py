def positive_numbers(input_list):
    output_list = []
    for num in input_list:
        if num > 0:
            output_list.append(num)
    return output_list


print(positive_numbers([-1, 2, -3, 0, 4, 5, -6]))