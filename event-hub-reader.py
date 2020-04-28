import os
import sys
import logging
import time
from azure.eventhub import EventHubClient, Receiver, Offset


logger = logging.getLogger("azure")

EVENT_HUB_URL = os.environ["EVENT_HUB_URL"]
EVENT_HUB_KEY = os.environ["EVENT_HUB_KEY"]

USER = "RootManageSharedAccessKey"


CONSUMER_GROUP = "$default"
OFFSET = Offset("-1")
PARTITION = "0"

total = 0
last_sn = -1
last_offset = "-1"
client = EventHubClient(EVENT_HUB_URL, debug=False, username=USER, password=EVENT_HUB_KEY)
try:
    receiver = client.add_receiver(
        CONSUMER_GROUP, PARTITION, prefetch=5000, offset=OFFSET)
    client.run()
    start_time = time.time()
    for event_data in receiver.receive():
        print("Received: {}".format(event_data.body_as_str(encoding='UTF-8')))
        total += 1

    end_time = time.time()
    client.stop()
    run_time = end_time - start_time
    print("Received {} messages in {} seconds".format(total, run_time))

except KeyboardInterrupt:
    pass
finally:
    client.stop()
