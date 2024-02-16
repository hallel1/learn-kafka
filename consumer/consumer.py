from confluent_kafka import Consumer


def main():
    conf = {'bootstrap.servers': 'localhost:9092',
            'group.id': 'hallel_group',
            'auto.offset.reset': 'smallest'}

    consumer = Consumer(conf)
    consumer.subscribe(['hallel_topic'])
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        print('Received message: {}'.format(msg.value().decode('utf-8')))

    consumer.close()


if __name__ == '__main__':
    main()
