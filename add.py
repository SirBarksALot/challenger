from etwas import connection


noun_list = [
    {
        "article": "der",
        "noun_singular": "Vater",
        "noun_plural": "Väter"
    }
]


def add_item_to_db(data):
    item_id = connection('nouns').insert_one(data).inserted_id


for noun in noun_list:
    add_item_to_db(noun)
