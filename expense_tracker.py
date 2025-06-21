#!/usr/bin/env python3
"""
Expense Tracker Application
A command-line tool for managing and analyzing personal expenses using Pandas and NumPy.

Author: ROHAN
Date: June 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
import sys

class ExpenseTracker:
    """
    A comprehensive expense tracking application with data analysis and visualization capabilities.
    """
    
    def __init__(self, csv_file='expenses.csv'):
        """
        Initialize the ExpenseTracker with a CSV file.
        
        Args:
            csv_file (str): Path to the CSV file containing expense data
        """
        self.csv_file = csv_file
        self.df = None
        self.load_data()
    
    def load_data(self):
        """
        Load expense data from CSV file. Create a new file if it doesn't exist.
        """
        try:
            if os.path.exists(self.csv_file):
                self.df = pd.read_csv(self.csv_file)
                # Convert Date column to datetime
                self.df['Date'] = pd.to_datetime(self.df['Date'])
                print(f"Successfully loaded {len(self.df)} expenses from {self.csv_file}")
            else:
                # Create sample data if file doesn't exist
                print(f"⚠ {self.csv_file} not found. Creating sample data...")
                self.create_sample_data()
        except Exception as e:
            print(f"Error loading data: {e}")
            sys.exit(1)
    
    def create_sample_data(self):
        """
        Create sample expense data for demonstration purposes.
        """
        sample_data = {
            'Date': ['2025-06-10', '2025-06-11', '2025-06-12', '2025-06-12', 
                    '2025-06-13', '2025-06-14', '2025-06-15'],
            'Category': ['Food', 'Transport', 'Rent', 'Utilities', 'Food', 
                        'Entertainment', 'Transport'],
            'Amount': [150, 50, 5000, 200, 300, 800, 75],
            'Description': ['Pizza at Dominos', 'Rickshaw fare', 'June Rent', 
                           'Electricity Bill', 'Grocery shopping', 'Movie tickets', 'Bus fare']
        }
        
        self.df = pd.DataFrame(sample_data)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.save_data()
        print(f"Created sample data with {len(self.df)} entries")
    
    def save_data(self):
        """
        Save the current DataFrame to CSV file.
        """
        try:
            self.df.to_csv(self.csv_file, index=False, date_format='%Y-%m-%d')
            print(f"Data saved to {self.csv_file}")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def display_total_overview(self):
        """
        Display comprehensive spending overview including totals and extremes.
        """
        print("\n" + "="*60)
        print("           TOTAL SPENDING OVERVIEW")
        print("="*60)
        
        if self.df.empty:
            print("No expenses found.")
            return
        
        # Calculate totals
        total_amount = self.df['Amount'].sum()
        total_transactions = len(self.df)
        average_expense = self.df['Amount'].mean()
        
        print(f"Total Amount Spent: ₹{total_amount:,.2f}")
        print(f"Total Transactions: {total_transactions}")
        print(f"Average Expense: ₹{average_expense:,.2f}")
        
        # Find highest and lowest expenses
        highest_idx = self.df['Amount'].idxmax()
        lowest_idx = self.df['Amount'].idxmin()
        
        print(f"\n HIGHEST EXPENSE:")
        print(f"   Date: {self.df.loc[highest_idx, 'Date'].strftime('%Y-%m-%d')}")
        print(f"   Category: {self.df.loc[highest_idx, 'Category']}")
        print(f"   Amount: ₹{self.df.loc[highest_idx, 'Amount']:,.2f}")
        print(f"   Description: {self.df.loc[highest_idx, 'Description']}")
        
        print(f"\n LOWEST EXPENSE:")
        print(f"   Date: {self.df.loc[lowest_idx, 'Date'].strftime('%Y-%m-%d')}")
        print(f"   Category: {self.df.loc[lowest_idx, 'Category']}")
        print(f"   Amount: ₹{self.df.loc[lowest_idx, 'Amount']:,.2f}")
        print(f"   Description: {self.df.loc[lowest_idx, 'Description']}")
    
    def category_analysis(self):
        """
        Perform detailed category-wise analysis of expenses.
        """
        print("\n" + "="*70)
        print("           CATEGORY-WISE ANALYSIS")
        print("="*70)
        
        if self.df.empty:
            print("No expenses found for analysis.")
            return
        
        # Group by category and calculate statistics
        category_stats = self.df.groupby('Category').agg({
            'Amount': ['sum', 'count', 'mean'],
            'Description': 'count'
        }).round(2)
        
        # Flatten column names
        category_stats.columns = ['Total_Amount', 'Transaction_Count', 'Average_Amount', 'Description_Count']
        
        # Calculate percentage of total spending
        total_spending = self.df['Amount'].sum()
        category_stats['Percentage'] = (category_stats['Total_Amount'] / total_spending * 100).round(2)
        
        # Sort by total amount (descending)
        category_stats = category_stats.sort_values('Total_Amount', ascending=False)
        
        print(f"{'Category':<15} {'Total (₹)':<12} {'Count':<8} {'Avg (₹)':<10} {'%':<8}")
        print("-" * 70)
        
        for category, row in category_stats.iterrows():
            print(f"{category:<15} {row['Total_Amount']:>10,.2f} {row['Transaction_Count']:>6} "
                  f"{row['Average_Amount']:>8,.2f} {row['Percentage']:>6.2f}%")
        
        return category_stats
    
    def create_pie_chart(self):
        """
        Create and display a pie chart of expenses by category.
        """
        if self.df.empty:
            print("No data available for pie chart.")
            return
        
        # Group by category and sum amounts
        category_totals = self.df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
        
        # Create pie chart
        plt.figure(figsize=(10, 8))
        colors = plt.cm.Set3(np.linspace(0, 1, len(category_totals)))
        
        wedges, texts, autotexts = plt.pie(category_totals.values, 
                                          labels=category_totals.index,
                                          autopct='%1.1f%%',
                                          colors=colors,
                                          startangle=90,
                                          explode=[0.05] * len(category_totals))
        
        # Customize the chart
        plt.title('Expense Distribution by Category', fontsize=16, fontweight='bold', pad=20)
        
        # Improve text readability
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        # Add a legend with amounts
        legend_labels = [f"{cat}: ₹{amt:,.0f}" for cat, amt in category_totals.items()]
        plt.legend(wedges, legend_labels, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        
        plt.tight_layout()
        
        # Save the chart
        chart_filename = 'expense_pie_chart.png'
        plt.savefig(chart_filename, dpi=300, bbox_inches='tight')
        print(f"✓ Pie chart saved as {chart_filename}")
        
        # Show the chart
        plt.show()
    
    def filter_by_date(self):
        """
        Filter expenses by date range and display analysis.
        """
        print("\n" + "="*50)
        print("           FILTER BY DATE RANGE")
        print("="*50)
        
        try:
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()
            
            # Convert to datetime
            start_dt = pd.to_datetime(start_date)
            end_dt = pd.to_datetime(end_date)
            
            # Filter dataframe
            mask = (self.df['Date'] >= start_dt) & (self.df['Date'] <= end_dt)
            filtered_df = self.df.loc[mask]
            
            if filtered_df.empty:
                print(f"No expenses found between {start_date} and {end_date}")
                return
            
            print(f"\n✓ Found {len(filtered_df)} expenses between {start_date} and {end_date}")
            print(f"Total Amount: ₹{filtered_df['Amount'].sum():,.2f}")
            
            # Display filtered data
            print(f"\n{'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<30}")
            print("-" * 70)
            
            for _, row in filtered_df.iterrows():
                print(f"{row['Date'].strftime('%Y-%m-%d'):<12} {row['Category']:<15} "
                      f"₹{row['Amount']:>8,.2f} {row['Description']:<30}")
            
            # Perform analysis on filtered data
            print(f"\n Category Analysis for {start_date} to {end_date}:")
            if len(filtered_df) > 0:
                category_totals = filtered_df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
                total = filtered_df['Amount'].sum()
                
                for category, amount in category_totals.items():
                    percentage = (amount / total * 100)
                    print(f"   {category}: ₹{amount:,.2f} ({percentage:.1f}%)")
        
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
        except Exception as e:
            print(f"Error filtering data: {e}")
    
    def add_new_expense(self):
        """
        Add a new expense entry via command line input.
        """
        print("\n" + "="*50)
        print("           ADD NEW EXPENSE")
        print("="*50)
        
        try:
            # Get input from user
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if not date:
                date = datetime.now().strftime('%Y-%m-%d')
            
            category = input("Enter category (Food/Transport/Rent/Utilities/Entertainment/etc.): ").strip()
            amount = float(input("Enter amount (₹): ").strip())
            description = input("Enter description: ").strip()
            
            # Validate inputs
            if not category or not description:
                print("Category and description cannot be empty.")
                return
            
            if amount <= 0:
                print("Amount must be positive.")
                return
            
            # Create new expense entry
            new_expense = {
                'Date': pd.to_datetime(date),
                'Category': category,
                'Amount': amount,
                'Description': description
            }
            
            # Add to dataframe
            new_row = pd.DataFrame([new_expense])
            self.df = pd.concat([self.df, new_row], ignore_index=True)
            
            # Save to CSV
            self.save_data()
            
            print(f"   Successfully added expense:")
            print(f"   Date: {date}")
            print(f"   Category: {category}")
            print(f"   Amount: ₹{amount:,.2f}")
            print(f"   Description: {description}")
            
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Error adding expense: {e}")
    
    def export_summary_report(self):
        """
        Export category analysis to a CSV summary report.
        """
        try:
            category_stats = self.df.groupby('Category').agg({
                'Amount': ['sum', 'count', 'mean'],
                'Date': ['min', 'max']
            }).round(2)
            
            # Flatten column names
            category_stats.columns = ['Total_Amount', 'Transaction_Count', 'Average_Amount', 'First_Date', 'Last_Date']
            
            # Calculate percentage
            total_spending = self.df['Amount'].sum()
            category_stats['Percentage'] = (category_stats['Total_Amount'] / total_spending * 100).round(2)
            
            # Add summary statistics
            summary_stats = pd.DataFrame({
                'Total_Amount': [total_spending],
                'Transaction_Count': [len(self.df)],
                'Average_Amount': [self.df['Amount'].mean()],
                'First_Date': [self.df['Date'].min()],
                'Last_Date': [self.df['Date'].max()],
                'Percentage': [100.0]
            }, index=['TOTAL'])
            
            # Combine category stats with summary
            full_report = pd.concat([category_stats, summary_stats])
            
            # Export to CSV
            report_file = 'summary_report.csv'
            full_report.to_csv(report_file)
            
            print(f"   Summary report exported to {report_file}")
            print(f"   Categories analyzed: {len(category_stats)}")
            print(f"   Total transactions: {len(self.df)}")
            print(f"   Total amount: ₹{total_spending:,.2f}")
            
        except Exception as e:
            print(f"Error exporting summary: {e}")
    
    def display_menu(self):
        """
        Display the main menu options.
        """
        print("\n" + "="*60)
        print("           EXPENSE TRACKER MENU")
        print("="*60)
        print("1. Total Spending Overview")
        print("2. Category-wise Analysis")
        print("3. Pie Chart Visualization")
        print("4. Filter by Date Range")
        print("5. Add New Expense")
        print("6. Export Summary Report")
        print("7. Reload Data")
        print("8. View All Expenses")
        print("9. Exit")
        print("="*60)
    
    def view_all_expenses(self):
        """
        Display all expenses in a formatted table.
        """
        print("\n" + "="*80)
        print("            ALL EXPENSES")
        print("="*80)
        
        if self.df.empty:
            print("No expenses found.")
            return
        
        # Sort by date (newest first)
        sorted_df = self.df.sort_values('Date', ascending=False)
        
        print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<40}")
        print("-" * 80)
        
        for _, row in sorted_df.iterrows():
            print(f"{row['Date'].strftime('%Y-%m-%d'):<12} {row['Category']:<15} "
                  f"₹{row['Amount']:>8,.2f} {row['Description']:<40}")
        
        print(f"\nTotal Expenses: {len(sorted_df)} | Total Amount: ₹{sorted_df['Amount'].sum():,.2f}")
    
    def run(self):
        """
        Main application loop.
        """
        print("Welcome to the Expense Tracker!")
        print("Manage your finances with ease using Python, Pandas & NumPy")
        
        while True:
            self.display_menu()
            
            try:
                choice = input("Enter your choice (1-9): ").strip()
                
                if choice == '1':
                    self.display_total_overview()
                elif choice == '2':
                    self.category_analysis()
                elif choice == '3':
                    self.create_pie_chart()
                elif choice == '4':
                    self.filter_by_date()
                elif choice == '5':
                    self.add_new_expense()
                elif choice == '6':
                    self.export_summary_report()
                elif choice == '7':
                    self.load_data()
                elif choice == '8':
                    self.view_all_expenses()
                elif choice == '9':
                    print("Thank you for using Expense Tracker! Stay financially healthy!")
                    break
                else:
                    print("Invalid choice. Please select 1-9.")
                
                # Wait for user input before continuing
                if choice in ['1', '2', '4', '6', '8']:
                    input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Thanks for using Expense Tracker!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                input("Press Enter to continue...")

def main():
    """
    Main function to run the expense tracker application.
    """
    try:
        # Create and run the expense tracker
        tracker = ExpenseTracker()
        tracker.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()