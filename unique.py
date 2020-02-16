

def first_missing(num_dict):
    if len(num_dict) == 0:
        return 0
    else:
        i = 0
        for i in range(len(num_dict)):
            if i not in num_dict:
                return i

        return i + 1


def find_unique(name, items_collection):
    query = {'name': f'{name}'}
    projection = {'_id': False, 'unique_name': True}

    same_name_cursor = items_collection.find(query, projection)
    num_dict = {}
    for document in same_name_cursor:
        document_unique_name = document['unique_name']
        name_num = document_unique_name.split('_')[1]
        num_dict[int(name_num)] = True

    unique_name = f'{name}_{str(first_missing(num_dict))}'
    return unique_name
