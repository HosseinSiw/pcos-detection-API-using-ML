# PCOS Prediction Web App

This is a FastAPI web application that predicts the likelihood of Polycystic Ovary Syndrome (PCOS) based on input features like age, BMI, menstrual cycle data, testosterone levels, and antral follicle count. The model is trained using machine learning techniques and is served via a RESTful API, dataset from: <a href='https://www.kaggle.com/datasets/samikshadalvi/pcos-diagnosis-dataset'>Kaggle</a>

## Features

- **Prediction Endpoint**: A `GET` endpoint to predict PCOS based on the input features.
- **Input Parameters**: Users can provide the following parameters to make predictions:
  - `age`: Age of the person
  - `bmi`: Body Mass Index (BMI)
  - `menstrual`: Menstrual status (binary value, 0 or 1)
  - `testosterone`: Testosterone levels
  - `antral_follicle_count`: Antral follicle count (number of follicles in the ovaries)

## Requirements

Make sure you have the following installed:
- Python 3.7+
- FastAPI
- Uvicorn
- Joblib
- Numpy
- Sklearn

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd <your-project-folder>

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the application:
    ```bash
    cd web-app
    uvicorn main:app --reload

5. Access the api via your browser:
    Open your browser and go to http://127.0.0.1:8000.
    You can check the available routes at http://127.0.0.1:8000/docs (Swagger UI).

### Contributing
Feel free to fork the repository and submit pull requests. If you have any suggestions or improvements, open an issue or create a pull request.