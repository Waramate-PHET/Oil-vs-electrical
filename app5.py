import streamlit as st
import base64
import requests
from datetime import datetime

# Function to add background image from URL
def add_bg_from_url(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = base64.b64encode(response.content).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{image_data}");
                background-size: cover;
            }}
            .stTextInput, .stNumberInput, .stSelectbox {{
                background-color: rgba(255, 255, 255, 0.8);
                padding: 10px;
                border-radius: 10px;
            }}
            .info-box {{
                background-color: rgba(255, 255, 255, 0.8);
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 20px;
                font-size: 1.2em;
            }}
            .fuel-price-box {{
                background-color: rgba(255, 255, 255, 0.9);
                padding: 10px;
                border-radius: 10px;
                font-weight: bold;
                margin-bottom: 20px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Failed to load the background image.")

# Data for cars
car_data = {
    "BYD": {"Atto 3": {"type": "EV", "battery": 60, "range": 420}},
    "Tesla": {"Model Y": {"type": "EV", "battery": 75, "range": 505}},
    "MG": {"MG ZS EV": {"type": "EV", "battery": 44.5, "range": 337}},
    "ORA": {"Good Cat": {"type": "EV", "battery": 63, "range": 500}},
    "Neta": {"V": {"type": "EV", "battery": 38.5, "range": 300}},
    "Honda": {"Civic": {"type": "Gasoline", "fuel_efficiency": 15, "fuel_type1": "Benzene"}},
    "Mazda": {"Mazda 2": {"type": "Gasoline", "fuel_efficiency": 18, "fuel_type1": "Diesel"}},
    "Isuzu": {"D-Max": {"type": "Gasoline", "fuel_efficiency": 12, "fuel_type1": "Diesel"}},
    "Toyota": {"Camry": {"type": "Gasoline", "fuel_efficiency": 12, "fuel_type1": "Benzene"}},
    "Ford": {"Ranger": {"type": "Gasoline", "fuel_efficiency": 10, "fuel_type1": "Diesel"}}
}

# Function to get fuel prices
def get_fuel_prices(fuel_type1):
    prices = {
        "Gasohol 91": 40.50,
        "Gasohol 95": 41.00,
        "E20": 35.00,
        "E85": 30.00,
        "Benzene": 45.00,
        "Diesel": 32.00
    }
    return prices.get(fuel_type1, 0)

# Function to count visitors
def count_visitor():
    if 'visitor_count' not in st.session_state:
        st.session_state['visitor_count'] = 0
        st.session_state['visit_dates'] = []

    st.session_state['visitor_count'] += 1
    st.session_state['visit_dates'].append(datetime.now().strftime('%Y-%m-%d'))

    return st.session_state['visitor_count'], st.session_state['visit_dates']

# Main app logic
def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'

    if st.session_state['page'] == 'home':
        home_page()
    elif st.session_state['page'] == 'comparison':
        comparison_page()

# Home page: Button to start comparison between electric and gasoline vehicles
def home_page():
    visitor_count, visit_dates = count_visitor()
    
    st.title("รถที่ใช้น้ำมัน vs รถใช้ไฟฟ้า")
    st.write("เปรียบเทียบประสิทธิภาพและค่าใช้จ่ายระหว่าง รถไฟฟ้า และ รถใช้น้ำมัน")
    st.write(f"จำนวนผู้เข้าชมทั้งหมด: {visitor_count}")

    if st.button('คำนวณรถที่ใช้น้ำมัน vs รถใช้ไฟฟ้า'):
        st.session_state['page'] = 'comparison'

# Comparison page: Car selection and input for both electric and gasoline vehicles
def comparison_page():
    st.title("เปรียบเทียบ รถไฟฟ้า vs รถใช้น้ำมัน")

    col1, col2 = st.columns(2)

    # Filter electric and gasoline cars
    ev_brands = [brand for brand in car_data if car_data[brand][list(car_data[brand].keys())[0]]['type'] == "EV"]
    gas_brands = [brand for brand in car_data if car_data[brand][list(car_data[brand].keys())[0]]['type'] == "Gasoline"]

    # Select EV Car Brand and Model
    with col1:
        st.header("รถใช้ไฟฟ้า")
        ev_car_brand = st.selectbox("เลือกยี่ห้อรถไฟฟ้า", ev_brands, key="ev_car_brand")
        ev_car_model = st.selectbox(
            "เลือกรุ่นรถไฟฟ้า", [model for model in car_data[ev_car_brand].keys()], key="ev_car_model")

        if car_data[ev_car_brand][ev_car_model]["type"] == "EV":
            ev_battery = car_data[ev_car_brand][ev_car_model]["battery"]
            ev_range = car_data[ev_car_brand][ev_car_model]["range"]
            st.write(f"แบตเตอรี่: {ev_battery} kWh")
            st.write(f"ระยะทางสูงสุด: {ev_range} กม.")
        
        electricity_price = st.number_input("กรอกราคาค่าไฟฟ้า (บาท/kWh)", min_value=0.0, key="electricity_price")
        ev_distance = st.number_input("กรอกระยะทางที่เดินทาง (กม.)", min_value=0.0, key="ev_distance")
        ev_speed_ev = st.number_input("กรอกความเร็วปกติของรถไฟฟ้า (กม./ชม.)", min_value=0.0, key="ev_speed_ev")

    # Select Gasoline Car Brand and Model
    with col2:
        st.header("รถใช้น้ำมัน")
        gas_car_brand = st.selectbox("เลือกยี่ห้อรถน้ำมัน", gas_brands, key="gas_car_brand")
        gas_car_model = st.selectbox(
            "เลือกรุ่นรถน้ำมัน", [model for model in car_data[gas_car_brand].keys()], key="gas_car_model")

        if car_data[gas_car_brand][gas_car_model]["type"] == "Gasoline":
            gas_efficiency = car_data[gas_car_brand][gas_car_model]["fuel_efficiency"]
            fuel_type1 = car_data[gas_car_brand][gas_car_model]["fuel_type1"]
            fuel_price = get_fuel_prices(fuel_type1)
            st.write(f"อัตราสิ้นเปลืองน้ำมัน: {gas_efficiency} กม./ลิตร")
            st.write(f"ประเภทน้ำมัน: {fuel_type1}")
            fuel_type = st.selectbox("เลือกประเภทน้ำมัน", ["Gasohol 91", "Gasohol 95", "E20", "E85", "Benzene", "Diesel"])  
            fuel_price = get_fuel_prices(fuel_type)
            st.markdown(f"<div class='fuel-price-box'>ราคาน้ำมันที่เลือก: {fuel_price:.2f} บาท/ลิตร</div>", unsafe_allow_html=True)

        gas_distance = st.number_input("กรอกระยะทางที่เดินทาง (กม.)", min_value=0.0, key="gas_distance")
        gas_speed_gas = st.number_input("กรอกความเร็วปกติของรถน้ำมัน (กม./ชม.)", min_value=0.0, key="gas_speed_gas")

    # Perform calculation and comparison
    if st.button("คำนวณ"):
        # EV calculation
        ev_efficiency = ev_distance / ev_range if ev_distance > 0 else 0
        ev_total_cost = ev_efficiency * ev_distance * electricity_price if ev_distance > 0 else 0

        # Gasoline calculation
        gas_efficiency_value = car_data[gas_car_brand][gas_car_model]["fuel_efficiency"]
        gas_total_cost = (gas_distance / gas_efficiency_value) * fuel_price if gas_distance > 0 else 0

        # Display results side by side
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='info-box'>ผลลัพธ์รถไฟฟ้า</div>", unsafe_allow_html=True)
            st.markdown(
                f"<div class='info-box'>ประสิทธิภาพ: {ev_efficiency:.2f} kWh/กม.<br>ค่าใช้จ่ายรวม: {ev_total_cost:.2f} บาท</div>", 
                unsafe_allow_html=True
            )

        with col2:
            st.markdown("<div class='info-box'>ผลลัพธ์รถใช้น้ำมัน</div>", unsafe_allow_html=True)
            st.markdown(
                f"<div class='info-box'>ประสิทธิภาพ: {gas_efficiency_value} กม./ลิตร<br>ค่าใช้จ่ายรวม: {gas_total_cost:.2f} บาท</div>", 
                unsafe_allow_html=True
            )

        # Compare costs
        if gas_total_cost < ev_total_cost:
            st.subheader("รถใช้น้ำมันถูกกว่ารถใช้ไฟฟ้า")
        elif gas_total_cost > ev_total_cost:
            st.subheader("รถใช้ไฟฟ้าถูกกว่ารถใช้น้ำมัน")
        else:
            st.subheader("ค่าใช้จ่ายทั้งสองเท่ากัน")

    # Go back button
    if st.button("กลับไปหน้าหลัก"):
        st.session_state['page'] = 'home'

# Run the app
if __name__ == '__main__':
    add_bg_from_url('https://images-storage.thaiware.site/tips/2020_11/images/1433_20111714250002_67.png')  # Set background from URL
    main()