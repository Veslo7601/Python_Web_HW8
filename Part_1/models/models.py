from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import (ReferenceField, DateTimeField,
                                EmbeddedDocumentField, ListField,
                                StringField)


class FullName(EmbeddedDocument):
    name = StringField()

class Date(EmbeddedDocument):
    date = StringField()

class Location(EmbeddedDocument):
    location = StringField()

class Description(EmbeddedDocument):
    description = StringField()

class Quote(EmbeddedDocument):
    quote = StringField()

class Autors(Document):
    name = EmbeddedDocumentField(FullName)
    born_date = EmbeddedDocumentField(Date)
    born_location = EmbeddedDocumentField(Location)
    description = EmbeddedDocumentField(Description)

class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Autors)
    quote = EmbeddedDocumentField(Quote)
