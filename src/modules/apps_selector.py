from src.modules.llm_response_generator import LlmAppSelector
from src.util import LoadAppsInfo

class Selector:

    def __init__(self, selector_model = "LLM"):
        self.selector_model = selector_model
        self.apps_info = LoadAppsInfo()


    def detect(self, query):
        if self.selector_model == "LLM":
            apps = LlmAppSelector().generate_response(query, self.apps_info)
            return apps