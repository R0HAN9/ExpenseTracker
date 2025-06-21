# 💰 Expense Tracker - Command Line Finance Manager

A comprehensive command-line expense tracking application built with Python, Pandas, and NumPy. This tool helps you manage, analyze, and visualize your personal finances with detailed reporting and interactive charts.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-Latest-orange.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Latest-red.svg)

## 🚀 Features

### ✅ Core Features

- **📊 Total Spending Overview** - Complete financial summary with highest/lowest expenses
- **📈 Category-wise Analysis** - Detailed breakdown by expense categories with percentages
- **🥧 Pie Chart Visualization** - Interactive visual representation of expense distribution
- **📅 Date Range Filtering** - Filter and analyze expenses for specific time periods
- **➕ Add New Expenses** - Easy command-line expense entry
- **📋 Export Summary Reports** - Generate CSV reports for external analysis

### 🎯 Bonus Features

- **👁️ View All Expenses** - Comprehensive expense listing with sorting
- **🔄 Data Reload** - Refresh data without restarting the application
- **💾 Auto-save** - Automatic CSV file updates
- **🎨 Rich CLI Interface** - Colorful, user-friendly command-line experience
- **📊 Statistical Analysis** - Average expenses, transaction counts, and more
- **🛡️ Error Handling** - Robust error management and validation

## 🗂️ Project Structure

```
ExpenseTracker/
├── expense_tracker.py      # Main application script
├── expenses.csv           # Input data file (user-editable)
├── summary_report.csv     # Generated summary output file
├── expense_pie_chart.png  # Generated visualization
├── README.md             # This documentation
├── requirements.txt      # Python dependencies
└── screenshots/          # Sample outputs (optional)
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone/Download the Project

```bash
# Download the project files to your local machine
mkdir ExpenseTracker
cd ExpenseTracker
# Copy the provided files into this directory
```

### Step 2: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Or install individually:
pip install pandas numpy matplotlib
```

### Step 3: Prepare Data File

The application will automatically create a sample `expenses.csv` file if none exists. You can also create your own:

```csv
Date,Category,Amount,Description
2025-06-10,Food,150,Pizza at Dominos
2025-06-11,Transport,50,Rickshaw fare
2025-06-12,Rent,5000,June Rent
```

### Step 4: Run the Application

```bash
python expense_tracker.py
```

## 🎮 How to Use

### Main Menu Options

When you run the application, you'll see an interactive menu:

```
          💰 EXPENSE TRACKER MENU
============================================================
1. 📊 Total Spending Overview
2. 📈 Category-wise Analysis
3. 🥧 Pie Chart Visualization
4. 📅 Filter by Date Range
5. ➕ Add New Expense
6. 📋 Export Summary Report
7. 🔄 Reload Data
8. 👁️  View All Expenses
9. ❌ Exit
============================================================
```

### Sample Usage Examples

#### 1. **Total Spending Overview**

```
💰 Total Amount Spent: ₹6,455.00
📋 Total Transactions: 12
📊 Average Expense: ₹537.92

🔥 HIGHEST EXPENSE:
   Date: 2025-06-12
   Category: Rent
   Amount: ₹5,000.00
   Description: June Rent

💡 LOWEST EXPENSE:
   Date: 2025-06-11
   Category: Transport
   Amount: ₹50.00
   Description: Rickshaw fare
```

#### 2. **Category Analysis**

```
Category        Total (₹)    Count   Avg (₹)    %
----------------------------------------------------------------------
Rent              5,000.00       1   5,000.00  77.46%
Entertainment       800.00       2     400.00  12.39%
Food                580.00       4     145.00   8.98%
Transport           225.00       3      75.00   3.49%
Utilities           350.00       2     175.00   5.42%
```

#### 3. **Adding New Expense**

```
Enter date (YYYY-MM-DD) or press Enter for today: 2025-06-21
Enter category: Food
Enter amount (₹): 85
Enter description: Morning coffee
✅ Successfully added expense!
```

#### 4. **Date Range Filtering**

