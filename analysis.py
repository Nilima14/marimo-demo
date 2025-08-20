# analysis.py
# Author: Nilima Motghare
# Email: 23f1000504@ds.study.iitm.ac.in
# Marimo reactive notebook demo

import marimo as mo

# -----------------------------
# Cell 1: Define a base variable
# -----------------------------
x = 10
# This is a base variable. Other cells will depend on it.


# -----------------------------
# Cell 2: Add interactive slider
# -----------------------------
slider = mo.ui.slider(1, 100, value=25)
# Slider widget allows dynamic control of "scale".


# -----------------------------
# Cell 3: Create a dependent variable
# -----------------------------
scaled_value = x * slider.value
# This depends on both Cell 1 (x) and Cell 2 (slider).


# -----------------------------
# Cell 4: Dynamic markdown output
# -----------------------------
mo.md(f"""
# 📊 Interactive Analysis

- **Base value (x):** {x}  
- **Slider value:** {slider.value}  
- **Scaled result (x * slider):** {scaled_value}  

{"🟢" * (slider.value // 5)}  
""")
