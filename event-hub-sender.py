import sys
import logging
import datetime
import time
import os

from azure.eventhub import EventHubClient, Sender, EventData

logger = logging.getLogger("azure")


EVENT_HUB_URL = os.environ["EVENT_HUB_URL"]
EVENT_HUB_KEY = os.environ["EVENT_HUB_KEY"]

USER = "RootManageSharedAccessKey"

try:
    if not EVENT_HUB_URL:
        raise ValueError("No EventHubs URL supplied.")

    # Create Event Hubs client
    client = EventHubClient(EVENT_HUB_URL, debug=False, username=USER, password=EVENT_HUB_KEY)
    sender = client.add_sender(partition="0")
    client.run()
    try:
        start_time = time.time()
        for i in range(100):
            print("Sending message: {}".format(i))
            message = "Message {}".format(i)
            sender.send(EventData(message))
    except:
        raise
    finally:
        end_time = time.time()
        client.stop()
        run_time = end_time - start_time
        logger.info("Runtime: {} seconds".format(run_time))

except KeyboardInterrupt:
    pass
