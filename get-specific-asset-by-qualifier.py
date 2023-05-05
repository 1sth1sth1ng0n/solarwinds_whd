import requests
import os
import sys

''' obtains long listing asset details from solarwinds web help desk, using s/n or hostname.
'''

# set env variables
whd_hostname = os.environ.get("WHD_API_ENDPOINT")
api_key = os.environ.get("WHD_API_TECH_KEY")

serial = sys.argv[1]

# can also use ?qualifier=(networkName%20%3D%20'ASSET_HOST_NAME')
url = f"{whd_hostname}/helpdesk/WebObjects/Helpdesk.woa/ra/Assets/?qualifier=(serialNumber%20%3D%20{serial})&style=long&apiKey={api_key}"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)