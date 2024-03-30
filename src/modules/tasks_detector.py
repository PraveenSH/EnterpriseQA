from src.util import LoadTasksInfo
from src.modules.llm_response_generator import LlmTaskDetector

class Detector:

    def __init__(self, detector_model = "LLM"):
        self.detector_model = detector_model
        self.task_info = LoadTasksInfo()


    def detector(self, query, seleted_apps):
        if self.detector_model == "LLM":
            tasks = LlmTaskDetector().generate_response(query, self.task_info, seleted_apps)
            return tasks