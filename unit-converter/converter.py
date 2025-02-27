import streamlit as st

# Streamlit App
st.set_page_config(page_title="Google Unit Converter", layout="centered")
st.title("🌍 Google Unit Converter")

# Sidebar selection
option = st.sidebar.selectbox(
    "Choose conversion type", 
    ["Length", "Weight", "Temperature", "Currency", "Speed", "Area", "Volume", "Time", "Energy"]
)

def unit_converter(category, units, conversion_func):
    st.header(f"{category} Converter")
    from_unit = st.selectbox("From", units, key=f"from_{category}")
    to_unit = st.selectbox("To", units, key=f"to_{category}")
    value = st.number_input("Enter value", min_value=0.0, format="%.4f", key=f"value_{category}")

    if st.button("Convert", key=f"convert_{category}"):
        result = conversion_func(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

def simple_conversion(value, from_unit, to_unit, conversion_rates):
    return value * conversion_rates[from_unit] / conversion_rates[to_unit]

if option == "Length":
    length_units = {"meters": 1, "kilometers": 1000, "centimeters": 0.01, "millimeters": 0.001,
                    "inches": 0.0254, "feet": 0.3048, "yards": 0.9144, "miles": 1609.34}
    unit_converter("Length", length_units.keys(), lambda v, f, t: simple_conversion(v, f, t, length_units))

elif option == "Weight":
    weight_units = {"grams": 1, "kilograms": 1000, "milligrams": 0.001, "pounds": 453.592, "ounces": 28.3495}
    unit_converter("Weight", weight_units.keys(), lambda v, f, t: simple_conversion(v, f, t, weight_units))

elif option == "Speed":
    speed_units = {"meters per second": 1, "kilometers per hour": 3.6, "miles per hour": 2.237, "feet per second": 3.281}
    unit_converter("Speed", speed_units.keys(), lambda v, f, t: simple_conversion(v, f, t, speed_units))

elif option == "Area":
    area_units = {"square meters": 1, "square kilometers": 1e6, "square feet": 0.092903, "square inches": 0.00064516,
                  "acres": 4046.86, "hectares": 10000}
    unit_converter("Area", area_units.keys(), lambda v, f, t: simple_conversion(v, f, t, area_units))

elif option == "Volume":
    volume_units = {"liters": 1, "milliliters": 0.001, "cubic meters": 1000, "cubic feet": 28.3168,
                    "gallons": 3.78541, "cups": 0.236588, "pints": 0.473176}
    unit_converter("Volume", volume_units.keys(), lambda v, f, t: simple_conversion(v, f, t, volume_units))

elif option == "Time":
    time_units = {"seconds": 1, "minutes": 60, "hours": 3600, "days": 86400, "weeks": 604800,
                  "months": 2.628e+6, "years": 3.154e+7}
    unit_converter("Time", time_units.keys(), lambda v, f, t: simple_conversion(v, f, t, time_units))

elif option == "Energy":
    energy_units = {"joules": 1, "calories": 4.184, "kilocalories": 4184, "kilowatt hours": 3.6e6, "electronvolts": 1.602e-19}
    unit_converter("Energy", energy_units.keys(), lambda v, f, t: simple_conversion(v, f, t, energy_units))

elif option == "Temperature":
    st.header("Temperature Converter")
    temp_units = ["celsius", "fahrenheit", "kelvin"]
    from_unit = st.selectbox("From", temp_units, key="temp_from")
    to_unit = st.selectbox("To", temp_units, key="temp_to")
    value = st.number_input("Enter value", format="%.2f", key="temp_value")

    def convert_temperature(value, from_unit, to_unit):
        conversions = {
            "celsius": {"fahrenheit": (value * 9/5 + 32), "kelvin": (value + 273.15)},
            "fahrenheit": {"celsius": ((value - 32) * 5/9), "kelvin": ((value - 32) * 5/9 + 273.15)},
            "kelvin": {"celsius": (value - 273.15), "fahrenheit": ((value - 273.15) * 9/5 + 32)}
        }
        return conversions[from_unit].get(to_unit, value)

    if st.button("Convert", key="temp_convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

# Custom CSS
st.markdown("""
    <style>
        .stButton button {
            background-color: #4CAF50 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            border-radius: 5px !important;
            font-size: 16px !important;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #45a049 !important;
        }
        .stTextInput input, .stNumberInput input {
            border-radius: 5px !important;
            padding: 10px !important;
            border: 2px solid #ddd !important;
            font-size: 16px !important;
        }
    </style>
""", unsafe_allow_html=True)
