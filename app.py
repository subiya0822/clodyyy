import json

def lambda_handler(event, context):
    print("Event:", event)

    name = None
    if event.get("queryStringParameters") and "name" in event["queryStringParameters"]:
        name = event["queryStringParameters"]["name"]
    
    message = f"Hello, {name}!" if name else "Hello from Lambda!"

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": message})
    }
