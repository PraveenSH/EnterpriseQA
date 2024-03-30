
class MockData:

    all_employee_names = ["smit", "john", "sachin", "praveen", "james", "steve"]
    all_employee_ids = ["id_0", "id_1", "id_2", "id_3", "id_4", "id_5"]

    hr_data = [
                {"emp_id": "id_0", "emp_name": "smit", "manager_id": "NONE"},
                {"emp_id": "id_1", "emp_name": "john", "manager_id": "id_0"},
                {"emp_id": "id_2", "emp_name": "sachin", "manager_id": "id_0"},
                {"emp_id": "id_3", "emp_name": "praveen", "manager_id": "id_1"},
                {"emp_id": "id_4", "emp_name": "james", "manager_id": "id_2"},
                {"emp_id": "id_5", "emp_name": "steve", "manager_id": "id_2"}
    ]

    payroll_data = [
                {"emp_id": "id_0", "comp": "500000"},
                {"emp_id": "id_1", "comp": "260000"},
                {"emp_id": "id_2", "comp": "265000"},
                {"emp_id": "id_3", "comp": "200000"},
                {"emp_id": "id_4", "comp": "195000"},
                {"emp_id": "id_5", "comp": "205000"}
    ]