import json

def lambda_handler(event, context) :
    order = {'id':123,'itemName':'Laptop','quantity':3} # get order data from user

    return { # Return a dummy status code and message
        'statusCode' : 200,
        'headers' : {},
        'body' : json.dumps(order)
    } 