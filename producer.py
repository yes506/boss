import json
import pika
import json

params = pika.URLParameters('amqps://adyzazjv:eX3pCl0sCOFl6iETiL5bf0fngTrkLN0j@dingo.rmq.cloudamqp.com/adyzazjv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(methods, body):
    properties = pika.BasicProperties(methods)
    channel.basic_publish(exchange='', routing_key='order', body=json.dumps(body), properties=properties)