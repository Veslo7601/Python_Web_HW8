
import pika
import json
from faker import Faker
from models.models import Contact, FullName, Email, Body, Date
from connect.connect_to_pika import connect_to_pika
from random import randint

from connect.connect import connect

def main():

    connection = connect_to_pika()
    channel = connection.channel()
    channel.exchange_declare(exchange="Task", exchange_type='direct')
    channel.queue_declare(queue="task_queue", durable=True)
    channel.queue_bind(exchange="Task", queue="task_queue")

    for _ in range(0, randint(1, 5)):
        fake = Faker()
        name = FullName(name=fake.name())
        email = Email(email=fake.email())
        body = Body(body=fake.text())
        date = Date(date=fake.date())

        contact = Contact(
            name=name,
            email=email,
            body=body,
            date=date,
        )

        contact_data = contact.to_mongo()
        contact.save()
        contact_id = str(contact.id)
        message_data = {
            'contact_id': contact_id,
            'contact_data': contact_data
        }

        channel.basic_publish(
            exchange="Task",
            routing_key="task_queue",
            body=json.dumps(message_data).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
        print(f"Message {contact_id} send")

    connection.close()

if __name__ == '__main__':
    main()


