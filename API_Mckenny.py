

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Fancmd 4
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/25/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

#FanStatus 4
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/26/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

#lightCmd 2
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/27/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

#lightCmdFDBK 4
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/28/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

#Curtains 4
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/29/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

#CurtainFDBK4
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/30/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)


#AnalogValues begin here

#SpaceTemperature 4
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analogValue/25/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify= False)

print(response.text)

#SpaceTemperature Set
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analogValue/26/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

#LightDim FDBK 4
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analogValue/27/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

#lightDim 4
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analogValue/28/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

#Bed 4
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analogValue/29/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

#bedFDbk
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analogValue/30/properties/presentValue"

payload = ""
headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

#multistateValues begin here

#HVACC 
import requests

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/multistateValue/5/properties/presentValue"

payload = ""

headers = {
  'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
  'Cookie': 'ECLYPSERESTSESSIONID=12mqmkw373sx7lik73e7xzk4s'
}

response = requests.request("GET",url, headers=headers, data=payload, verify=False)

print(response.text)


#json_result = response.json()
# requests < 1.0: json_result = result.json
#print(json_result)

#json_result['value'] = '2'

#print(json_result)

