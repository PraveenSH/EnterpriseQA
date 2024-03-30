from openai import OpenAI
from abc import ABC, abstractmethod
import json
from src.util import LoadTasksInfo
from data.mock_app_data import MockData


class LlmResponseGenerator(ABC):

    def __init__(self):
        api_key = ""
        self.client = OpenAI(api_key=api_key)


    def get_response(self, prompt):
        try:
            chat_completion = self.client.chat.completions.create(messages=[{"role": "user",
                                                                        "content": prompt,
                                                                        }],
                                                             model="gpt-3.5-turbo-1106",
                                                             temperature=0.3)
            return chat_completion.choices[0].message.content

        except Exception as e:
            print("This error occurred: ", e)
            return None


    @abstractmethod
    def generate_response(self):
        pass


class LlmAppSelector(LlmResponseGenerator):

    def generate_response(self, query, info_data):

        prompt = "Below are name of applications and information about their content in the json format." \
                 + json.dumps(info_data) \
                 + "\n Identify all the relevant applications needed. Return all the required apps for a given query: " + query
        response = self.get_response(prompt)
        selected_apps = []
        for app in info_data.keys():
            if app in response:
                selected_apps.append(app)

        return selected_apps

class LlmTaskDetector(LlmResponseGenerator):

    def generate_response(self, query, tasks_info, selected_apps):

        relevant_tasks = {}
        relevant_apis = []

        for app in selected_apps:
            relevant_tasks[app] = tasks_info[app]
            for api in relevant_tasks[app].keys():
                relevant_apis.append(api)

        # return ["get_manager_name"]
        prompt = "Below are name of applications, their APIs and information about what those APIs can do in json format." \
                 + json.dumps(relevant_tasks) \
                 + " Return the correct APIs to be executed for the given query: " + query
        response = self.get_response(prompt)

        selected_tasks = []

        for api in relevant_apis:
            if api in response:
                selected_tasks.append(api)
        '''
        for word in response.split():
            if word in relevant_apis:
                selected_tasks.append(word)
        '''

        return selected_tasks


class LlmParameterExtractor(LlmResponseGenerator):

    def generate_response(self, query, api, extracted_data):

        task_info = LoadTasksInfo()
        api_info = {}

        for app_key in task_info.keys():
            for key in task_info[app_key]:
                if key == api:
                    api_info[api] = task_info[app_key][key]

        prompt = "Below are name of applications, their APIs and information about what those APIs can do in json format." \
                 + json.dumps(api_info) \
                 + "\n I need to execute the API " + api \
                 + "\n Extract the correct parameter required to execute this API from the given query: " + query \
                 + "\n If required parameters are already computed and stored, return it from the json: " + json.dumps(
            extracted_data)

        response = self.get_response(prompt)

        for name in MockData.all_employee_names:
            if name in response:
                return name

        for eid in MockData.all_employee_ids:
            if eid in response:
                return eid

        return "parameter not found"


class LlmResponder(LlmResponseGenerator):

    def generate_response(self, query, results):
        prompt = "Below is the extracted data in json format for a user query." \
                 + json.dumps(results) \
                 + "\n This is the user orignal query: " + query \
                 + "\n Respond to query with the correct answer from the extracted data above."

        response = self.get_response(prompt)
        return response