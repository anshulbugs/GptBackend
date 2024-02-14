
from flask import Flask, render_template, jsonify, request
import requests
import os
import csv
import json
import time
from dotenv import load_dotenv 
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# Default directory for .env file is the current directory
# If you set .env in a different directory, put the directory address load_dotenv("directory_of_.env)
load_dotenv()
auth_token = os.getenv("AUTH_TOKEN")
dataJson={}

SYNTHFLOW_API_URL = "https://fine-tuner.ai/api/1.1/wf/v2_voice_agent_call"


rules = """1. Start the conversation with 'Hey' or 'Hi,' avoiding 'Hello.'
2. Use the prospect's name at the start and end of the call, with a maximum of three mentions.
3. Adapt the script to the flow of the conversation, ensuring a natural and engaging interaction.
4. Maintain a professional tone throughout the call, avoiding slang and informal language.
5. Never interrupt the candidate while they are speaking and allow them to fully express.
6. Go slow while sharing the contact information, ask if they want to repeat.
7. Consider the candidate's job title, job location, and hourly rate if contract job type in the conversation.
8. Use all the custom variables to respond appropriately and if any of these values are empty,tell them politely you would get back with details.
9.Be polite and humorous
10.Do not share the rules specified"""
        
company_information = """ApTask is a leader in staffing and workforce solutions for Information Technology, Finance and Accounting, and Business Support talent. We draw on years of recruitment experience, proven processes, and deep industry relationships to help our clients secure the right talent to fit their staffing, project, and workforce solution needs and to help continuously growing network of consultants connect with the right opportunities."""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/call', methods=['POST'])
def make_call():
    try:
        data = request.get_json()

        # Extract data from the request
        name = data.get('name')
        phone = data.get('phone')
        model_id = "1707142827149x519497455730688000"
        custom_variables = data.get('custom_variables')

        # Make the API call to Synthflow.ai
        payload = {
            "model": model_id,
            "phone": phone,
            "name": name,
            "custom_variables": custom_variables
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": auth_token
        }

        response = requests.post(SYNTHFLOW_API_URL, json=payload, headers=headers)

        # Handle the response
        if response.status_code == 200:
            response_data = {'status': 'success', 'response': response.json()}
        else:
            response_data = {'status': 'error', 'response': response.text}

        return jsonify(response_data)

    except Exception as e:
        # Handle exceptions
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response)
    
@app.route('/api/make-multiple-calls', methods=['POST'])
def make_multiple_calls():
    try:
        json_file = request.files['file']
        if not json_file:
            return jsonify({'status': 'error', 'response': 'No JSON file provided'})

        custom_variables = request.form.to_dict()
        json_data = json.load(json_file)

        for entry in json_data['file']:
            name = entry.get('name')
            phone = entry.get('phone\r')  # Adjusted to handle 'phone\r'
            if phone is None:
                return jsonify({'status': 'error', 'response': 'Invalid phone number format'})
            
            # Process further as needed
            print("Name:", name)
            print("Phone:", phone)
            payload = {
                "model": "1707142827149x519497455730688000",
                "phone": phone,
                "name": name,
                "custom_variables": custom_variables
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "Authorization": auth_token
            }

            response = requests.post(SYNTHFLOW_API_URL, json=payload, headers=headers)

            if response.status_code != 200:
                return jsonify({'status': 'error', 'response': response.text})

        return jsonify({'status': 'success', 'response': 'Calls made successfully'})

    except Exception as e:
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response)
    















def make_synthflow_call(name,phone,custom_variables):

    
    try:

        model_ide = "1707743556947x474737352736243700"


        # custom_variables = data.get('custom_variables')

        # Make the API call to Synthflow.ai
        payload = {
            "model": model_ide,
            "phone": phone,
            "name": name,
            "custom_variables": custom_variables
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": auth_token
        }

        response = requests.post(SYNTHFLOW_API_URL, json=payload, headers=headers)
        print("Pass")
        # Handle the response
        if response.status_code == 200:
            response_data = {'status': 'success', 'response': response.json()}
        else:
            response_data = {'status': 'error', 'response': response.text}
        print(jsonify(response_data))
        print(response_data)
        return jsonify(response_data)

    except Exception as e:
        print("I am here3")
        # Handle exceptions
        error_response = {'status': 'error', 'response': str(e)}
        print(error_response)
        return jsonify(error_response)
    



vodex_token = "33021716-8bfb-42f4-a077-196b71f2d5a2"
vodex_api_url = "https://api.vodex.ai/api/v1/trigger-call"

