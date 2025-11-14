<h1 align="center" id="title">EMI Calculator</h1>

<p id="description">A web-based Equated Monthly Installment (EMI) Calculator built with Streamlit and deployed on Streamlit Cloud .</p>

<h2>🚀 Final product</h2>

[https://emicalculatorgit-bdmf9frspmaihvkhawewgg.streamlit.app/](https://emicalculatorgit-bdmf9frspmaihvkhawewgg.streamlit.app/)

<h2>Project Screenshots:</h2>

<img src="https://github.com/bluetorodev/emi_calculator/blob/main/screenshot.png" alt="project-screenshot">

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Input loan amount interest rate and tenure (in years or months)
*   Calculates monthly EMI total payment and interest payable
*   Provides a simple user-friendly interactive UI
*   Responsive fast and requires no installation (runs in browser)
*   (Optional) Charts or breakdowns of principal vs. interest over time

<h2>🛠️ Installation Steps:</h2>

<p>1. Open the live app link above.</p>

<p>2. Enter the Loan Amount.</p>

<p>3. Enter the Annual Interest Rate (in %).</p>

<p>4. Enter the Tenure (number of years or months).</p>

<p>5. View the results:</p>

```
Monthly EMI
```

```
Total payment amount
```

```
Total interest paid
```

<p>8. (Optional) View any extra visual breakdowns if implemented.</p>

<p>9. Installation (for local development)</p>

```
git clone https://github.com/bluetorodev/emi_calculator.git
```

```
cd emi-calculator
```

```
streamlit run app.py
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Frontend / UI: Streamlit (Python)
*   Backend / Logic: Python functions computing EMI using the formula: EMI = 𝑃 × 𝑟 × ( 1 + 𝑟 ) 𝑛 ( 1 + 𝑟 ) 𝑛 − 1 EMI= (1+r) n −1 P×r×(1+r) n ​ where 𝑃 P=principal 𝑟 r=monthly interest rate 𝑛 n=number of monthly payments.
*   Hosting / Deployment: Streamlit Cloud
*   Dependencies: (e.g.) streamlit numpy pandas

*   Version: 1.0.0

