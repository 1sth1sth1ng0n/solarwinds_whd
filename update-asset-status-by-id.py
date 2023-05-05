import requests
import json
import os
import sys

''' manipulates asset status for solarwinds web help desk.
'''

# set env variables
whd_hostname = os.environ.get("WHD_API_ENDPOINT")
api_key = os.environ.get("WHD_API_TECH_KEY")

asset = sys.argv[1]

url = f"{whd_hostname}/helpdesk/WebObjects/Helpdesk.woa/ra/Assets/{asset}?apiKey={api_key}"

''' custom status type id numbers can be collected from the 'AssetStatuses' endpoint
'''
payload = json.dumps({
  "assetstatus": {
    "id": 1, # 1 = 'deployed', 2 = 'inventory'
    "type": "AssetStatus"
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
