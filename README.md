# 🤖 Flipkart Customer Support Query Classification

This project uses **Machine Learning + Natural Language Processing (NLP)** to automatically classify Flipkart customer support queries into:
- **Class 1** → Return/Refund/Cancellation related  
- **Class 0** → Other queries (order status, payment, product info, etc.)

The goal is to **automate ticket routing**, reduce manual support load, and improve customer response times.

---

## 🎯 Project Objective

- Build a binary classification model using customer support text data  
- Apply TF-IDF for vectorization  
- Use Logistic Regression for classification  
- Save the trained model and deploy it via **Streamlit app**

---

## 🧾 Dataset

**File**: `Customer_support_data.csv`  
- Contains customer messages and issue categories  
- Preprocessed to generate a `binary_label` column (1 = return-related, 0 = other)

---

## 🛠️ Technologies Used

- Python 🐍  
- Pandas, NumPy  
- Scikit-learn (TF-IDF, Logistic Regression, Model Evaluation)  
- Joblib (model saving)  
- Streamlit (optional deployment)

---

## 📊 Steps Covered

- ✅ Text cleaning & preprocessing  
- ✅ TF-IDF vectorization  
- ✅ Feature scaling (for numerical features)  
- ✅ Model training (Logistic Regression)  
- ✅ Hyperparameter tuning using GridSearchCV  
- ✅ Model evaluation (accuracy, precision, recall, F1-score)  
- ✅ Model saving using `joblib`  
- ✅ Predict on unseen test queries  
- ✅ Deployment-ready setup via `app.py`

---

## 🚀 How to Run

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/your-username/flipkart-support-query-classification.git
cd flipkart-support-query-classification
````

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 3. Run the Notebook

Open and run `Flipkart_Customer_Support_Classification.ipynb` in Jupyter or Colab.

### 🔹 4. Streamlit App (Optional)

```bash
streamlit run app.py
```

---

## 📦 Files Included

* `Flipkart_Customer_Support_Classification.ipynb` — Full notebook (ML + Results)
* `Customer_support_data.csv` — Dataset (or sample if private)
* `model.pkl` — Trained ML model
* `vectorizer.pkl` — TF-IDF vectorizer
* `label_encoder.pkl` — Binary label encoder
* `app.py` — Streamlit app for real-time prediction

---

## 🧪 Example Queries

| Input Message                                 | Predicted Class    |
| --------------------------------------------- | ------------------ |
| I want to return my damaged order             | 1 (Return-related) |
| When will my product be delivered?            | 0 (Other)          |
| How do I cancel and get a refund?             | 1 (Return-related) |
| The payment failed but the money was deducted | 0 (Other)          |

---

## ✅ Conclusion

This project shows how Machine Learning can automate real-world customer support tasks in e-commerce. It helps streamline operations, reduce support delays, and boost customer satisfaction.

---

## 👨‍💻 Author

**\Prathmesh Nitnaware**
Beginner in AI/ML
📬 Feel free to connect or contribute!

```
