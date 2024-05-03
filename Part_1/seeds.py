import json
import connect.connect
from models.models import FullName, Date, Location, Description, Quote, Autors, Quotes

def seed():

    with open("Part_1/json_file/authors.json", "r") as authors:
        data = json.load(authors)
        for i in data:
            name = FullName(name= i["fullname"])
            date = Date(date= i["born_date"])
            location = Location(location= i["born_location"])
            description = Description(description= i["description"])

            description_data = description.to_mongo()

            autors = Autors(
                name=name,
                born_date=date,
                born_location=location,
                description=description_data,
            )
            autors.save()


    with open("Part_1/json_file/qoutes.json", "r", encoding="utf-8") as q:
        data = json.load(q)
        for i in data:

            author_name = i["author"]
            author = Autors.objects(name__name=author_name).first()
            tag = i["tags"]
            quote = Quote(quote=i["quote"])
            quote = Quotes(
                author=author,
                quote=quote,
                tags=tag
            )
            quote.save()

if __name__=="__main__":
    seed()