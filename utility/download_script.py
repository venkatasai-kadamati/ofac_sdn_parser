# Script to download the OFAC XML file
# ! Problem: signed certificate is needed to download the file
# ! TODO: 👎 Solution: disable certificate verification, but due to company firewall it is not granting access
# ! Workaround Solution: Just scrap what part of data we need
# ** -------------------------- SCRIPT START ---------------------------
import requests

# Retrieve the XML from OFAC
url = 'https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xml'
response = requests.get(url, verify=True)  # Disable certificate verification

if response.status_code == 200:
    xml_content = response.content
else:
    print("Error downloading XML")
    exit()

# import ssl
# import certifi
# import requests

# print(ssl.get_server_certificate(('www.treasury.gov', 443))) 

