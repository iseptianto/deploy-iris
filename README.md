
![Code_LlB8FEMM3E](https://github.com/user-attachments/assets/193b1dfd-2dda-471c-8dbc-0f58bc8c0f47)

# **Iris Classification Web App** 🌼

## **Project Description**  
This project is a **Flask-based web application** that utilizes **Machine Learning** to classify **Iris flowers**.  
Users can input flower features (sepal length, sepal width, petal length, and petal width), and the application will predict the Iris species based on a trained **classification model**.

## **Technologies Used**  
- Python (Flask, NumPy, Pandas, Pickle)  
- Bootstrap 5.3  
- Scikit-learn (Machine Learning Model)  

## **Installation**  
Make sure you have **Python** installed. Then, run the following command to install dependencies:  
```bash
pip install -r requirements.txt
```

## **How to Run the Application**  
1. Clone this repository to your computer:  
   ```bash
   git clone https://github.com/iseptianto/deploy-iris.git
   cd repository
   ```
2. Run the application using the following command:  
   ```bash
   python app.py
   ```
3. Open your browser and access **http://127.0.0.1:5000/** to start using the application.

## **Application Usage**  
- Enter the **sepal length and width** as well as the **petal length and width** in **centimeters**.  
- Click the **"Predict"** button to obtain the classification result for the Iris species.

## **Project Structure**  
```
│── static/
│   ├── style.css
│   ├── images/
│── templates/
│   ├── index.html
│── app.py
│── eden.pkl
│── requirements.txt
│── README.md
```
- `static/` → Folder for storing CSS files and images  
- `templates/` → Folder for storing HTML files  
- `app.py` → Flask backend file  
- `eden.pkl` → Trained Machine Learning model  
- `requirements.txt` → List of required libraries  

## **Machine Learning Model**  
The model used in this application is **[specify the classification method used, e.g., Logistic Regression or Random Forest]**, which was trained using the **Iris dataset**.

## **Contributions**  
If you would like to contribute to this project, please **fork** the repository and submit a **pull request**.  
All contributions, whether improving the code or enhancing features, are greatly appreciated! 🚀

