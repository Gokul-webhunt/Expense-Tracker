"""
Expense Tracker
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load expenses from CSV
def load_expenses(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None

# Display total, max, min
def total_spending_summary(df):
    print("***********************************")
    print("\tTotal Spending Overview")
    print("***********************************")
    total = df['Amount'].sum()
    max_expense = df.loc[df['Amount'].idxmax()]
    min_expense = df.loc[df['Amount'].idxmin()]
    print(f"Total Amount Spent: Rs.{total}")
    print(f"Highest Expense: Rs.{max_expense['Amount']} ({max_expense['Category']} - {max_expense['Description']})")
    print(f"Lowest Expense: Rs.{min_expense['Amount']} ({min_expense['Category']} - {min_expense['Description']})")

# Analyze by category
def category_analysis(df):
    print("***********************************")
    print("\tCategory-wise Analysis")
    print("***********************************")
    grouped = df.groupby('Category')['Amount'].agg(['sum', 'count'])
    grouped['percentage'] = (grouped['sum'] / df['Amount'].sum() * 100).round(2)
    print(grouped)

# Show pie chart
def show_pie_chart(df):
    print("***********************************")
    print("\tGenerating Pie Chart...")
    print("***********************************")
    category_totals = df.groupby('Category')['Amount'].sum()
    category_totals.plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title("Expense Breakdown by Category")
    plt.ylabel('')
    plt.show()

# Main function
def main():
    file_path = 'expenses.csv'
    df = load_expenses(file_path)
    if df is not None:
        total_spending_summary(df)
        category_analysis(df)
        choice = input("\nDo you want to view a pie chart? (y/n): ").lower()
        if choice == 'y':
            show_pie_chart(df)

# Run the app
if __name__ == '__main__':
    main()
