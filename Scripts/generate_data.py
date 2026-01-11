import pandas as pd
import numpy as np
import os

def generate_student_data(num_students=1000):
    np.random.seed(42)
    
    # Features
    attendance = np.random.uniform(60, 100, num_students)
    study_hours = np.random.uniform(1, 10, num_students)
    previous_scores = np.random.uniform(40, 100, num_students)
    sleep_hours = np.random.uniform(4, 9, num_students)
    extracurricular = np.random.choice([0, 1], num_students)
    
    # Target variable (Performance)
    # Logic: higher attendance, study hours, and previous scores lead to better performance
    # Noise: add some randomness
    noise = np.random.normal(0, 5, num_students)
    
    # Calculate a score
    performance_score = (
        0.3 * attendance + 
        0.4 * (study_hours * 10) + 
        0.3 * previous_scores + 
        noise
    )
    
    # Classify performance
    # 0: At-Risk (< 60)
    # 1: Average (60 - 80)
    # 2: Excellent (> 80)
    performance_cat = []
    for score in performance_score:
        if score < 70:
            performance_cat.append(0) # At-Risk
        elif score < 85:
            performance_cat.append(1) # Average
        else:
            performance_cat.append(2) # Excellent
            
    df = pd.DataFrame({
        'Attendance': attendance,
        'Study_Hours': study_hours,
        'Previous_Scores': previous_scores,
        'Sleep_Hours': sleep_hours,
        'Extracurricular': extracurricular,
        'Performance': performance_cat
    })
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/students.csv', index=False)
    print(f"Generated {num_students} student records in data/students.csv")

if __name__ == "__main__":
    generate_student_data()
