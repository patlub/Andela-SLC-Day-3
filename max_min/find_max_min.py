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
