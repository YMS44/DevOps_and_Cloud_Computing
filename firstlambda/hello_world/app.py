import json

# import requests


def first_lambda(event, context):
    return "Hello: "+str(event) # Because event is a dictionary