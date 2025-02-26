import json

def Lambda_handler(event, context):
 return {    
  'statusCode': 200
  'body': json.dumps('Hello from updated Lambda from vscode')
 }