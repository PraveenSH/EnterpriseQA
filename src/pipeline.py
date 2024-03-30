from src.modules.apps_selector import Selector
from src.modules.tasks_detector import Detector
from src.modules.flow_creator import Creator
from src.modules.responder import Responder


def process(query):

    app_selector = Selector()
    task_detector = Detector()
    flow_creator = Creator()
    responder = Responder()


    relevant_apps = app_selector.detect(query)
    print("Data to be fetched from: ", relevant_apps)

    tasks = task_detector.detector(query, relevant_apps)
    print("The APIs to be executed: ", tasks)

    result_data = flow_creator.create_and_execute(query, tasks)
    print("Extracted all intermediate data: ", result_data)

    response = responder.respond(query, result_data)
    return response


if __name__ == "__main__":

    user_query = "what is sachin's salary?"
    resp = process(user_query)
    print(resp)
