import pika
import json
from connect.connect_to_pika import connect_to_pika
from connect.connect import connect
from models.models import Contact

def main():
    connection = connect_to_pika()
    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=receiving_message)

    channel.start_consuming()

def receiving_message(ch, method, properties, body):
    message = json.loads(body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(message)
    contact_id = message["contact_id"]
    contact = Contact.objects(id=contact_id).first()
    contact.send = True
    contact.save()


if __name__ == '__main__':
    main()