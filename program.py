# Returns list_1 + list_2 as they were two big numbers
def list_sum(list_1: list[int], list_2: list[int]) -> list[int]:
    min_length = min(len(list_1), len(list_2))
    list_1, list_2 = list_1[::-1], list_2[::-1]

    # common part
    result = [e_1 + e_2 for e_1, e_2 in zip(list_1[:min_length - 1], list_2[:min_length - 1])]
    result += list_1[min_length:] if min_length == len(list_1) else list_2[min_length:]
    return list_times_number(result[::-1], 1)


# Returns a list of elements of input_list times number
def list_times_number(input_list: list[int], number: int) -> list[int]:
    result = [element * number for element in input_list[::-1]]
    for index, element in enumerate(result[:-1]):
        if element >= 10:
            result[index + 1] += element // 10
            result[index] = element % 10

    return result[::-1]


# Returns list_1 * list_2 as they were two big numbers
def list_times_list(list_1: list[int], list_2: list[int]) -> list[int]:
    result = []
    for index, element in enumerate(list_2[::-1]):
        list_1_times_element = list_times_number(list_1, element) + [0] * index
        result = list_sum(result, list_1_times_element)
    return result


# Converts an integers list into a string
def list_to_string(input_list: list[int]) -> str:
    return ' '.join([str(d) for d in input_list])


# Converts a string into list of digits(integers)
def string_to_list(input_string):
    return [int(d) for d in input_string]


# Main program

first, second = '31112', '271828'
first_list, second_list = string_to_list(first), string_to_list(second)
print(f'{first} * {second} = {list_times_list(first_list, second_list)}')
