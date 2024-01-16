# import string
# import random

# def prompt_yes_no(question):
#     """ Helper function to prompt for a yes/no answer """
#     while True:
#         answer = input(question + " (y/n): ").lower()
#         if answer in ['y', 'n']:
#             return answer == 'y'
#         else:
#             print("Please enter 'y' for yes or 'n' for no.")

# def get_user_preferences():
#     """ Function to get user preferences for password generation """
#     length = int(input("Enter the desired length of the password: "))
#     use_uppercase = prompt_yes_no("Include uppercase letters?")
#     use_lowercase = prompt_yes_no("Include lowercase letters?")
#     use_digits = prompt_yes_no("Include digits?")
#     use_punctuation = prompt_yes_no("Include special characters (punctuation)?")
#     return length, use_uppercase, use_lowercase, use_digits, use_punctuation

# def generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation):
#     """
#     Generate a random password based on user preferences.
#     """
#     characters = ''
#     if use_uppercase:
#         characters += string.ascii_uppercase
#     if use_lowercase:
#         characters += string.ascii_lowercase
#     if use_digits:
#         characters += string.digits
#     if use_punctuation:
#         characters += string.punctuation

#     if characters == '':
#         return "No characters selected for password generation!"

#     return ''.join(random.choice(characters) for _ in range(length))

# # Main program
# def generate():
#     length, use_uppercase, use_lowercase, use_digits, use_punctuation = get_user_preferences()
#     password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation)

#     res = {
#         "status" : 200,
#         "body" : password
#     }

#     return res
   
# # print("Generated Password:", password)

import uuid
from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=['GET', 'POST'])
def generate():
    randompw = uuid.uuid4()

    res = {
        "status" : 200, 
        "body" : randompw
    }

    return res

if __name__ == '__main__':
    app.run()

# print(randompw)