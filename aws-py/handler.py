import json
import boto3
import os

def hello(event, context):
    # client = boto3.client("lambda")
    # response =  client.list_functions()
    return (os.environ["FIRST_NAME"])
