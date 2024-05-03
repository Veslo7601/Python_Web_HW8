import json
import connect.connect
from models.models import FullName, Date, Location, Description, Quote, Autors, Quotes

BOT_ACTIVE = True

def decorator(func):
    def exeption(*args, **kargs):
        try:
            return func(*args, **kargs)
        except Exception as e:
            return "Enter correct command"
    return exeption

@decorator
def command_parser(comand_input:str):
    """function parse command"""
    command_list = {
        "name":command_find_name,
        "tag":command_find_tags,
        "tags":command_find_tags,
        "exit":command_exit,
    }

    new_input = comand_input.split(":")
    return command_list[new_input[0]](new_input[1:])

def command_find_name(input_name:list[str] = "Albert Einstein"):
    """function for find quotes using author name"""
    new_name = input_name[0].strip()
    author_list = Autors.objects(name__name=new_name).first()
    if author_list:
        data = {}
        author = author_list.name.name
        data[author] = []
        quotes = Quotes.objects(author=author_list)
        for i in quotes:
            data[author].append(i.quote.quote)
        return data

def command_find_tags(input_tag_list:list = None):
    """function for find quotes using tags"""

    if input_tag_list is None:
        input_tag_list = ["humor", "value"]

    input_tag_list = "".join(input_tag_list).strip().replace(",","").split(" ")
    data = []
    for input_tag in input_tag_list:
        tags = Quotes.objects(tags=input_tag).all()
        for i in tags:
            data.append(f"Autor: {i.author.name.name}, Quote: {i.quote.quote}, Tags: {i.tags}")
    return data

def command_exit(value=None):
    """function close bot"""
    global BOT_ACTIVE
    BOT_ACTIVE = False
    return "Good bye"

def main():
    """function main"""
    print("Hello")
    while BOT_ACTIVE:
        user_input = input("Enter command ->  ")
        print(command_parser(user_input))

if __name__=="__main__":
    main()