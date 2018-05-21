from Reader import Reader
import time
import os
import socket
from requests import post
import os

reader = Reader(os.getenv('SCANNERNAME', 'blah'))

url = os.environ['HASSURL'] + '/api/events/rfid_scan'
headers = {'x-ha-access': os.environ['HASSKEY'],
           'content-type': 'application/json'}

print('Reader is ready')

while True:
    card = reader.readCard()
    try:
        event_data = '{"scanner": "' + socket.gethostname() + '", "card_id": "'+card+'"}'
        print('Read card:', card, event_data)
        response = post(url, headers=headers, data=event_data)
        print(response.text)
        time.sleep(0.2)
    except OSError as e:
        print('Execution failed:', e)
        time.sleep(0.2)
