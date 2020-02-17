from etwas import connection


noun_list = [
    {
        "english": ["child"],
        "german": ["das Kind"],
        "polish": ["dziecko"],
    }
]


def add_item_to_db(data):
    item_id = connection('nouns').insert_one(data).inserted_id


for noun in noun_list:
    add_item_to_db(noun)
