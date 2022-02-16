from typing import Any, Text, Dict, List, Union, Optional
from dotenv import load_dotenv

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

import csv
import os

load_dotenv()

airtable_api_key=os.getenv("AIRTABLE_API_KEY")
base_id=os.getenv("BASE_ID")
table_name=os.getenv("TABLE_NAME")

def create_wine_log(confirm_suggestion, color, flavor, ):
    header = ['confirm_suggestion', 'color', 'flavor']
    data = [confirm_suggestion, color, flavor]

    with open('user_response.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerow(data)

class ValidateWineForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_wine_form"

    async def validate_confirm_suggestion(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
            return {"confirm_suggestion": False}
  

class ActionSubmitResults(Action):
    def name(self) -> Text:
        return "action_submit_results"
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

      
       confirm_suggestion = tracker.get_slot("confirm_suggestion")
       color = tracker.get_slot("color")
       flavor = tracker.get_slot("flavor")
       

       response = create_wine_log(
               confirm_suggestion=confirm_suggestion,
                color=color,
                flavor=flavor
            )

       dispatcher.utter_message("Thanks, your answers have been recorded!")
       return []