
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#FanCmd 4 get
def get_fancmd4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/25/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json


#FanCmd4 post
def post_fancmd4(value):
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/25/properties/presentValue"

    payload = '{"value":"'+value+'"}'
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("post", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json
post_fancmd4("Active")


#FanStatus 4 get
def get_fanStatus4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/26/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json


#lightCmd 2 get
def get_Lightcmd2():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/27/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json

#lightCmd 2 post
def post_Lightcmd2(value):
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/27/properties/presentValue"

    payload = '{"value":"'+value+'"}'
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("post", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json
post_Lightcmd2("Active")


#lightCmdFDBK 4 get
def get_LightcmdFDBK4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/28/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json

#Curtains 4 get
def get_Curtains4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/29/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json

#Curtains 4 post
def post_Curtains4(value):
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/29/properties/presentValue"

    payload = '{"value":"'+value+'"}'
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("post", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json
post_Curtains4("Active")


#CurtainFDBK4 get
def get_CurtainsFDBK4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/30/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json



#AnalogValues begin here

#SpaceTemperature 4 get
def get_SpaceTemperature4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/25/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json

#SpaceTemperature4 post
def post_SpaceTemperature4(value):
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/25/properties/presentValue"

    payload = '{"value":"'+value+'"}'
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("post", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json
post_SpaceTemperature4("Active")


#SpaceTemperatureSet Get
def get_SpaceTemperatureSet4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/26/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json


#LightDim FDBK 4 get
def get_LightDimFDBK4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/27/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json

#lightDim 4 get
def get_LightDim4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/28/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json

#lightDim 4 post
def post_LightDim4(value):
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/28/properties/presentValue"

    payload = '{"value":"'+value+'"}'
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("post", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json
post_LightDim4("Active")

#Bed 4
def get_Bed4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/29/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json

#Bed4 post 
def post_Bed4(value):
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/29/properties/presentValue"

    payload = '{"value":"'+value+'"}'
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("post", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json
post_Bed4("Active")

#bedFDbk get
def get_BedFDBK4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/30/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json


#multistateValue begin here

#HVACC get
def get_BedFDBK4():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/multistateValue/5/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.json