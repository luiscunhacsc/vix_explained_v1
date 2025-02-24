# Capital Asset Pricing Model (CAPM) Explained

## Overview

The **Capital Asset Pricing Model (CAPM)** is a foundational financial model that estimates the expected return of an asset based on its systematic risk (β). This interactive application empowers users to explore the intricate relationship between risk and return by allowing them to adjust key parameters, visualize outcomes, and dive into both the theory and practical applications behind CAPM.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Cloning the Repository](#cloning-the-repository)
  - [Creating a Virtual Environment](#creating-a-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Editing the Code](#editing-the-code)
- [Additional Resources](#additional-resources)
- [Support](#support)
- [License](#license)

## Overview

The CAPM is a core component of modern portfolio theory. It allows investors to understand and quantify the trade-off between risk and return by using beta (β) as a measure of an asset's sensitivity to market movements. This project includes:

- An interactive dashboard to input parameters such as the risk-free rate, market return, and beta.
- Dynamic visualizations that demonstrate how these parameters influence expected returns.
- Educational content that explains the underlying theory, assumptions, and real-world applications of CAPM.

## Features

- **Interactive Dashboard:** Real-time visualization of the Security Market Line (SML) and expected returns.
- **Customizable Inputs:** Adjust key financial parameters and see instant feedback.
- **Educational Modules:** Detailed explanations of CAPM, including its assumptions and limitations.
- **Hands-On Labs:** Practical examples and case studies to solidify your understanding.
- **User-Friendly Interface:** Designed for both beginners and seasoned finance professionals.

## Installation

### Prerequisites

Before setting up the project locally, ensure you have:

1. **A Computer:** Windows, macOS, or Linux.
2. **Python 3.9 or Higher:** (Python 3.12 is preferred).  
   Download from: [python.org/downloads](https://www.python.org/downloads/)
3. **Visual Studio Code (VS Code):** For code editing.  
   Download from: [code.visualstudio.com](https://code.visualstudio.com/)
4. **Git:** (Optional, but recommended for cloning the repository).  
   Download from: [git-scm.com/downloads](https://git-scm.com/downloads)

### Cloning the Repository

#### Option 1: Cloning via Git (Recommended)

1. Open Terminal (macOS/Linux) or Command Prompt/PowerShell (Windows).
2. Navigate to your desired directory:
   ```
   cd Documents
   ```
3. Clone the repository:
   ```
   git clone https://github.com/luiscunhacsc/capm_explained_v1.git
   ```
4. Enter the project folder:
   ```
   cd capm_explained_v1
   ```

#### Option 2: Download as ZIP

1. Visit [https://github.com/luiscunhacsc/capm_explained_v1](https://github.com/luiscunhacsc/capm_explained_v1).
2. Click on **Code > Download ZIP**.
3. Extract the ZIP file to your preferred location.

### Creating a Virtual Environment

Using a virtual environment helps manage dependencies efficiently.

1. Open VS Code and navigate to the project folder.
2. Open the integrated terminal (use **Ctrl + `** or select *Terminal > New Terminal*).
3. Create a virtual environment by running:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - **On Windows:**
     ```
     venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```
     source venv/bin/activate
     ```

### Installing Dependencies

With the virtual environment activated, install the required packages:
1. Upgrade pip:
   ```
   python.exe -m pip install --upgrade pip
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
This command installs libraries such as:
- **Streamlit** – For the interactive UI.
- **NumPy** – For mathematical computations.
- **Matplotlib** – For plotting visualizations.

## Usage

To launch the interactive CAPM application:

1. Ensure your virtual environment is active.
2. Run the following command in the terminal:
   ```
   streamlit run capm_explained.py
   ```
3. A new browser tab should open automatically at [http://localhost:8501](http://localhost:8501). If not, open your browser and navigate to that URL manually.

## Troubleshooting

- **ModuleNotFoundError:**  
  Verify that the virtual environment is activated using `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux).

- **Python Not Recognized:**  
  Ensure that Python is correctly installed and added to your system's PATH.

- **Browser Does Not Open Automatically:**  
  Manually navigate to [http://localhost:8501](http://localhost:8501) in your web browser.

## Editing the Code

To customize or improve the application:

1. Open `capm_explained.py` in VS Code.
2. Modify the code as desired.
3. After saving changes, restart the Streamlit app:
   - Stop the current session (using **Ctrl + C** in the terminal).
   - Relaunch with:
     ```
     streamlit run capm_explained.py
     ```

## Additional Resources

- **Streamlit Documentation:**  
  [docs.streamlit.io](https://docs.streamlit.io)

- **CAPM Overview:**  
  [Investopedia CAPM Guide](https://www.investopedia.com/terms/c/capm.asp)

- **Modern Portfolio Theory:**  
  [Investopedia Modern Portfolio Theory](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)

## Support

For issues, suggestions, or contributions, please open an issue on GitHub:  
[https://github.com/luiscunhacsc/capm_explained_v1/issues](https://github.com/luiscunhacsc/capm_explained_v1/issues)

## License & Legal Disclaimer

This project is licensed under the [CC BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/deed.en).

**By Luís Simões da Cunha**

This software is provided for educational purposes only. All information and results generated by this tool are intended solely for educational use and should not be interpreted as financial, investment, or professional advice. The author makes no representations or warranties of any kind, express or implied, regarding the accuracy, reliability, or completeness of the information provided. Use of this software is entirely at your own risk, and the author shall not be held liable for any errors, inaccuracies, or damages arising from its use.
