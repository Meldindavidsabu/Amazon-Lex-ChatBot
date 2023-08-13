import json

def lambda_handler(event, context):
    intent = event['currentIntent']['name']
    slots = event['currentIntent']['slots']

    if intent == 'OrderFoodIntent':
        food_type = slots['FoodType']
        food_choice = slots['FoodChoice']

        if food_choice == 'Pizza':
            price = 143
            response = f"Your order costs ₹ {price}. Cash on delivery is available. Thank you for choosing us!"
        else:
            response = "Sorry, we currently offer only Pizza as an option."

        return {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "T",
                    "content": response
                }
            }
        }
