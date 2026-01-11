import requests
import json
import time
import sys

def test_api():
    url = "http://localhost:8000/predict"
    
    # Test Case 1: At-Risk Student
    # Low attendance, low study hours, low previous scores
    data_risk = {
        "Attendance": 50.0,
        "Study_Hours": 2.0,
        "Previous_Scores": 55.0,
        "Sleep_Hours": 6.0,
        "Extracurricular": 0
    }
    
    print("\nTesting Case 1: At-Risk Student...")
    try:
        response = requests.post(url, json=data_risk)
        if response.status_code == 200:
            result = response.json()
            print("Response:", json.dumps(result, indent=2))
            if result['status'] == 'At-Risk':
                print("✅ Correctly identified as At-Risk")
            else:
                print(f"❌ Incorrect classification: {result['status']}")
        else:
            print(f"❌ Request failed with status code {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"❌ Connection failed: {e}")

    # Test Case 2: Excellent Student
    # High attendance, high study hours, high previous scores
    data_excellent = {
        "Attendance": 95.0,
        "Study_Hours": 8.0,
        "Previous_Scores": 90.0,
        "Sleep_Hours": 8.0,
        "Extracurricular": 1
    }
    
    print("\nTesting Case 2: Excellent Student...")
    try:
        response = requests.post(url, json=data_excellent)
        if response.status_code == 200:
            result = response.json()
            print("Response:", json.dumps(result, indent=2))
            if result['status'] == 'Excellent':
                print("✅ Correctly identified as Excellent")
            else:
                print(f"❌ Incorrect classification: {result['status']}")
        else:
            print(f"❌ Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    # Wait a bit for server to start if running immediately after startup
    print("Waiting for server to ensure it is up...")
    time.sleep(2) 
    test_api()
