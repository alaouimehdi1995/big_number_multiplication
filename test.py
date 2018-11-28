from program import (
    list_sum,
    list_times_list,
    list_times_number,
    list_to_string,
    string_to_list,
)



def success_handler(test_name, test_index, test_tuple, result):
    print(f'Test {test_name} {test_index}, OK.')


def failure_handler(test_name, test_index, test_tuple, result):
    print(f'Test {test_name} {test_index}: {test_tuple[0]} * {test_tuple[1]} failed.'
          f' Expected: {test_tuple[2]}, found: {result}')


def test_list_sum():
    test_name = 'list_sum'
    list_1, list_2 = [9, 8, 7], [1, 4, 8, 3]
    expected_result = [2, 4, 7, 0]
    result = list_sum(list_1, list_2)
    handler = success_handler if result == expected_result else failure_handler
    handler(test_name, 0, (list_1, list_2, expected_result), result)


def test_list_times_number():
    test_name = 'list_times_number'
    array, number = [9, 8, 7], 3
    expected_result = [2, 9, 6, 1]
    result = list_times_number(array, number)
    handler = success_handler if result == expected_result else failure_handler
    handler(test_name, 0, (array, number, expected_result), result)


def test_list_times_list():
    test_name = 'list_times_list'
    list_1, list_2 = [9, 8, 7], [1, 4, 8, 3]
    expected_result = [1, 4, 6, 3, 7, 2, 1]
    result = list_times_list(list_1, list_2)
    handler = success_handler if result == expected_result else failure_handler
    handler(test_name, 0, (list_1, list_2, expected_result), result)


def test_program():
    TESTS = [
        ('1', '1', '1'),
        ('3', '6', '18'),
        ('100', '2', '200'),
        ('11111', '11111', '123454321'),
        ('31112', '271828', '8457112736'),
    ]
    test_name = 'e2e'
    for index, test in enumerate(TESTS):
        result = list_to_string(
            list_times_list(
                string_to_list(test[0]),
                string_to_list(test[1]),
            ),
        )
        handler = success_handler if result == test[2] else failure_handler
        handler(test_name, index, test, result)


if __name__ == '__main__':
    tests_to_execute = [
        test_list_sum,
        test_list_times_number,
        test_list_times_list,
        test_program,
    ]
    for test in tests_to_execute:
        test()
