# Returns list_1 + list_2 as they were two big numbers
def list_sum(list_1: list, list_2: list) -> list:
    list_1, list_2 = list_1[::-1], list_2[::-1]
    list_1, list_2 = (list_1, list_2) if len(list_1) >= len(list_2) else (list_2, list_1)
    result = [
        e + list_2[i] if i < len(list_2) else e for i, e in enumerate(list_1)
    ]
    return list_times_number(result[::-1], 1)


# Returns a list of elements of input_list times number
def list_times_number(input_list: list, number: int) -> list:
    result = [element * number for element in input_list[::-1]]
    increment_number = 0
    for index, element in enumerate(result):
        result[index] = element + increment_number
        increment_number = result[index] // 10
        result[index] = result[index] % 10

    if increment_number > 0:
        result.append(increment_number)
    return result[::-1]


# Returns list_1 * list_2 as they were two big numbers
def list_times_list(list_1: list, list_2: list) -> list:
    for index, element in enumerate(list_2[::-1]):
        list_1_times_element = list_times_number(list_1, element) + [0] * index
        result = list_1_times_element if index == 0 else list_sum(result, list_1_times_element)
    return result


# Converts an integers list into a string
def list_to_string(input_list: list) -> str:
    return ''.join([str(d) for d in input_list])


# Converts a string into list of digits(integers)
def string_to_list(input_string):
    return [int(d) for d in input_string]


# Main program
if __name__ == '__main__':
    first, second = '31112', '271828'
    first_list, second_list = string_to_list(first), string_to_list(second)
    print(f'{first} * {second} = {list_to_string(list_times_list(first_list, second_list))}')
