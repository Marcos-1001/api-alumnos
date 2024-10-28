import boto3
import json

def lambda_handler(event, context):
    print(event)
    # Entrada (json)
    alumno = event['body']
    
       

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    # Modificar alumno


    # Columna alumno_datos es un diccionario
    response = table.update_item(
        Key={
            'tenant_id': alumno['tenant_id'],
            'alumno_id': alumno['alumno_id']
        },
        UpdateExpression="set alumno_datos = :a",
        ExpressionAttributeValues={
            ':a': alumno['alumno_datos']
        },
        
        ReturnValues="UPDATED_NEW"
    )

    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }