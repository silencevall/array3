def get_cortege(list_data):
    average = 1
    if len(list_data) > 0:
        average = sum(list_data)/len(list_data)
    for i in range(len(list_data)):
        list_data[i] = list_data[i]/average
    return list_data
