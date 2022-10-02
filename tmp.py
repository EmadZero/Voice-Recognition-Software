import urllib3
import requests
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/multistateValue/25/properties/presentValue"
url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/25/properties/presentValue"
url2 = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/25/properties/presentValue"

payload = '{"value":"Inactive"}'
payload = json.loads(payload)
print(payload)
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=12mqmkw373sx7lik73e7xzk4s'
}

response = requests.request("get", url, headers=headers, data=payload, verify=False)
response2 = requests.request("post", url2, headers=headers, data=payload, verify=False)


print(response.text)
print(response2.text)

alldevices = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue"
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=12mqmkw373sx7lik73e7xzk4s'
}

#alldevicesResponse = requests.request("GET", alldevices, headers=headers, data="", verify=False)
#print(alldevicesResponse.text)


