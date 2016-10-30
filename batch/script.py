import sched, time
from kafka import KafkaConsumer
import sched, time
from elasticsearch import Elasticsearch
import json
es = Elasticsearch([{'host': 'es', 'port': 9200}])

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
	print("hello")
	consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
	for message in consumer:
		new_listing = json.loads((message.value).decode('utf-8'))
		print(new_listing)
		ret = es.index(index='listing_index', doc_type='listing', id=new_listing['id'], body=new_listing)
	es.indices.refresh(index="listing_index")

	s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()