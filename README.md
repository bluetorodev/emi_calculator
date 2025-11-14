
# 💰 EMI Calculator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)

**A professional web-based Equated Monthly Installment (EMI) Calculator built with Streamlit**

[🚀 Live Demo](#-live-demo) • [⚡ Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [🤝 Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🚀 Live Demo](#-live-demo)
- [⚡ Quick Start](#-quick-start)
- [📖 Usage Guide](#-usage-guide)
- [🛠️ Technical Details](#️-technical-details)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🎯 Overview

EMI Calculator is a comprehensive, web-based application designed to help users calculate Equated Monthly Installments (EMI) for loans. Built with Streamlit and deployed on Streamlit Cloud, it provides an intuitive interface for calculating loan payments, generating detailed amortization schedules, and downloading financial data.

Whether you're planning a home loan, car loan, personal loan, or any other type of installment-based borrowing, this calculator provides accurate calculations with a clean, responsive interface that works seamlessly across all devices.

---

## ✨ Features

### 🔢 **Core Calculations**
- **EMI Calculation**: Accurate monthly payment computation using the standard formula
- **Total Interest**: Complete interest calculation over the loan tenure
- **Total Payment**: Principal amount plus total interest payable
- **Interest Rate Handling**: Supports both zero-interest and standard rate loans

### 📊 **Detailed Analytics**
- **Amortization Schedule**: Month-by-month breakdown of payments
- **Principal vs Interest**: Clear visualization of payment components
- **Balance Tracking**: Outstanding balance at each payment period
- **CSV Export**: Download complete schedule for offline analysis

### 🎨 **User Experience**
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Real-time Calculations**: Instant results as you modify inputs
- **Input Validation**: Prevents errors with intelligent validation
- **Clean Interface**: Professional, intuitive design
- **Currency Formatting**: Proper Indian Rupee (₹) formatting

### 🛡️ **Reliability**
- **Rounding Protection**: Handles floating-point precision issues
- **Error Handling**: Graceful handling of edge cases
- **Zero Interest Support**: Special handling for 0% interest loans
- **Input Constraints**: Validates all user inputs

---

## 🚀 Live Demo

Access the live application instantly:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/bluetorodev/emi_calculator/main/app.py)

*No installation required - runs directly in your browser!*

---

## ⚡ Quick Start

### Option 1: Use Online (Recommended)
1. Click the [Live Demo](#-live-demo) link above
2. Start calculating EMIs immediately!

### Option 2: Run Locally
```bash
# Clone the repository
git clone https://github.com/bluetorodev/emi_calculator.git
cd emi_calculator

# Install dependencies
pip install streamlit pandas numpy

# Run the application
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📖 Usage Guide

### Basic Calculation

1. **Enter Loan Amount**: Input the principal amount you want to borrow
2. **Set Interest Rate**: Enter the annual interest rate (percentage)
3. **Choose Tenure**: Specify the loan period in months
4. **View Results**: Instantly see your EMI, total interest, and total payment

### Advanced Features

#### 📅 **Start Date (Optional)**
- Add a schedule start date to see when your payments begin
- Useful for planning and budgeting

#### 📊 **Amortization Schedule**
- View detailed month-by-month breakdown
- See opening balance, interest, principal, and closing balance
- Understand how much of each payment goes toward interest vs principal

#### 💾 **Download Schedule**
- Export the complete amortization schedule as CSV
- Perfect for financial planning and record-keeping

### Example Calculation
```
Loan Amount: ₹10,00,000
Interest Rate: 8.25% per annum
Tenure: 36 months

Results:
• Monthly EMI: ₹31,214
• Total Interest: ₹1,23,705
• Total Payment: ₹11,23,705
```

---

## 🛠️ Technical Details

### **Technologies Used**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend Framework** | [Streamlit](https://streamlit.io) | Web application framework |
| **Data Processing** | [Pandas](https://pandas.pydata.org) | Data manipulation and analysis |
| **Numerical Computing** | [NumPy](https://numpy.org) | Mathematical calculations |
| **Deployment** | [Streamlit Cloud](https://share.streamlit.io) | Cloud hosting platform |
| **Development** | [Python](https://python.org) 3.8+ | Core programming language |

### **Core Algorithm**

The EMI calculation uses the standard financial formula:

```
EMI = P × r × (1 + r)^n / ((1 + r)^n - 1)

Where:
P = Principal loan amount
r = Monthly interest rate (annual rate ÷ 12 ÷ 100)
n = Number of monthly installments
```

### **Key Features Implementation**

- **Floating-point Precision**: Handles calculation accuracy with proper rounding
- **Zero Interest Handling**: Special case for 0% interest loans (simple division)
- **Amortization Logic**: Accurate principal and interest component separation
- **Data Export**: CSV generation with proper formatting
- **Responsive UI**: Adaptive layout for all screen sizes

### **Dependencies**
```
streamlit>=1.0.0
pandas>=1.0.0
numpy>=1.0.0
```

---

## 📁 Project Structure

```
emi_calculator/
├── .devcontainer/          # Development container configuration
├── app.py                 # Main application file
├── screenshot.png         # Application screenshot
├── README.md             # This file
└── requirements.txt      # Python dependencies (to be added)
```

---

## 🤝 Contributing

We welcome contributions to improve the EMI Calculator! Here's how you can help:

### **How to Contribute**

1. **Fork** the repository
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/yourusername/emi_calculator.git
   ```

3. **Create** a feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. **Make** your changes
5. **Test** thoroughly
6. **Commit** your changes:
   ```bash
   git commit -m 'Add amazing feature'
   ```

7. **Push** to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```

8. **Open** a Pull Request

### **Areas for Improvement**

- 🌐 **Internationalization**: Add support for other currencies
- 📈 **Visualizations**: Add charts for payment breakdown
- 🎨 **Themes**: Multiple UI themes and customization
- 📱 **Mobile Optimization**: Enhanced mobile experience
- 🔧 **Additional Features**: Prepayment calculations, comparison tools
- 🧪 **Testing**: Comprehensive unit and integration tests

### **Code Standards**

- Follow PEP 8 style guidelines
- Add docstrings for functions
- Include comments for complex logic
- Test your changes locally before submitting

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 bluetorodev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- **Streamlit Team**: For providing an excellent web application framework
- **Financial Community**: For standardizing EMI calculation formulas
- **Open Source Contributors**: For the amazing Python libraries that power this application
- **Users**: For feedback and suggestions that help improve the calculator

---

## 📞 Support

If you encounter any issues or have questions:

- **🐛 Bug Reports**: [Open an issue](https://github.com/bluetorodev/emi_calculator/issues)
- **💡 Feature Requests**: [Suggest new features](https://github.com/bluetorodev/emi_calculator/issues)
- **📧 Contact**: Reach out through GitHub

---

<div align="center">

**Made with ❤️ by [bluetorodev](https://github.com/bluetorodev)**

*Empowering financial decisions through accurate calculations*

[![⭐ Star this repo](https://img.shields.io/github/stars/bluetorodev/emi_calculator?style=social)](https://github.com/bluetorodev/emi_calculator)
[![🔗 Share](https://img.shields.io/badge/Share-LinkedIn-blue)](https://linkedin.com/shareArticle)

</div>

