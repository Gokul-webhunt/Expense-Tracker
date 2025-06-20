
# 💸 Expense Tracker – Python + Pandas + NumPy  
👤 Author: **Gokul**

A command-line app to track your daily expenses and analyze spending patterns using **Python, Pandas, and NumPy**.  
Perfect for learning data manipulation while solving a real-life problem! 📊

---

## 🧠 Key Concepts & Definitions

- **CSV File** 📄: A simple file format used to store tabular data (Comma-Separated Values).
- **Pandas** 🐼: A powerful library used for data analysis and manipulation.
- **NumPy** 🔢: Library for performing fast mathematical operations.
- **DataFrame** 📊: A 2D table-like structure provided by Pandas to work with data easily.

---

## 🛠️ Functions Used

- `pd.read_csv()` – Read a CSV file into a DataFrame 📥  
- `df.sum()` – Calculate total expenses 💰  
- `df.max()` / `df.min()` – Find highest/lowest amounts 📈📉  
- `df.groupby()` – Group data by category 📂  
- `np.round()` – Round percentage values to 2 decimal places 🔁  
- `plt.pie()` – (Optional) Generate a pie chart 🥧  

---

## 🖥️ Sample Output

```
==> 💸 Total Spending Overview
Total Amount Spent: Rs.5400
Highest Expense: Rs.5000 (Rent - June Rent)
Lowest Expense: Rs.50 (Transport - Rickshaw fare)

==> 📊 Category-wise Analysis
              sum  count  percentage
Category                              
Food          150      1        2.78
Transport      50      1        0.93
Rent         5000      1       92.59
Utilities     200      1        3.70
```

---

## 🔍 Program Explanation (Step-by-Step)

1️⃣ **Load CSV File**  
Read the file `expenses.csv` using `pandas.read_csv()`.

2️⃣ **Overview Section**  
Calculate total expenses using `.sum()`, find max and min expenses with `.idxmax()` / `.idxmin()`.

3️⃣ **Group by Category**  
Use `groupby()` to:
- Sum expenses per category
- Count number of transactions
- Calculate percentage of total spending

4️⃣ **Optional Chart (Bonus)**  
Use `matplotlib.pyplot.pie()` to display category-wise breakdown visually.
