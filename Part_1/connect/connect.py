from mongoengine import connect
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('Section', 'mongo_user')
mongodb_pass = config.get('Section', 'mongodb_pass')
db_name = config.get('Section', 'db_name')
domain = config.get('Section', 'domain')

connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)