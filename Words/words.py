__author__ = 'Patrick Luboobi'


def words(string) -> dict:
    """
        Function to count each Words in sentence
        and store results in a dictionary

        Args:
            string: A sentence of Words
        Raises:
            TypeError: If Argument is not a string
        Returns:
            dict: Each word and the number of times 
                  it occurs  
        """

    # Check argument type
    if not isinstance(string, str):
        raise TypeError('Argument should be a string')
    else:
        output_dict = {}

        # Make string a list of individual Words
        str_list = string.split()

        for item in str_list:
            # If item is a digit, make it an integer
            if item.isdigit():
                item = int(item)

            # Update word already in dictionary
            if item in output_dict:
                output_dict[item] += 1

            # Enter word if not already in dictionary
            else:
                output_dict[item] = 1

    return output_dict
