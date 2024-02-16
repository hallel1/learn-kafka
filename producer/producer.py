from confluent_kafka import Producer
import socket


def main():
    conf = {'bootstrap.servers': 'localhost:9092',
            'client.id': socket.gethostname()}

    producer = Producer(conf)
    for i in range(100):
        producer.produce("hallel_topic", f"aloo-{i}", callback=delivery_report)
        producer.poll(30)

    producer.flush()


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}] {}'.format(msg.topic(), msg.partition(), msg.value()))


if __name__ == '__main__':
    main()
