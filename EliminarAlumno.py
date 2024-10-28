import boto3
import json

def lambda_handler(event, context):
    print(event)
    # Entrada (json)
    alumno = event['body']
    
     

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    response = table.delete_item(
        Key={
            'tenant_id': alumno['tenant_id'],
            'alumno_id': alumno['alumno_id']
        }
    )

    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }