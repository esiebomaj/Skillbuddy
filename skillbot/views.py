from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse

import json, requests, random, re
from pprint import pprint

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from wit import Wit

from .response import Response
import random



# ===================
# wit config
# ===================

wit_access_token='Z3TTKIDS35IZIRRKAW7AOTLVNQNXCSMU'

client=Wit(access_token=wit_access_token)

# ============================

# Create your views here.

PAGE_ACCESS_TOKEN = "EAANxRXY346UBADPa9SHZCLpGtCTAhTKMz94ILv55SJh0GM4qLDDOPSIdnCuKjpO9RBZA6o2y2MQYxhfR8hCLc79MC2eeMFggAjLWzfFkK0dKVLndcVkMZBwItmPZCIiCcvZCI6Q3ZBYgyGsNEpICJSNM95guPOlCNB5R62SjHAywZDZD"
VERIFY_TOKEN = "123456789"



def generate_response(characteristeics, user_details):
    name=user_details['first_name']
    intent=characteristeics[0]

    if intent == None:
        response='i dont understand what u are saying oga'
    else:
        response=random.choice(Response[intent])

    return response

	


#helper funtion to get characteristeics
def get_xter(wit_response):

    if wit_response['intents'] != []:
        intent=wit_response['intents'][0]['name']
    else:
        intent=None

    entities1={}
    if wit_response['entities'] !={}:
        for entity in wit_response['entities']:
            a=entity
            entities1[a]=wit_response['entities'][a][0]['body']
    else:
        entities1=None

    if wit_response['traits'] != {}:
        sentiment=wit_response['traits']['wit$sentiment'][0]['value']
    else:
        sentiment=None

    text=wit_response['text']

    return intent, entities1, sentiment, text


# This function sends the message back to the user
def post_facebook_message(fbid, recevied_message):           
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token={}'.format(PAGE_ACCESS_TOKEN)
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())


#The bot view
class BotView(generic.View):
    
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '123456789':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)


    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))


        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
       
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                if 'message' in message:
                    # Print the message to the terminal
                    recieved_messsage=message['message']['text']
                    print(recieved_messsage)

                    # ==================================
                    # integrate Wit.ai bot here
                    # ==================================
                    wit_response=client.message(recieved_messsage)
                    pprint(wit_response)

                    characteristics=get_xter(wit_response)


                    #define a functioln to generate response
                    


                    #GEt user details
                    fbid=message['sender']['id']
                    user_details_url = "https://graph.facebook.com/v2.6/{}".format(fbid)
                    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':'{}'.format(PAGE_ACCESS_TOKEN)}
                    user_details = requests.get(user_details_url, user_details_params).json()
 
                    message_to_be_sent=generate_response(characteristics, user_details)

                    print(message_to_be_sent)
                    #print user details
                    pprint(user_details)

                   

    				#Send Message
                    post_facebook_message(fbid, message_to_be_sent)  

        return HttpResponse()