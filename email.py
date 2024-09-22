import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    ses.send_email(
        Source='${SOURCE_EMAIL}',
        Destination={
            'ToAddresses': [
                event['destinationEmail'],
            ]
        },
        Message={
            'Subject': {
                'Data': 'Project purpose'
            },
            'Body': {
                'Text': {
                    'Data': event['message']
                }
            }
        }
    )
    return 'Email sent!'
