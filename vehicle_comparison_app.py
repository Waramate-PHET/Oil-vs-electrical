import streamlit as st
import base64
import requests

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
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Failed to load the background image.")

def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'

    if st.session_state['page'] == 'home':
        home_page()
    elif st.session_state['page'] == 'comparison':
        comparison_page()

# Home page: Button to start comparison between electric and gasoline vehicles
def home_page():
    st.title("รถที่ใช้น้ำมัน vs รถใช้ไฟฟ้า")
    st.write("เปรียบเทียบประสิทธิภาพและค่าใช้จ่ายระหว่าง รถไฟฟ้า และ รถใช้น้ำมัน")

    if st.button('คำนวณรถที่ใช้น้ำมัน vs รถใช้ไฟฟ้า'):
        st.session_state['page'] = 'comparison'

# Comparison page: Inputs and calculation for both electric and gasoline vehicles
def comparison_page():
    st.title("เปรียบเทียบ รถไฟฟ้า vs รถใช้น้ำมัน")

    col1, col2 = st.columns(2)

    # Inputs for Electric Vehicle
    with col1:
        st.header("รถใช้ไฟฟ้า")
        
        st.write("กรอกความจุแบตเตอรี่ (kWh)")
        battery_capacity = st.number_input("แบตเตอรี่ (kWh)", min_value=0.0, key="battery_capacity")
        
        st.write("กรอกระยะทางที่รถไปได้ (กิโลเมตร)")
        electric_distance = st.number_input("ระยะทางที่รถไฟฟ้าไปได้ (km)", min_value=0.0, key="electric_distance")
        
        st.write("แสดงความเร็วปกติของตัวรถ (กม./ชม.)")
        electric_speed = st.number_input("ความเร็วปกติ (km/h)", min_value=0.0, key="electric_speed")
        
        st.write("กรอกราคาค่าไฟฟ้า (บาท/kWh)")
        electricity_price = st.number_input("ราคาค่าไฟฟ้า (บาท/kWh)", min_value=0.0, key="electricity_price")

    # Inputs for Gasoline Vehicle
    with col2:
        st.header("รถใช้น้ำมัน")
        
        st.write("กรอกความจุถังน้ำมัน (ลิตร)")
        fuel_capacity = st.number_input("น้ำมัน (ลิตร)", min_value=0.0, key="fuel_capacity")
        
        st.write("กรอกระยะทางที่รถไปได้ (กิโลเมตร)")
        gasoline_distance = st.number_input("ระยะทางที่รถน้ำมันไปได้ (km)", min_value=0.0, key="gasoline_distance")
        
        st.write("แสดงความเร็วปกติของตัวรถ (กม./ชม.)")
        gasoline_speed = st.number_input("ความเร็วปกติ (km/h)", min_value=0.0, key="gasoline_speed")
        
        st.write("กรอกราคาน้ำมัน (บาท/ลิตร)")
        fuel_price = st.number_input("ราคาน้ำมัน (บาท/ลิตร)", min_value=0.0, key="fuel_price")

    # Perform calculation and comparison
    if st.button("คำนวณ"):
        # Electric vehicle efficiency and cost
        if electric_distance > 0:
            electric_efficiency = battery_capacity / electric_distance
            total_electric_cost = battery_capacity * electricity_price
        else:
            electric_efficiency = 0
            total_electric_cost = 0
        
        # Gasoline vehicle efficiency and cost
        if gasoline_distance > 0:
            gasoline_efficiency = fuel_capacity / gasoline_distance
            total_fuel_cost = fuel_capacity * fuel_price
        else:
            gasoline_efficiency = 0
            total_fuel_cost = 0

        # Compare total costs
        if total_fuel_cost < total_electric_cost:
            cheaper_option = "รถใช้น้ำมันถูกกว่ารถใช้ไฟฟ้า"
        elif total_fuel_cost > total_electric_cost:
            cheaper_option = "รถใช้ไฟฟ้าถูกกว่ารถใช้น้ำมัน"
        else:
            cheaper_option = "ค่าใช้จ่ายทั้งสองเท่ากัน"

        # Display results
        st.subheader("ผลลัพธ์การคำนวณ")
        
        st.write(f"**รถไฟฟ้า** ประสิทธิภาพ: {electric_efficiency:.2f} kWh/กิโลเมตร")
        st.write(f"ค่าใช้จ่ายรวมสำหรับรถไฟฟ้า: {total_electric_cost:.2f} บาท")
        
        st.write(f"**รถใช้น้ำมัน** ประสิทธิภาพ: {gasoline_efficiency:.2f} ลิตร/กิโลเมตร")
        st.write(f"ค่าใช้จ่ายน้ำมันรวม: {total_fuel_cost:.2f} บาท")

        st.subheader(f"ผลการเปรียบเทียบ: {cheaper_option}")

    # Add a "Go Back" button to return to the main page
    if st.button("กลับไปหน้าหลัก"):
        st.session_state['page'] = 'home'

# Run the app
if __name__ == '__main__':
    add_bg_from_url('https://images-storage.thaiware.site/tips/2020_11/images/1433_20111714250002_67.png')  # Set background from URL
    main()
