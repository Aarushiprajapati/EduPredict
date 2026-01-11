# EduPredict 🎓

**EduPredict** is an intelligent early warning system designed to analyze student academic performance. By leveraging Machine Learning, it identifies at-risk students based on attendance, study habits, and previous scores, providing actionable suggestions to improve their academic outcomes.

## 🚀 Features

*   **Real-time Prediction**: Instantly categorizes performance as "Excellent", "Average", or "At-Risk".
*   **Smart Suggestions**: Provides tailored advice based on specific input metrics (e.g., "Increase attendance", "Sleep more").
*   **Interactive Dashboard**: A beautiful, glassmorphic user interface for easy data entry and visualization.
*   **Production Ready**: Built with FastAPI and configured for seamless deployment on platforms like Render.

## 🛠️ Tech Stack

*   **Backend**: Python, FastAPI, Scikit-learn, Pandas, NumPy
*   **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism), JavaScript
*   **Machine Learning**: Random Forest Classifier

## 📦 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Aarushiprajapati/EduPredict.git
    cd EduPredict
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python -m uvicorn app.backend.main:app --reload
    ```

4.  **Access the Dashboard:**
    Open your browser and visit: `http://127.0.0.1:8000`

## ☁️ Deployment

This project includes a `render.yaml` blueprint. To deploy:

1.  Push this code to your GitHub repository.
2.  Log in to [Render](https://render.com).
3.  Create a new **Blueprint** service and link your repository.
4.  Render will automatically build and deploy the app.

## 📂 Project Structure

```
EduPredict/
├── app/
│   ├── backend/    # FastAPI server logic
│   └── frontend/   # User Interface (HTML/CSS/JS)
├── data/           # Synthetic datasets
├── models/         # Trained ML models (.pkl)
├── scripts/        # Training and data generation scripts
├── requirements.txt
└── render.yaml
```

---
*Created by [Aarushi Prajapati](https://github.com/Aarushiprajapati)*
