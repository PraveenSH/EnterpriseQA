from src.modules.llm_response_generator import LlmResponder

class Responder:

    def __init__(self):
        pass

    def respond(self, query, results):
        return LlmResponder().generate_response(query, results)