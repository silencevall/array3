def get_square(list_data):
    if len(list_data) > 0:
        for i in range(len(list_data)):
            list_data[i] = list_data[i] ** 0.5
    return list_data

