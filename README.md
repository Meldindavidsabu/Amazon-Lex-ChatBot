# Amazon-Lex-ChatBot
A simple chatbot using Amazon Lex

Amazon Lex Food Delivery Chatbot

This repository contains the code for an Amazon Lex chatbot designed for a food delivery app. The chatbot enables users to place food orders through a conversational interface. It recognizes user intents for ordering non-vegetarian, vegetarian, or vegan food, and guides users through selecting their preferred food choice. 

Step 1: Create Amazon Lex Bot

Log in to your AWS account.
Go to the Amazon Lex service.
Click the "Create" button to make a new bot.
Choose the "Custom bot" option.
Name your bot, select a voice (if applicable), and set the session timeout.
Create an intent called "OrderFoodIntent" for food ordering.
Add example phrases like "I want to order non vegetarian food," "Vegetarian food options," and "Vegan food menu."
Define slots like "FoodType" (non-veg, veg, vegan) and "FoodChoice" (pizza, burger, etc.).

Step 2: Create Lambda Function for Intent Fulfillment

1. Create a new Lambda function called "OrderFoodFunction."
2. Write code in the function to handle intent fulfillment.


Follow the prompts to interact with the Lex bot for food ordering.
The call will go through the contact flow and interact with the Lex bot.
Remember that this is a simplified explanation, and you may need to tailor the steps to your specific use case. Feel free to adapt the code, configuration, and flow to match your requirements. This project demonstrates how to create a basic food ordering chatbot integrated with Amazon Connect for a call center experience.

Note:
This chatbot is intended for demonstration purposes and serves as a foundation for building more complex conversational interfaces. Feel free to customize and expand upon it according to your specific requirements.








