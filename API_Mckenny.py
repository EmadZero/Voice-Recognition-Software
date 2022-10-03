import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def update_ui(value):
    url = "http://127.0.0.1:5000/update"
    payload = value
    headers = {
      'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


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
    #print(response.text)
    return response.text


#FanCmd4 post
def post_fancmd4(value):
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/25/properties/presentValue"

    payload = json.dumps({
      "value": value
    })


    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    print(payload)
    response = requests.request("post", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.text

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
    return response.text


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
    return response.text

#lightCmd 2 post
def post_Lightcmd4(value):
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binaryValue/27/properties/presentValue"

    payload = json.dumps({
      "value": value
    })

    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    print(payload)
    response = requests.request("post", url, headers=headers, data=payload, verify=False)
    
    return response.text



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
    return response.text

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
    return response.text

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
    return response.text


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
    return response.text



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
    return response.text

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
    return response.text


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
    return response.text


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
    return response.text

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
    return response.text

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
    return response.text

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
    return response.text

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
    return response.text

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
    return response.text


#multistateValue begin here

#HVACC get
def get_HVACC():
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/multistateValue/5/properties/presentValue"

    payload = ""
    headers = {
    'Authorization': 'Basic dGVhbTU6Q2hhbGxlbmdlVGVhbTU=',
    'Content-Type': 'application/json',
    'Cookie': 'ECLYPSERESTSESSIONID=1nf3d32b74ekp1fvq6xvz85pfy'
    }
    response = requests.request("get", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return response.text


post_fancmd4('Inactive')
