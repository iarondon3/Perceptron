# 🧠 Perceptron from Scratch

> An interactive single-layer perceptron built in pure Python, capable of classifying linearly separable data and visualizing results in real time through the console.

---

## 📌 Description

This project implements a **simple perceptron** from scratch without the use of any machine learning libraries. The program allows the user to load their own dataset, manually configure weights and bias, select an activation function, and instantly visualize the perceptron's performance through comparative scatter plots.

This project serves as the foundation for a [Multilayer Perceptron (MLP)](https://github.com/iarondon3/multilayer-perceptron) implementation with backpropagation.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![No ML Frameworks](https://img.shields.io/badge/No%20ML%20Libraries-Pure%20Python-green)

- **Python 3.x** — no ML libraries used (fully manual implementation)
- **Matplotlib** — only external dependency, used for visualization

---

## ✨ Features

- 📂 Load data from custom **CSV files** via console
- ⚙️ Manual configuration of **weights (w)** and **bias (b)**
- 🔘 Choose an **activation function** at runtime:
  - Step Function
  - Sigmoid Function
- 📊 Automatic generation of **3 side-by-side plots** using `matplotlib`:
  - Expected values (ground truth)
  - Predicted values by the perceptron
  - Error map (green / yellow / red)
- 🔁 Ability to **test different weights** without restarting the program

---

## 🗂️ Project Structure

```
perceptron/
│
├── main.py              # Entry point of the program
├── perceptron.py        # Perceptron logic (weighted sum, activation, execution)
├── data.py             # CSV loading and parsing
├── plots.py           # Visualization with matplotlib
│
├── fuzzy_separables.csv     # Linearly separable dataset (fuzzy)
└── no_separables.csv        # Linearly non-separable dataset
```

---

## 📊 Visualizations

| Plot | Description |
|---|---|
| **1. Expected Value** | Ground truth classification from the dataset |
| **2. Predicted Value** | Classification computed by the perceptron |
| **3. Error Map** | Green: low error (<5%) · Yellow: medium (<15%) · Red: high (>15%) |

The **decision boundary** (dashed line) is automatically calculated from the input weights and bias.

---

<details>
<summary>🚀 Getting Started</summary>

### 1. Clone the repository

```bash
git clone https://github.com/iarondon3/Perceptron.git
cd Perceptron
```

### 2. Install the dependency

```bash
pip install matplotlib
```

### 3. Run the program

```bash
python main.py
```

### Program Flow

```
1. Enter the path to your CSV file
2. Select an activation function (Step or Sigmoid)
3. Enter the bias value
4. Enter a weight for each input variable
5. The perceptron computes Z and generates predictions
6. Three comparative plots are displayed
7. Try new weights or exit the program
```

</details>

---

<details>
<summary>📁 File Format</summary>

The CSV file must include headers in the first row. The first `n-1` columns are inputs and the last column is the expected output (0 or 1):

```csv
x1,x2,output
2.5,1.3,1
0.8,3.1,0
...
```

</details>

---

<details>
<summary>🧮 Mathematical Foundation</summary>

**Weighted Sum:**
```
Z = (w1 · x1) + (w2 · x2) + ... + b
```

**Activation Functions:**

- **Step Function:** returns `1` if Z > 0, `0` otherwise
- **Sigmoid:** `σ(Z) = 1 / (1 + e^(-Z))`

> ⚠️ Known limitation: the perceptron **cannot separate** linearly non-separable data. This is an expected and demonstrated behavior using the `no_separables.csv` dataset.

</details>

---

## 👩‍💻 About the Author

*Isabella Rondón* | ***Business Economist & Data Analyst***

[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/isabella-rondon-rojas-/)
[![GitHub Portfolio](https://img.shields.io/badge/Visit-Portfolio-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/iarondon3)
