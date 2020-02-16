from pymongo import MongoClient


def connection(collection_name):
    client = MongoClient(
        host='23.251.129.52',
        port=27017,
        username="graph_user",
        password="pass",
        authSource='graph'
    )

    db = client[f'graph']
    collection = db[f'{collection_name}']

    return collection