```
Enter start date (YYYY-MM-DD): 2025-06-15
Enter end date (YYYY-MM-DD): 2025-06-20
✓ Found 5 expenses between 2025-06-15 and 2025-06-20
Total Amount: ₹1,155.00
```

## 📊 Sample Input/Output

### Input CSV Format

```csv
Date,Category,Amount,Description
2025-06-10,Food,150,Pizza at Dominos
2025-06-11,Transport,50,Rickshaw fare
2025-06-12,Rent,5000,June Rent
2025-06-12,Utilities,200,Electricity Bill
```

### Generated Summary Report (summary_report.csv)

```csv
Category,Total_Amount,Transaction_Count,Average_Amount,First_Date,Last_Date,Percentage
Food,880.0,4,220.0,2025-06-10,2025-06-19,13.63
Rent,5000.0,1,5000.0,2025-06-12,2025-06-12,77.46
Transport,225.0,3,75.0,2025-06-11,2025-06-20,3.49
Utilities,350.0,2,175.0,2025-06-12,2025-06-17,5.42
Entertainment,1200.0,2,600.0,2025-06-14,2025-06-18,18.60
TOTAL,6455.0,12,537.92,2025-06-10,2025-06-20,100.0
```

## 🎨 Visualizations

The application generates beautiful pie charts showing expense distribution:

- **Automatic color coding** for different categories
- **Percentage labels** on each slice
- **Legend with amounts** for detailed information
- **High-resolution PNG export** for sharing

## 🔧 Technical Details

### Libraries Used

- **Pandas**: Data manipulation, CSV handling, grouping operations
- **NumPy**: Numerical computations, statistical analysis
- **Matplotlib**: Data visualization, pie chart generation
- **DateTime**: Date parsing and manipulation
- **OS/Sys**: File operations and system interactions

### Key Features Implementation

- **Object-Oriented Design**: Clean, maintainable code structure
- **Error Handling**: Comprehensive exception management
- **Data Validation**: Input validation and type checking
- **Memory Efficient**: Optimized DataFrame operations
- **User-Friendly**: Intuitive CLI with clear feedback

### CSV File Structure

The application expects a CSV file with exactly these columns:

- `Date`: YYYY-MM-DD format
- `Category`: String (Food, Transport, Rent, etc.)
- `Amount`: Numeric value (positive numbers)
- `Description`: Text description of the expense

## 🚨 Troubleshooting

### Common Issues & Solutions

1. **Module Not Found Error**

   ```bash
   pip install pandas numpy matplotlib
   ```

2. **CSV File Corruption**

   - Delete `expenses.csv` to regenerate sample data
   - Check CSV format matches expected structure

3. **Date Format Errors**

   - Use YYYY-MM-DD format only
   - Ensure dates are valid calendar dates

4. **Chart Display Issues**
   - Install GUI backend for matplotlib
   - Chart saves as PNG even if display fails

## 📝 Development Notes

### Code Quality Features

- **Comprehensive Comments**: Every function documented
- **Type Hints**: Clear parameter and return types
- **Error Messages**: User-friendly error descriptions
- **Modular Design**: Separated concerns for maintainability
- **PEP 8 Compliance**: Python style guide adherence

### Performance Optimizations

- **Efficient DataFrame Operations**: Vectorized pandas operations
- **Memory Management**: Proper resource handling
- **Lazy Loading**: Data loaded only when needed
- **Batch Operations**: Grouped calculations for speed

## 🎯 Future Enhancements

- **Database Integration**: SQLite support for larger datasets
- **Budget Tracking**: Set and monitor spending limits
- **Multiple Currencies**: Support for different currencies
- **Data Import**: Import from bank statements
- **Web Interface**: Flask/Django web application
- **Mobile App**: Cross-platform mobile version

## 📄 License

This project is created for educational purposes. Feel free to use, modify, and distribute as needed.

## 👨‍💻 Author

Created as part of a Python data analysis project using Pandas and NumPy for financial data management.

---

**💡 Pro Tips:**

- Keep your CSV file backed up regularly
- Use consistent category names for better analysis
- Add expenses daily for accurate tracking
- Export summary reports monthly for review
- Use descriptive expense descriptions for clarity

**🎉 Happy Expense Tracking!** 💰📊
