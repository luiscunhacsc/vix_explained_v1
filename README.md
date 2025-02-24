# VIX Explained v1

This repository contains an interactive pedagogical tool designed to help users understand the VIX index and its relationship with option pricing. Built with Streamlit, the app provides a hands-on experience to explore how implied volatility (captured by the VIX) influences option prices using a simplified Black–Scholes model.

## Overview

The **VIX Explained v1** tool is structured into several tabs, each focusing on a different aspect of the VIX index:

- **Interactive Tool:** Experiment with key parameters such as implied volatility, time to expiration, underlying price, and risk-free rate to see how they affect the VIX value and option pricing.
- **Theory Behind VIX:** Learn about the theoretical foundations of the VIX index, including its role as a "fear gauge" and its derivation from option prices.
- **Comprehensive Tutorial:** A step-by-step guide that explains the dynamics of implied volatility and option pricing.
- **Practical Labs:** Predefined scenarios (baseline, high volatility, and low volatility) to simulate various market conditions.
- **The Very Basics of VIX:** A simple explanation of the VIX index and its importance in understanding market sentiment.

## Features

- **Interactive Visualization:** Use sliders to adjust parameters and observe real-time changes in option prices and the VIX index.
- **Black–Scholes Integration:** The app includes a simplified Black–Scholes call option pricing function to demonstrate the impact of volatility on option pricing.
- **Educational Value:** Ideal for classroom demonstrations and self-study to demystify key quantitative finance concepts.

## Installation

### Prerequisites

- Python 3.7 or higher

### Required Libraries

- [Streamlit](https://streamlit.io/)
- NumPy
- Matplotlib
- SciPy

Install the required packages using pip:

```bash
pip install streamlit numpy matplotlib scipy
```

## Running the App

To launch the interactive tool, navigate to the repository directory and run:

```bash
streamlit run app.py
```

This command will start the Streamlit server and open the app in your default web browser.

## Repository Structure

- **app.py:** The main Python file containing the Streamlit application code.
- **README.md:** This file.
- Additional configuration or asset files (if any) related to the project.

## Legal Disclaimer

The VIX Explained v1 software ("Software") is provided **for educational and informational purposes only** and is not intended to provide financial, investment, legal, or tax advice. By using this Software, you agree to the following terms:

### No Investment Advice

- The Software is designed solely to illustrate quantitative finance concepts and the functioning of the VIX index through simplified models.
- The developers, including Luís Simões da Cunha, are not financial advisors and do not offer personalized financial recommendations. Use of the Software does not create an advisory relationship.

### No Warranty

- THE SOFTWARE IS PROVIDED "AS IS," WITHOUT ANY WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.
- The authors and contributors make no representations or warranties regarding the accuracy, completeness, or reliability of the Software or its output.

### Limitation of Liability

- IN NO EVENT SHALL THE AUTHORS, CONTRIBUTORS, OR COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES, OR DAMAGES FOR LOSS OF PROFITS, REVENUE, DATA, OR USE, ARISING OUT OF OR IN CONNECTION WITH YOUR ACCESS TO OR USE OF THE SOFTWARE.
- Users assume full responsibility for any decisions made based on the Software.

### Indemnification

- By using this Software, you agree to indemnify, defend, and hold harmless the authors, contributors, and copyright holders from any claims, liabilities, damages, losses, or expenses (including reasonable attorneys' fees) arising out of or in any way connected with your use of the Software.

### Educational Purposes

- The Software is intended for **educational use only**. It is not a substitute for professional financial advice, investment strategies, or any professional services. Always consult with a licensed professional before making any financial decisions.

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

## Author

**Luís Simões da Cunha**