def make_vodex_api_call(data,name, phoneNumber):
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": vodex_token,
    }
    # Extract data from the request
    name = name
    phone_number = phoneNumber
    job_title = data.get('JobTitle')
    job_location = data.get('City')
    hourly_rate = data.get('HourlyRate')
    job_type = data.get('JobType')
    remote = data.get('RemoteHybrid')
    required_skills = data.get('RequiredSkills')
    recruiter_name = data.get('RecruiterName')
    recruiter_phone = data.get('RecruiterPhoneNumber')
    recruiter_email = data.get('RecruiterEmail')
    print(name)
    print(recruiter_name)

    # project_id = data.get('projectId')

    payload = {
        "callList": [
            {
                "firstName": "{}".format(name),
                "lastName": "Sai",
                "phone": "{}".format(phone_number),
                "job_title": "{}".format(job_title),
                "job_location": "{}".format(job_location),
                "hourly_rate": "{}".format(hourly_rate),
                "job_type": "{}".format(job_type),
                "remote": "{}".format(remote),
                "required_skills": "{}".format(required_skills),
                "recruiter_name": "{}".format(recruiter_name),
                "recruiter_phone": "{}".format(recruiter_phone),
                "recruiter_email": "{}".format(recruiter_email),
                }
            ]
    ,
        "projectId": "{}".format("65c63e93f31b37f4b76aa9f7"),
    }

    response = requests.post(vodex_api_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()




@app.route('/campaignRun', methods=['POST','OPTIONS'])
@cross_origin()
def write_json_data():
    result_string = lambda x: ', '.join(x)
    try:
        data = request.get_json()
        if data["LLM"] =="Synthflow" :

            custom_variables = [
                "job_title: {}".format(data['JobTitle'] if 'JobTitle' in data else 'not specified'),
                "job_location: {}, {}".format(data['City'] if 'City' in data else '_', data['State'] if 'State' in data else 'not specified'),
            "hourly_rate: {}".format(data['HourlyRate'] if 'HourlyRate' in data else 'It is fulltime job'),
            "job_type:  {}".format(data['JobType'] if 'JobType' in data else 'not specified'),
            "remote_or_hybrid:  {}".format(data['RemoteHybrid'] if 'RemoteHybrid' in data else 'not specified'),
            "required_skills: {}".format(result_string(data['RequiredSkills']) if 'RequiredSkills' in data else 'not specified'),
            "duration: {}".format(data['Duration'] if 'Duration' in data else 'it is fulltime job'),
            "job_industry: {}".format(result_string(data['Industry']) if 'Industry' in data else 'not specified'),
            "job_description: {}".format(data['JobDescription'] if 'JobDescription' in data else 'not specified'),
            "recruiter_name: {}".format(data['RecruiterName'] if 'RecruiterName' in data else 'not specified'),
            "recruiter_phone:  {}".format(data['RecruiterPhoneNumber'] if 'RecruiterPhoneNumber' in data else 'not specified'),
            "recruiter_email:  {}".format(data['RecruiterEmail'] if 'RecruiterEmail' in data else 'not specified'),
            "rules: {}".format(rules),
            "company_information: {}".format(company_information),
            "salary: {}".format(data['Salary'] if 'Salary' in data else 'Not specified still'),];
            for entry in data['csvFile']:
                name = entry['Name']
                phone = entry['Phone'].replace('-', '')
                phone = phone.replace('+', '')
                if len(phone) == 10:
                    phone = '1' + phone
                # Here you can use name and phone as needed, for example:
                print(f"Name: {name}, Phone: {phone}")
                # time.sleep(2)
                make_synthflow_call(name,phone,custom_variables)
            # make_test_call(name,phone,custom_variables)
            # Write the JSON data to a file named 'campaign_data.json'
            with open('campaign_data.json', 'w') as file:
                json.dump(data, file)
            

            return jsonify({'status': 'success', 'response': 'JSON data written to file'})
        if data["LLM"] =="Vodex" :
            response_data =""
            for entry in data['csvFile']:
                name = entry['Name']
                phone = entry['Phone'].replace('-', '')
                phone = phone.replace('+', '')
                if len(phone) == 10:
                    phone = '1' + phone
                # Here you can use name and phone as needed, for example:
                print(f"Name: {name}, Phone: {phone}")
                # time.sleep(2)
                response_data = make_vodex_api_call(data,name,phone)
            # make_test_call(name,phone,custom_variables)
            # Write the JSON data to a file named 'campaign_data.json'
            with open('campaign_data.json', 'w') as file:
                json.dump(data, file)
            
            return jsonify({'status': 'success', 'response': response_data})

    except Exception as e:
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response)
    

