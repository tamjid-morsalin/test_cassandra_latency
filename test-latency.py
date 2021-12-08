from cassandra.cluster import Cluster
import random
from datetime import datetime

cluster = Cluster(['localhost'])
session = cluster.connect('keyspace_test_latency')
session.default_timeout = 60

attack_type_arr = ["phishing", "dos", "malware", "mim", "unknown"]
attack_protocol_arr = ["udp", "ftp", "tcp"]

for x in range(20000000):
	ip = "103.134.25." + str(random.randint(0,255))
	attack_type = attack_type_arr[random.randint(0,4)]
	average_incoming_traffic = 80025028 + x
	attack_protocol = attack_protocol_arr[random.randint(0,2)]
	average_incoming_pps = 464 + random.randint(0,100)
	average_incoming_flow = 5 + random.randint(0,10)
	
	session.execute(
		"""
		INSERT INTO test_latency (
			ip,
			attack_type,
			average_incoming_traffic,
			attack_protocol,
			average_incoming_pps,
			average_incoming_flow
		)
		VALUES (%s, %s, %s, %s, %s, %s)
		""",
		(
			ip,
			attack_type,
			average_incoming_traffic,
			attack_protocol,
			average_incoming_pps,
			average_incoming_flow
		)
	)
	
	print(x)

