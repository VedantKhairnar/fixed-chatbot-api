import requests

# Define the base URL for the Flask API
base_url = 'http://127.0.0.1:5000/chatbot'

def test_main_menu():
    print("Testing main menu...")
    response = requests.post(base_url, json={"choice": "menu1"})
    response_data = response.json()

    assert response_data["question"] == "Please choose an option from menu1", f"Failed main menu test: {response_data['question']}"
    assert response_data["options"] == ["op1", "op2", "op3"], "Failed main menu options test"
    print("Main menu test passed.")
    return response_data

def test_option_1():
    print("Testing Option 1...")
    response = requests.post(base_url, json={"choice": "op1"})
    response_data = response.json()
    print("Response from Option 1:", response_data)
    assert response_data["question"] == "Please choose an option from op1", f"Failed Option 1 test: {response_data['question']}"
    assert response_data["options"] == ["op4", "op5"], "Failed Option 1 options test"
    print("Option 1 test passed.")
    return response_data

def test_option_1_1():
    print("Testing Option 1.1...")
    response = requests.post(base_url, json={"choice": "op4"})
    response_data = response.json()
    print("Response from Option 1.1:", response_data)
    assert response_data["answer"] == "You chose Option 4", f"Failed Option 1.1 test: {response_data['answer']}"
    assert response_data["options"] == ["Back to Main Menu"], "Failed Option 1.1 options test"
    print("Option 1.1 test passed.")
    return response_data

def test_back_to_main_menu():
    print("Testing back to main menu...")
    response = requests.post(base_url, json={"choice": "back"})
    response_data = response.json()
    print("Response from back to main menu:", response_data)
    assert response_data["question"] == "Please choose an option from menu1", f"Failed back to main menu test: {response_data['question']}"
    assert response_data["options"] == ["op1", "op2", "op3"], "Failed back to main menu options test"
    print("Back to main menu test passed.")
    return response_data

if __name__ == "__main__":
    test_main_menu()
    test_option_1()
    test_option_1_1()
    test_back_to_main_menu()
    print("All tests passed.")