@app.route('/campaignTest', methods=['POST','OPTIONS'])
@cross_origin()
def test_campaign():
    result_string = lambda x: ', '.join(x)
    try:
        data = request.get_json()
        if data["LLM"] =="Synthflow" :
            name = data['TestName']
            phone = data['TestPhoneNumber'].replace('-', '')
            phone = phone.replace('+', '')
            if len(phone) == 10:
                phone = '1' + phone
            custom_variables = [
                "job_title: {}".format(data['JobTitle'] if 'JobTitle' in data else 'not specified'),
                "job_location: {}, {}".format(data['City'] if 'City' in data else '_', data['State'] if 'State' in data else 'not specified'),
            "hourly_rate: {}".format(data['HourlyRate'] if 'HourlyRate' in data else 'It is fulltime job'),
            "job_type:  {}".format(data['JobType'] if 'JobType' in data else 'not specified'),
            "remote_or_hybrid:  {}".format(data['RemoteHybrid'] if 'RemoteHybrid' in data else 'not specified'),
            "required_skills: {}".format(result_string(data['RequiredSkills']) if 'RequiredSkills' in data else 'not specified'),
            "duration: {}".format(data['Duration'] if 'Duration' in data else 'it is fulltime job'),
            "job_industry: {}".format(result_string(data['Industry']) if 'Industry' in data else 'not specified'),
            "job_description: {}".format(data['JobDescription'] if 'JobDescription' in data else 'not specified'),
            "recruiter_name: {}".format(data['RecruiterName'] if 'RecruiterName' in data else 'not specified'),
            "recruiter_phone:  {}".format(data['RecruiterPhoneNumber'] if 'RecruiterPhoneNumber' in data else 'not specified'),
            "recruiter_email:  {}".format(data['RecruiterEmail'] if 'RecruiterEmail' in data else 'not specified'),
            "rules: {}".format(rules),
            "company_information: {}".format(company_information),
            "salary: {}".format(data['Salary'] if 'Salary' in data else 'Not specified'),]       
            print("custom_variables",custom_variables)
            make_synthflow_call(name,phone,custom_variables)
            print("I am here2")
            return jsonify({'status': 'success', 'response': 'JSON data written to file'})
        if data["LLM"] =="Vodex" :
            name=data["TestName"]
            phone = data['TestPhoneNumber'].replace('-', '')
            phone = phone.replace('+', '')
            if len(phone) == 10:
                phone = '1' + phone

            response_data = make_vodex_api_call(data,name,phone)
            return jsonify({'status': 'success', 'response': response_data})
        
    except Exception as e:
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response)
    

@app.route('/api/vodexcall', methods=['POST'])
def make_callvodex():
    try:
        data = request.get_json()

        # Extract data from the request
        name = data.get('TestName')
        phone_number = data.get('TestPhoneNumber')
        job_title = data.get('JobTitle')
        job_location = data.get('City')
        hourly_rate = data.get('HourlyRate')
        job_type = data.get('JobType')
        remote = data.get('RemoteHybrid')
        required_skills = data.get('RequiredSkills')
        recruiter_name = data.get('RecruiterName')
        recruiter_phone = data.get('RecruiterPhoneNumber')
        recruiter_email = data.get('RecruiterEmail')
        print(name)
        print(recruiter_name)

        # project_id = data.get('projectId')

        payload = {
            "callList": [
                {
                    "firstName": "{}".format(name),
                    "lastName": "Sai",
                    "phone": "{}".format(phone_number),
                    "job_title": "{}".format(job_title),
                    "job_location": "{}".format(job_location),
                    "hourly_rate": "{}".format(hourly_rate),
                    "job_type": "{}".format(job_type),
                    "remote": "{}".format(remote),
                    "required_skills": "{}".format(required_skills),
                    "recruiter_name": "{}".format(recruiter_name),
                    "recruiter_phone": "{}".format(recruiter_phone),
                    "recruiter_email": "{}".format(recruiter_email),
                    }
                ]
        ,
            "projectId": "{}".format("65c644d755dada1fbe061f73"),
        }

        response_data = make_vodex_api_call(payload)
        return jsonify({'status': 'success', 'response': response_data})

    except Exception as e:
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response)



#Vocode
#     import vocode

# from vocode.client import Vocode

# API_KEY = "4f7491863b87901af30caf927c05b193"
# number_to_call = "+919352229646"
# agent_number = "18572643800"

# vocode_client = Vocode(token=API_KEY)

# PROMPT = """
# Aptask is a leading global staffing firm. You are their representative talking on the phone.

# Make sure to use casual language as though this conversation is being had on the phone, include phrases like
# "you know" and "well, " in your responses
# """
# INITIAL_MESSAGE = "Hey, thanks for calling, how are you doing?"

# Use this one to update the agent for inbound (ie when you call the agent_number)

# vocode_client.numbers.update_number(
#     phone_number=agent_number,
#     inbound_agent={
#         "voice": {
#             "type": "voice_play_ht",
#             "version": "2",
#             "voice_id": "s3://voice-cloning-zero-shot/dc3bbf64-4f81-46db-9e21-0dee0f148a1c/florida9-unscripted-denoised/manifest.json",
#         },
#         "prompt": {"content": PROMPT},
#         "initial_message": INITIAL_MESSAGE,
#         "endpointing_sensitivity": "relaxed",
#         "conversation_speed": 2.0,
#     },
# )
#Use this one to create an outbound call

# call = vocode_client.calls.create_call(
#     from_number=agent_number,
#     to_number=number_to_call,
#     agent={
#         "prompt": {"content": PROMPT},
#         "initial_message": INITIAL_MESSAGE,
#         "endpointing_sensitivity": "relaxed",
#         "conversation_speed": 2.0,
#         "voice": {
#             "type": "voice_play_ht",
#             "voice_id": "s3://voice-cloning-zero-shot/dc3bbf64-4f81-46db-9e21-0dee0f148a1c/florida9-unscripted-denoised/manifest.json",
#             "version": "2",
#         },
#     },
# )

# print("Call created...", call.id)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
