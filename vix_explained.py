import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import log, sqrt, exp
from scipy.stats import norm

#############################################
# 1) Define callback functions for VIX labs:
#############################################
def reset_vix_parameters():
    st.session_state["vol_slider"] = 20.0   # 20%
    st.session_state["tau_slider"] = 30     # 30 days
    st.session_state["S_slider"] = 100.0      # Underlying price: 100
    st.session_state["r_slider"] = 2.0        # 2%

def set_lab1_vix_parameters():
    st.session_state["vol_slider"] = 20.0   # 20%
    st.session_state["tau_slider"] = 30
    st.session_state["S_slider"] = 100.0
    st.session_state["r_slider"] = 2.0

def set_lab2_vix_parameters():
    st.session_state["vol_slider"] = 40.0   # 40%
    st.session_state["tau_slider"] = 30
    st.session_state["S_slider"] = 100.0
    st.session_state["r_slider"] = 2.0

def set_lab3_vix_parameters():
    st.session_state["vol_slider"] = 10.0   # 10%
    st.session_state["tau_slider"] = 30
    st.session_state["S_slider"] = 100.0
    st.session_state["r_slider"] = 2.0

#############################################
# 2) Black–Scholes Call Option Pricing Function
#############################################
def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes call option price.
    
    Parameters:
      S     : Underlying price
      K     : Strike price
      T     : Time to expiration (in years)
      r     : Annual risk-free rate (in decimals)
      sigma : Annualized volatility (in decimals)
      
    Returns:
      Call option price
    """
    if T <= 0:
        return max(S - K, 0)
    d1 = (log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    call_price = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    return call_price

#############################################
# 3) Compute VIX Index Value (Simplified)
#############################################
def compute_vix(vol):
    """
    In this pedagogical tool, we assume the VIX index is the implied annualized volatility.
    (For example, an input volatility of 20% corresponds to a VIX value of 20.)
    """
    return vol

#############################################
# 4) Configure the Streamlit App
#############################################
st.set_page_config(layout="wide")
st.title("📊 Understanding the VIX Index")
st.markdown("Explore how implied volatility—as captured by the VIX index—affects option pricing and reflects market sentiment.")

#############################################
# 5) Sidebar: VIX Parameters and Disclaimer
#############################################
with st.sidebar:
    st.header("⚙️ VIX Parameters")
    st.button("↺ Reset Parameters", on_click=reset_vix_parameters)
    
    # Sliders (volatility is in percent, so we convert to decimals)
    vol = st.slider("Implied Annual Volatility (σ) [%]", 0.0, 100.0, 20.0, step=0.5, key='vol_slider') / 100
    tau = st.slider("Time to Expiration (days)", 1, 365, 30, step=1, key='tau_slider')
    S = st.slider("Underlying Price (S)", 50.0, 150.0, 100.0, step=0.5, key='S_slider')
    r = st.slider("Risk-Free Rate (r) [%]", 0.0, 10.0, 2.0, step=0.1, key='r_slider') / 100

    st.markdown("---")
    st.markdown(
    """
    **⚠️ Disclaimer**  
    *Educational purposes only. This tool is intended for learning about the VIX index and option pricing. It should not be used for actual investment decisions.*
    """
    )
    st.markdown(
    """
    <div style="margin-top: 20px;">
        <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">
            <img src="https://licensebuttons.net/l/by-nc/4.0/88x31.png" alt="CC BY-NC 4.0">
        </a>
        <br>
        <span style="font-size: 0.8em;">By Luís Simões da Cunha</span>
    </div>
    """, unsafe_allow_html=True)

#############################################
# 6) Main Calculation and Tabs
#############################################
# Compute the VIX index value (in our simplified model, equal to the input volatility * 100)
vix_value = compute_vix(vol)

# Create tabs for different sections
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎮 Interactive Tool", 
    "📚 Theory Behind VIX", 
    "📖 Comprehensive Tutorial", 
    "🛠️ Practical Labs",
    "🧠 The Very Basics of VIX"
])

#############################################
# Tab 1: Interactive VIX Calculator & Option Pricing
#############################################
with tab1:
    st.subheader("Interactive VIX Calculator & Option Pricing")
    st.markdown(f"### VIX Index Value: **{vix_value*100:.2f}%**")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("**Key Parameters:**")
        st.latex(r"\text{VIX} \approx \sigma \times 100")
        st.markdown(f"""
        - **Implied Volatility (σ):** {vol*100:.2f}%
        - **Time to Expiration:** {tau} days
        - **Underlying Price (S):** {S:.2f}
        - **Risk-Free Rate (r):** {r*100:.2f}%
        """)
    with col2:
        # Plot call option prices vs. strike price using Black-Scholes
        strikes = np.linspace(0.5 * S, 1.5 * S, 100)
        T_year = tau / 365  # convert days to years
        option_prices = [black_scholes_call(S, K, T_year, r, vol) for K in strikes]
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(strikes, option_prices, color='green', linewidth=2, label="Call Option Price")
        ax.set_title("Call Option Prices vs. Strike Price")
        ax.set_xlabel("Strike Price (K)")
        ax.set_ylabel("Call Option Price")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

#############################################
# Tab 2: Theory Behind VIX
#############################################
with tab2:
    st.markdown("""
    ## VIX: Theoretical Foundations

    The **VIX Index** reflects the market's expectation of future volatility over the next 30 days and is derived from S&P 500 index options.

    **Key Concepts:**
    - **Implied Volatility (σ):** Indicates the market’s forecast of the underlying asset's volatility.
    - **Option Prices:** The VIX is calculated from a wide range of option prices, capturing a consensus view of future risk.
    - **Market Sentiment:** Often dubbed the "fear gauge," higher VIX levels suggest greater uncertainty or risk.

    While the actual VIX calculation involves a sophisticated formula that integrates option prices across strikes, this tool simplifies the concept by equating the VIX index with the implied volatility.
    """)

#############################################
# Tab 3: Comprehensive VIX Tutorial
#############################################
with tab3:
    st.markdown("""
    ## Comprehensive VIX Tutorial

    **What you'll learn:**
    
    1. **Understanding Implied Volatility:**  
       - Derived from option prices, implied volatility reflects market expectations.
       - It is a key input in models like Black–Scholes for pricing options.
       
    2. **Interpreting the VIX Index:**  
       - The VIX translates implied volatility into a single, annualized percentage.
       - It serves as a benchmark for market uncertainty.
       
    3. **Option Pricing Dynamics:**  
       - Discover how variations in volatility impact call option prices.
       - Use the interactive tool to observe these effects graphically.
       
    4. **Practical Applications:**  
       - Gauge market sentiment and assess potential risk.
       - Understand both the strengths and limitations of volatility measures.
       
    Experiment with the sidebar parameters and observe the real-time impact on option pricing and the VIX value.
    """)

#############################################
# Tab 4: Practical Labs
#############################################
with tab4:
    st.header("🔬 Practical VIX Labs")
    lab_choice = st.radio(
        "Select a Lab:",
        ("Lab 1: Baseline Scenario", "Lab 2: High Volatility Environment", "Lab 3: Low Volatility Environment"),
        index=0
    )
    
    if lab_choice == "Lab 1: Baseline Scenario":
        st.subheader("Baseline Scenario")
        st.markdown("""
        **Scenario:**  
        Analyze a market with a moderate level of volatility.  
        **Parameters:**
        - Implied Volatility: 20%
        - Time to Expiration: 30 days
        - Underlying Price: 100
        - Risk-Free Rate: 2%
        """)
        st.button("⚡ Set Lab 1 Parameters", on_click=set_lab1_vix_parameters, key="lab1_vix")
    
    elif lab_choice == "Lab 2: High Volatility Environment":
        st.subheader("High Volatility Environment")
        st.markdown("""
        **Scenario:**  
        Explore a scenario with heightened market uncertainty.  
        **Parameters:**
        - Implied Volatility: 40%
        - Time to Expiration: 30 days
        - Underlying Price: 100
        - Risk-Free Rate: 2%
        """)
        st.button("⚡ Set Lab 2 Parameters", on_click=set_lab2_vix_parameters, key="lab2_vix")
    
    else:
        st.subheader("Low Volatility Environment")
        st.markdown("""
        **Scenario:**  
        Investigate a calm market scenario with lower volatility.  
        **Parameters:**
        - Implied Volatility: 10%
        - Time to Expiration: 30 days
        - Underlying Price: 100
        - Risk-Free Rate: 2%
        """)
        st.button("⚡ Set Lab 3 Parameters", on_click=set_lab3_vix_parameters, key="lab3_vix")

#############################################
# Tab 5: The Very Basics of VIX
#############################################
with tab5:
    st.header("🧠 The Very Basics of VIX")
    st.markdown("""
    **What is the VIX?**
    
    - **VIX Index:** Measures the market's expectation of near-term volatility.
    - **Implied Volatility:** Extracted from option prices, it reflects market uncertainty.
    - **Market Indicator:** Often called the "fear gauge," a high VIX signals elevated risk.
    
    **Key Takeaways:**
    - The VIX offers insight into market sentiment.
    - It is crucial for understanding option pricing and risk management.
    - This tool provides a simplified view of how volatility influences option prices.
    """)
