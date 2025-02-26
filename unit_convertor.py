import streamlit as st

# Function to load external CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Function to toggle dark mode
def toggle_dark_mode(dark_mode):
    if dark_mode:
        st.markdown(
            """
            <style>
            :root {
                --background: linear-gradient(45deg, #1e1e2f, #2d2d44);
                --text-color: #e0e0e0;
                --button-bg: #555;
                --button-hover-bg: #666;
                --input-bg: #444;
                --input-text: #e0e0e0;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            :root {
                --background: linear-gradient(45deg, #6a11cb, #2575fc);
                --text-color: white;
                --button-bg: #4CAF50;
                --button-hover-bg: #45a049;
                --input-bg: #333;
                --input-text: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

# Load the CSS file
load_css("styles.css")

# Title of the app with emoji
st.title("📏 Unit Convertor Pro")

# Sidebar for unit categories and dark/light mode toggle
with st.sidebar:
    st.header("Settings")
    unit_category = st.selectbox(
        "Select Unit Category",
        ["Length", "Weight", "Temperature", "Volume"],
        key="unit_category",
    )
    dark_mode = st.toggle("Dark Mode 🌙", value=True)

# Toggle dark mode
toggle_dark_mode(dark_mode)

# Dynamic unit selection based on category
if unit_category == "Length":
    units = ["meters", "kilometers", "centimeters", "millimeters", "feet", "inches", "miles", "yards"]
elif unit_category == "Weight":
    units = ["kilograms", "grams", "milligrams", "pounds", "ounces"]
elif unit_category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
elif unit_category == "Volume":
    units = ["liters", "milliliters", "gallons", "quarts", "pints", "cups", "tablespoons", "teaspoons"]

# Input fields in columns
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", units, key="from_unit")
with col2:
    to_unit = st.selectbox("To", units, key="to_unit")

value = st.number_input("Enter value to convert", value=1.0, key="value")

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_conversions = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "feet": 0.3048,
        "inches": 0.0254,
        "miles": 1609.34,
        "yards": 0.9144,
    }
    return value * (length_conversions[from_unit] / length_conversions[to_unit])

def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        "kilograms": 1,
        "grams": 0.001,
        "milligrams": 0.000001,
        "pounds": 0.453592,
        "ounces": 0.0283495,
    }
    return value * (weight_conversions[from_unit] / weight_conversions[to_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5 / 9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9 / 5 + 32
    else:
        return value

def convert_volume(value, from_unit, to_unit):
    volume_conversions = {
        "liters": 1,
        "milliliters": 0.001,
        "gallons": 3.78541,
        "quarts": 0.946353,
        "pints": 0.473176,
        "cups": 0.24,
        "tablespoons": 0.0147868,
        "teaspoons": 0.00492892,
    }
    return value * (volume_conversions[from_unit] / volume_conversions[to_unit])

# Perform conversion
if st.button("Convert 🔄"):
    with st.spinner("Converting..."):
        if unit_category == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif unit_category == "Weight":
            result = convert_weight(value, from_unit, to_unit)
        elif unit_category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif unit_category == "Volume":
            result = convert_volume(value, from_unit, to_unit)

        st.success(f"**{value} {from_unit} = {result:.2f} {to_unit}**")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Syeda Abiha Ahmed")