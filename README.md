# Medical Insurance Price Prediction System

Built a desktop app that predicts medical insurance premiums using machine learning. You enter details like age, BMI, smoking habit, and health conditions, and it gives you an estimated insurance cost based on patterns learned from historical data.

Used Python throughout — pandas for handling the dataset, scikit-learn for training a Linear Regression model, and Tkinter to build a simple GUI so users can actually interact with it instead of just running a script.

This wasn't meant to be a real-world pricing engine insurers would use. It was more about learning how to take a project from raw data to a working, usable tool: cleaning and preparing data, encoding categorical fields like gender and smoker status into numbers, training the model, and connecting it all to a front end.

## Features

- Interactive Tkinter GUI — age slider, BMI spinbox, health issue list, smoker radio buttons, salary field, gender checkboxes
- Linear Regression model trained on a CSV dataset with `scikit-learn`
- Categorical fields (`Gender`, `Smoker`, `Health_Issues`) encoded with `LabelEncoder`
- Instant predicted price shown in the same window

## Tech stack

- **Python 3**
- **pandas** — data loading and handling
- **scikit-learn** — `LinearRegression`, `LabelEncoder`
- **Tkinter** — GUI (ships with standard Python; on some Linux distros install separately with `sudo apt install python3-tk`)

## Project structure

```
.
├── main.py               # App entry point — loads data, trains model, runs GUI
├── health_data_100.csv   # Sample dataset (100 records)
├── requirements.txt
└── README.md
```

## Getting started

1. Clone the repo:
   ```bash
   git clone https://github.com/Hammad-Khan-Dev/Medical-Insurance-Price-Prediction-System.git
   cd Medical-Insurance-Price-Prediction-System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.py
   ```

4. Fill in the details in the GUI and click **Predict Insurance Price**.

## Dataset

`health_data_100.csv` contains 100 sample records with the following columns:

| Column | Description |
|---|---|
| `Age` | Person's age in years |
| `BMI` | Body Mass Index |
| `Health_Issues` | Condition category (e.g. Asthma, Hypertension, None) |
| `Smoker` | Yes / No |
| `Salary` | Annual income |
| `Gender` | Male / Female |
| `Insurance_Price` | Target variable — the value the model learns to predict |

Swap in your own CSV with the same column names to retrain on different data.

## Notes

- This is an academic/learning project — the pricing logic is illustrative, not actuarially accurate.
- The bundled dataset is synthetic and generated for demonstration purposes.

## License

MIT
