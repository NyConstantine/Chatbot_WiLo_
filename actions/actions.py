# from typing import Any, Text, Dict, List, Union, Optional
# from dotenv import load_dotenv
# 
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormValidationAction
# 
# import csv
# import os
# 
# load_dotenv()
# 
# airtable_api_key=os.getenv("AIRTABLE_API_KEY")
# base_id=os.getenv("BASE_ID")
# table_name=os.getenv("TABLE_NAME")
# 
# def create_wine_log( color, flavor, ):
#     header = [ 'color', 'flavor']
#     data = [ color, flavor]
# 
#     with open('user_response.csv', 'w', encoding='UTF8', newline='') as f:
#         writer = csv.writer(f)
# 
#         # write the header
#         writer.writerow(header)
# 
#         # write the data
#         writer.writerow(data)
# 
# class ValidateWineForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_wine_form"
#   
# 
# class ActionSubmitResults(Action):
#     def name(self) -> Text:
#         return "action_submit_results"
#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
# 
#       
# 
#        color = tracker.get_slot("color")
#        flavor = tracker.get_slot("flavor")
#        
# 
#        response = create_wine_log(
#                 color=color,
#                 flavor=flavor
#             )
# 
#        return []