import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

def train_model():
    # Load data
    df = pd.read_csv('data/students.csv')
    
    X = df.drop('Performance', axis=1)
    y = df['Performance']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test_scaled)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))
    
    # Save model and scaler
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/student_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    
    # Save feature names for reference in API
    joblib.dump(X.columns.tolist(), 'models/feature_names.pkl')
    
    print("Model and scaler saved to models/")

if __name__ == "__main__":
    train_model()
