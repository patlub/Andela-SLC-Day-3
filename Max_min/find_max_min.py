__author__ = 'Patrick Luboobi'


def find_max_min(arg_list) -> list:
    """
    Finds max and minimum number from a list and returns them in list
    Args:
        arg_list: A list of integers
    Raises:
        ValueError: If non int found in list arg
    Returns:
        list: Containing maximum and minimum number
    """

    # Argument should be a list
    if not isinstance(arg_list, list):
        raise TypeError('Argument should be a list')

    # All list items should be numbers
    elif not all(isinstance(item, int) for item in arg_list):
        raise ValueError('All list items should be integers')

    else:
        output_list = []

        # Sort list first
        arg_list.sort()

        first = arg_list[0]
        last = arg_list[len(arg_list) - 1]

        # Append minimum element to list
        output_list.append(first)

        # If min and max are not equal
        # Append max to list too
        if first != last:
            output_list.append(last)

        return output_list
