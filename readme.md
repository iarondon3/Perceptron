# 🧠 Perceptron from Scratch — Emerging Computing

> An interactive single-layer perceptron built in pure Python, capable of classifying linearly separable data and visualizing results in real time through the console.

---

## 📌 Description

This project implements a **simple perceptron** from scratch as part of the *Emerging Computing (FPTSP25)* course at Universidad Metropolitana. The program allows the user to load their own dataset, manually configure weights and bias, select an activation function, and instantly visualize the perceptron's performance through comparative scatter plots.

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
├── datos.py             # CSV loading and parsing
├── grafico.py           # Visualization with matplotlib
│
├── fuzzy_separables.csv     # Linearly separable dataset (fuzzy)
└── no_separables.csv        # Linearly non-separable dataset
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/iarondon3/perceptron.git
cd perceptron
```

### 2. Install the dependency

The project only requires `matplotlib` as an external library.

```bash
pip install matplotlib
```

### 3. Run the program

```bash
python main.py
```

---

## 🖥️ Program Flow

```
1. Enter the path to your CSV file
2. Select an activation function (Step or Sigmoid)
3. Enter the bias value
4. Enter a weight for each input variable
5. The perceptron computes Z and generates predictions
6. Three comparative plots are displayed
7. Try new weights or exit the program
```

---

## 📊 Visualizations

The program renders three plots side by side:

| Plot | Description |
|---|---|
| **1. Expected Value** | Ground truth classification from the dataset |
| **2. Predicted Value** | Classification computed by the perceptron |
| **3. Error Map** | Green: low error (<5%) · Yellow: medium (<15%) · Red: high (>15%) |

The **decision boundary** (dashed line) is automatically calculated from the input weights and bias.

---

## 📁 CSV Format

The file must include headers in the first row. The first `n-1` columns are inputs, and the **last column is the expected output** (0 or 1).

```csv
x1,x2,output
2.5,1.3,1
0.8,3.1,0
...
```

---

## 🧮 Mathematical Foundation

The perceptron computes the weighted sum:

```
Z = (w1 · x1) + (w2 · x2) + ... + b
```

Then applies the selected activation function:

- **Step Function:** returns `1` if Z > 0, `0` otherwise
- **Sigmoid:** `σ(Z) = 1 / (1 + e^(-Z))`

> ⚠️ Known limitation: the perceptron **cannot separate** linearly non-separable data. This is an expected and demonstrated behavior using the `no_separables.csv` dataset.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Pure Python](https://img.shields.io/badge/No%20ML%20Libraries-Pure%20Python-green)

- **Python 3.x** — no ML libraries used (fully manual implementation)
- **Matplotlib** — only external dependency, used for visualization

---

## 👩‍💻 Author

**Isabella Rondón**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/isabella-rondon-rojas-/)

*Emerging Computing — Universidad Metropolitana*  
*Professor: Fernando Torre Mora*

---

## 📄 License

This project is for academic purposes only.
