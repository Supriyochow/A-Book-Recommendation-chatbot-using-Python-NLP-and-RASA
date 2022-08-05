# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.sparse import csr_matrix

from sklearn import model_selection, datasets
from sklearn.neighbors import NearestNeighbors
import joblib
import pickle

from Book_Recommendation import recommend_book
from Book_Genre_Extraction import genre_extract
import re

book_name=""
author_name=""
publisher_name=""


class ActionGreeting(Action):

    def name(self) -> Text:
         return "action_utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(image="https://c0.wallpaperflare.com/preview/806/354/362/assorted-reading-books.jpg")
        dispatcher.utter_message(text="Hello I am Marky\nWelcome to BookMe Chatbot\nHow can we help you today?",buttons= [{"payload":"/explore_books","title":"Explore Books"},{"payload":"/recommend_books","title":"Get Book Recommendation"}])

        return []



class ActionExploreBooks(Action):

    def name(self) -> Text:
         return "action_explore_books"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Choose the Genre you want to explore: ",buttons= [{"payload":"/recommend_books","title":"Fiction"},{"payload":"/recommend_books","title":"Thriller"},{"payload":"/recommend_books","title":"Romantic"}])

         return []




class ActionRecommendBooks(Action):

    def name(self) -> Text:
         return "action_recommend_books"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            dispatcher.utter_message(text="Please wait.... We are recommending..")
            li= recommend_book()
            #book_name=tracker.get_slot('book_name')
            dispatcher.utter_message(text="Hurrayyyy!! We got some books that you might like.....")
            for i in range(5):
                dispatcher.utter_message(image="{}".format(li["link"][i]))
                dispatcher.utter_message(text="Book Name: {0}\nAuthor: {1}\nPublisher: {2}".format(li["Name"][i],li["author"][i],li["publisher"][i]))
                
            return []


