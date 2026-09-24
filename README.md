# Customer Segmentation Web App

A Machine Learning-based **Customer Segmentation Web Application** that groups customers into meaningful segments based on their characteristics and purchasing behavior.

The project uses **K-Means Clustering** to identify customer groups and provides an interactive web interface built with **Flask**.

---

## 📌 Project Overview

Customer segmentation is the process of dividing customers into groups with similar characteristics or behaviors.

This project uses unsupervised machine learning to automatically identify customer segments. Businesses can use these segments to better understand their customers and design targeted marketing strategies.

### Key Features

* Customer segmentation using **K-Means Clustering**
* Data preprocessing and feature selection
* Interactive Flask web application
* Customer segment prediction
* Visual representation of customer groups
* Machine Learning model integration with the web application
* Deployable on AWS

---

## 🧠 Machine Learning Approach

The project follows the following workflow:

```text
Customer Dataset
       ↓
Data Preprocessing
       ↓
Feature Selection
       ↓
Feature Scaling
       ↓
K-Means Clustering
       ↓
Customer Segments
       ↓
Flask Web Application
       ↓
Customer Prediction
```

### Algorithm Used

**K-Means Clustering**

K-Means is an unsupervised learning algorithm that divides data points into `K` clusters based on their similarity.

The algorithm works by:

1. Selecting `K` cluster centroids.
2. Assigning each customer to the nearest centroid.
3. Updating the centroid of each cluster.
4. Repeating the process until the clusters converge.

---

## 📊 Customer Segmentation

The model groups customers into different segments based on the selected customer features.

Example segments may represent customers such as:

* High-value customers
* Budget-conscious customers
* Frequent buyers
* Low-engagement customers

> The exact interpretation of each cluster depends on the dataset and features used for training.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* NumPy
* Pandas

### Data Visualization

* Matplotlib
* Seaborn

### Web Development

* Flask
* HTML
* CSS
* JavaScript

### Deployment

* AWS

---

## 📁 Project Structure

```text
Customer-Segmentation/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
│
├── dataset/
│   └── customer_data.csv
│
├── notebook/
│   └── customer_segmentation.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/customer-segmentation.git
```

Navigate into the project:

```bash
cd customer-segmentation
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

Start the Flask server:

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser to access the application.

---

## 🔮 How It Works

The user provides the required customer information through the web interface.

The application then:

1. Receives the customer input.
2. Performs the required preprocessing.
3. Applies the saved scaler.
4. Passes the processed data to the trained K-Means model.
5. Determines the customer's cluster.
6. Displays the predicted customer segment.

---

## 📈 Model Development

The Machine Learning model was developed using the following steps:

### 1. Data Collection

Customer data is collected and loaded using Pandas.

### 2. Data Preprocessing

The dataset is analyzed and prepared for machine learning.

Typical preprocessing steps include:

* Handling missing values
* Removing unnecessary columns
* Selecting relevant features
* Feature scaling

### 3. Exploratory Data Analysis

The customer dataset is analyzed using statistical summaries and visualizations to understand:

* Customer distribution
* Feature relationships
* Spending behavior
* Customer characteristics

### 4. Selecting the Number of Clusters

The appropriate number of clusters is determined using techniques such as the **Elbow Method**.

### 5. Model Training

K-Means clustering is trained on the processed customer data.

```python
KMeans(n_clusters=k)
```

### 6. Model Saving

The trained model and preprocessing objects are saved so they can be reused by the Flask application without retraining every time.

---

## 📊 Results

The trained clustering model successfully divides customers into meaningful groups based on their characteristics.

The resulting clusters can be analyzed to understand differences between customer groups and support targeted business strategies.

---

## 🌐 Web Application

The Flask application provides a simple interface where users can enter customer information and receive the corresponding customer segment.

### Application Flow

```text
User Input
    ↓
Flask Backend
    ↓
Data Preprocessing
    ↓
Scaler
    ↓
K-Means Model
    ↓
Predicted Cluster
    ↓
Customer Segment
```

---

## ☁️ AWS Deployment

The application can be deployed on AWS to make the customer segmentation system accessible over the internet.

A typical deployment architecture is:

```text
User
  ↓
Internet
  ↓
AWS
  ↓
Flask Application
  ↓
ML Model
  ↓
Customer Segment
```

---

## 💡 Business Applications

Customer segmentation can be used for:

* Targeted marketing campaigns
* Personalized offers
* Customer retention
* Product recommendations
* Customer relationship management
* Identifying high-value customers
* Improving marketing efficiency

---

## 🔮 Future Improvements

Possible improvements include:

* Add more customer behavioral features
* Experiment with other clustering algorithms
* Add automatic cluster interpretation
* Improve the user interface
* Add interactive visualizations
* Add customer segmentation analytics dashboard
* Deploy using Docker
* Add real-time customer data processing
* Implement automated model retraining

---

## 👨‍💻 Author

**Nikhil**

AI & Machine Learning Enthusiast

Interested in:

* Machine Learning
* Deep Learning
* MLOps
* Artificial Intelligence
* Data Science

---

## ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ on GitHub!
