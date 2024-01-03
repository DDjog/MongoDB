from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import DateTimeField, ReferenceField, EmbeddedDocumentField, ListField, StringField


class Author(Document):
    fullname = StringField()
    #born_date = DateTimeField() #problem z data na macOS, nie odczytywał formatu
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author)
    quote = StringField()


def find_quote_by_author(_fullname):
    author = Author.objects(fullname=_fullname).first()

    if author == None:
        return None

    quote_by_author = Quote.objects(author=author.id)

    return quote_by_author


def find_single_tag(_tag):
    single_tag = Quote.objects(tags=_tag)

    if single_tag == None:
        return None

    return single_tag


def find_tags(_tags):
    tags = Quote.objects(tags__all=_tags)

    if tags == None:
        return None

    return tags

