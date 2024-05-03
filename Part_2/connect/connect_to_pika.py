import pika

def connect_to_pika(loggin:str="guest", password:str="guest", host:str="localhost", port:int=5672):
    credentials = pika.PlainCredentials(loggin, password)
    parameters = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    return connection
