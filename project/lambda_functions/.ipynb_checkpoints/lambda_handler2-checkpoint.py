import json
# import sagemaker
import base64
# from sagemaker.serializers import IdentitySerializer
import boto3

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2022-10-18-21-51-06-524" ## TODO: fill in

def lambda_handler(event, context):

    
    # Decode the image data
    image = base64.b64decode(event['image_data'])

    # # Instantiate a Predictor
    # predictor = Predictor(
    #     endpoint_name=endpoint,
    #     session=sagemaker.Session()
    # )
    
    
    runtime= boto3.Session().client(service_name='sagemaker-runtime', region_name='us-east-1')
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, 
                                           ContentType='image/png', 
                                           Body=image)
    
    event["inferences"] = json.loads(response['Body'].read().decode("utf-8"))

    # # For this model the IdentitySerializer needs to be "image/png"
    # predictor.serializer = IdentitySerializer("image/png")
    
    # # Make a prediction:
    # inferences = predictor.predict(image)## TODO: fill in
    
    # # We return the data back to the Step Function    
    # event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': event
    }
    