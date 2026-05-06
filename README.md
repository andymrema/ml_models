#  Tanzania Water Pump Functionality Prediction

> *Can data science save lives? I think so.*

A machine learning project that predicts whether water pumps across Tanzania are **functional or non-functional** — built by a year 2 data science student, using real data, solving a real problem.

---

## 🌍 Why This Project?

Millions of Tanzanians depend on water pumps for clean water every day. When a pump fails and no one knows until it's too late, entire communities suffer.

I wanted to use data science to answer one question:

**Can we predict which pumps will fail — before they do?**

This project is my attempt to answer that. It's not just a school assignment. It's about my country, my people, and what data can do when it's pointed at something that matters.

---

## 🤖 What the Model Does

The model takes in features about a water pump — its age, installer, water quality, location, and more — and predicts one of two outcomes:

| Prediction | Meaning |
|---|---|
| ✅ Functional | The pump is working fine |
| ❌ Non-Functional | The pump has failed or needs repair |

---

## 🧠 Machine Learning Approach

| Component | Details |
|---|---|
| Algorithm | Decision Tree Classifier |
| Encoding | Label Encoding for categorical variables |
| Model Persistence | Joblib (.pkl format) |
| Deployment | Streamlit Community Cloud |

### Steps performed:
1. Data exploration and understanding
2. Handling missing values
3. Encoding categorical features
4. Training the Decision Tree model
5. Saving the trained model with Joblib
6. Building an interactive Streamlit app for live predictions

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-lightblue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)

- Python
- Pandas & NumPy
- Scikit-learn
- Joblib
- Streamlit

---

## 📂 Project Structure

```
tanzania-water-pump-prediction/
│
├── app.py                  # Streamlit web application
├── models/
│   ├── pump_model.pkl      # Trained Decision Tree model
│   ├── encoders_X.pkl      # Feature encoders
│   ├── feature_columns.pkl # Feature column order
│   └── le_Y.pkl            # Target label encoder
├── requirements.txt        # Dependencies
└── README.md
```

---

## 🚀 Run It Locally

```bash
# Step 1: Clone the repo
git clone https://github.com/andymrema/tanzania-water-pump-prediction.git

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the app
streamlit run app.py
```

---

## 🌐 Live Demo

👉 **[Try the live app here](https://mlproject-jabjhfbfb2zfckuvuk5zkd.streamlit.app/)**

Enter pump details and get an instant prediction on whether it's functional or not.

---

## 📈 What I Learned

- How to work with real-world, messy data
- The importance of encoding categorical variables correctly
- How to deploy a machine learning model as a web app
- That data science is most powerful when it solves real problems

---

## 🙋‍♂️ About Me

Hi, I'm **Andy Mrema** Data Science student from Tanzania, building real-world projects and sharing everything I learn.

I believe data science shouldn't be locked behind complexity. I'm on a mission to make it accessible to beginners while using it to solve African problems.

📸 Follow my journey on Instagram: [@andywithdata](https://www.instagram.com/andywithdata)
💻 More projects: [github.com/andymrema](https://github.com/andymrema)

---

*If this project inspired you or helped you learn something — leave a ⭐ on the repo. It means a lot!*
