import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import requests
import json

access_key = 'your_access_key'
secret_key = 'your_secret_key'

service = "bedrock"

url = "https://bedrock.us-east-1.amazonaws.com/model/ai21.j2-grande-instruct/invoke"

# ----- take json input form user as per the example body ------
print("Please enter the text to convert: ")
user_input = input()
print("Please enter in which language you want to convert: ")
language = input()

body = {"prompt":""}

body['prompt'] = user_input + " convert this text into " + language

# body = {
#     "prompt": "Business Management System. convert this json values to french.",
#     "maxTokens": 200,
#     "temperature": 0.7,
#     "topP": 1,
#     "stopSequences": [],
#     "countPenalty": {
#         "scale": 0
#     },
#     "presencePenalty": {
#         "scale": 0
#     },
#     "frequencyPenalty": {
#         "scale": 0
#     }
# }

# ------------------------------

body = json.dumps(body)

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='us-east-1'
)

bedrock = boto3.client(service_name='bedrock',region_name='us-east-1',endpoint_url='https://bedrock.us-east-1.amazonaws.com',aws_access_key_id=access_key,aws_secret_access_key=secret_key)

response = bedrock.invoke_model(body=body, modelId='ai21.j2-grande-instruct', accept="*/*", contentType='application/json')

json_response = json.loads(response['body'].read())

print("Converted result response: ")
print(json_response['completions'][0]['data']['text'])
