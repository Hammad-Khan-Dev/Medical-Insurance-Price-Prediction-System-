"""
Medical Insurance Price Prediction System
------------------------------------------
Predicts an approximate medical insurance premium based on a person's
age, BMI, health issues, smoking status, salary, and gender.

Pipeline: load CSV -> encode categorical columns -> train Linear
Regression model -> collect input via Tkinter GUI -> predict and display.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import tkinter as tk

# ===============================
# Load Dataset
# ===============================
df = pd.read_csv("health_data_100.csv")

gender_encoder = LabelEncoder()
smoker_encoder = LabelEncoder()
health_encoder = LabelEncoder()

df['Gender'] = gender_encoder.fit_transform(df['Gender'])
df['Smoker'] = smoker_encoder.fit_transform(df['Smoker'])
df['Health_Issues'] = health_encoder.fit_transform(df['Health_Issues'])

X = df[['Age', 'BMI', 'Health_Issues', 'Smoker', 'Salary', 'Gender']]
y = df['Insurance_Price']

# ===============================
# Train Model
# ===============================
model = LinearRegression()
model.fit(X, y)


# ===============================
# Prediction Function
# ===============================
def predict_price():
    age = age_scale.get()
    bmi = float(bmi_spinbox.get())

    health = health_listbox.get(health_listbox.curselection())
    if health == "None":
        health = 0
    else:
        health = health_encoder.transform([health])[0]

    smoker = smoker_encoder.transform([smoker_var.get()])[0]

    salary = float(salary_entry.get())

    # Gender Checkbutton Logic
    if male_var.get() == 1:
        gender = "Male"
    elif female_var.get() == 1:
        gender = "Female"
    else:
        result_label.config(text="Select Gender")
        return

    gender = gender_encoder.transform([gender])[0]

    input_data = [[age, bmi, health, smoker, salary, gender]]

    prediction = model.predict(input_data)

    result_label.config(text=f"Predicted Insurance Price: \u20b9{round(prediction[0], 2)}")


# ===============================
# Tkinter GUI
# ===============================
root = tk.Tk()
root.title("Medical Insurance Price Predictor")
root.geometry("400x520")

# Age Scale
tk.Label(root, text="Age").pack()
age_scale = tk.Scale(root, from_=18, to=80, orient="horizontal")
age_scale.pack()

# BMI Spinbox
tk.Label(root, text="BMI").pack()
bmi_spinbox = tk.Spinbox(root, from_=0, to=40, increment=0.1)
bmi_spinbox.pack()

# Health Issues Listbox
tk.Label(root, text="Health Issues").pack()

health_options = [
    "Arthritis",
    "Asthma",
    "High Cholesterol",
    "Hypertension",
    "Sleep Apnea",
    "Type 2 Diabetes",
    "None"
]

health_listbox = tk.Listbox(root, height=7)
for item in health_options:
    health_listbox.insert(tk.END, item)

health_listbox.pack()

# Smoker
tk.Label(root, text="Smoker").pack()

smoker_var = tk.StringVar(value="No")

tk.Radiobutton(root, text="Yes", variable=smoker_var, value="Yes").pack()
tk.Radiobutton(root, text="No", variable=smoker_var, value="No").pack()

# Salary Entry
tk.Label(root, text="Salary").pack()
salary_entry = tk.Entry(root)
salary_entry.pack()

# Gender Checkbuttons
tk.Label(root, text="Gender").pack()

male_var = tk.IntVar()
female_var = tk.IntVar()

tk.Checkbutton(root, text="Male", variable=male_var).pack()
tk.Checkbutton(root, text="Female", variable=female_var).pack()

# Predict Button
tk.Button(root, text="Predict Insurance Price", command=predict_price).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
