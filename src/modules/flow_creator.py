from src.mock_apis.hr_apis import HrDatabse
from src.mock_apis.payroll_apis import PayrollDatabse
from src.modules.llm_response_generator import LlmParameterExtractor

class Creator:

    def __init__(self):

        hr_apis = HrDatabse()
        payroll_apis = PayrollDatabse()

        self.available_apis = {
            "get_employee_name": hr_apis.get_employee_name,
            "get_employee_id": hr_apis.get_employee_id,
            "get_manager_name": hr_apis.get_manager_name,
            "get_manager_id": hr_apis.get_manager_id,
            "get_comp": payroll_apis.get_comp,
            "get_total_comp": payroll_apis.get_total_comp
        }


    def extract_parameters(self, query, api, extracted_data):
        parameter = LlmParameterExtractor().generate_response(query, api, extracted_data)
        return parameter


    def create_and_execute(self, query, apis):

        extracted_data = {}

        for api in apis:
            param = self.extract_parameters(query, api, extracted_data)
            result = self.available_apis[api](param)

            extracted_data.update(result)
        return extracted_data