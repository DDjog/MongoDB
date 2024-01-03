import json
from models import Author, Quote


def load_data(filename):
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)


def delete_data():
    Quote.drop_collection()
    Author.drop_collection()


def put_data_to_mongo():
    authors_data = load_data("authors.json")
    quotes_data = load_data("quotes.json")

    for a in authors_data:
        adata = Author(**a)
        adata.save()

    for q in quotes_data:
        qdata = Quote()
        qdata.author = Author.objects(fullname=q["author"]).first()
        qdata.tags = q["tags"]
        qdata.quote = q["quote"]
        qdata.save()


