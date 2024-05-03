from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import (ReferenceField, DateTimeField,
                                EmbeddedDocumentField, ListField,
                                StringField, BooleanField)

class FullName(EmbeddedDocument):
    name = StringField()

class Email(EmbeddedDocument):
    email = StringField()

class Body(EmbeddedDocument):
    body = StringField()

class Date(EmbeddedDocument):
    date = StringField()

class Contact(Document):
    name = EmbeddedDocumentField(FullName)
    email = EmbeddedDocumentField(Email)
    send = BooleanField(default=False)
    body = EmbeddedDocumentField(Body)
    date = EmbeddedDocumentField(Date)
