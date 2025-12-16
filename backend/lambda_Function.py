import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactFormData')

def lambda_handler(event, context):
    try:
        body = event.get('body', {})
        if isinstance(body, str):
            body = json.loads(body)

        item = {
            'id': str(uuid.uuid4()),
            'name': body.get('name'),
            'email': body.get('email'),
            'message': body.get('message')
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'content-type'
            },
            'body': json.dumps({'message': 'Form submitted successfully'})
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }

