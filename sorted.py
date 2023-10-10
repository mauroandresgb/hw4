def sort_dictionary(input_dict):

    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a valid dictionary.")

    sorted_dict = sorted(input_dict.items(), key=lambda x: x[0], reverse=True)

       result_list = [(name, data[0]) for name, data in sorted_dict]

    return result_list

