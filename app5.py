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

# Data for cars (example based on the note)
car_data = {
    "BYD": {"Atto 3": {"type": "EV", "battery": 60, "range": 420}},
    "Tesla": {"Model Y": {"type": "EV", "battery": 75, "range": 505}},
    "MG": {"MG ZS EV": {"type": "EV", "battery": 44.5, "range": 337}},
    "ORA": {"Good Cat": {"type": "EV", "battery": 63, "range": 500}},
    "Honda": {"Civic": {"type": "Gasoline", "fuel_efficiency": 15, "fuel_type": "Benzene"}},
    "Mazda": {"Mazda 2": {"type": "Gasoline", "fuel_efficiency": 18, "fuel_type": "Diesel"}},
    "Isuzu": {"D-Max": {"type": "Gasoline", "fuel_efficiency": 12, "fuel_type": "Diesel"}},
}

# Home page: Button to start comparison between electric and gasoline vehicles
def home_page():
    st.title("รถที่ใช้น้ำมัน vs รถใช้ไฟฟ้า")
    st.write("เปรียบเทียบประสิทธิภาพและค่าใช้จ่ายระหว่าง รถไฟฟ้า และ รถใช้น้ำมัน")

    if st.button('คำนวณรถที่ใช้น้ำมัน vs รถใช้ไฟฟ้า'):
        st.session_state['page'] = 'comparison'

# Comparison page: Car selection and input for both electric and gasoline vehicles
def comparison_page():
    st.title("เปรียบเทียบ รถไฟฟ้า vs รถใช้น้ำมัน")

    col1, col2 = st.columns(2)

    # Select EV Car Brand and Model
    with col1:
        st.header("รถใช้ไฟฟ้า")
        ev_car_brand = st.selectbox("เลือกยี่ห้อรถไฟฟ้า", [brand for brand in car_data if car_data[brand][list(car_data[brand].keys())[0]]['type'] == 'EV'])
        ev_car_model = st.selectbox("เลือกรุ่นรถไฟฟ้า", list(car_data[ev_car_brand].keys()))

        ev_car_info = car_data[ev_car_brand][ev_car_model]
        st.write(f"คุณเลือกรถไฟฟ้า: {ev_car_brand} {ev_car_model}")
        st.write(f"ความจุแบตเตอรี่: {ev_car_info['battery']} kWh")
        st.write(f"ระยะทางสูงสุด: {ev_car_info['range']} km")

        st.write("กรอกความเร็วปกติของรถ (กม./ชม.)")
        ev_speed = st.number_input("ความเร็ว (km/h)", min_value=0.0, key="ev_speed")

        st.write("กรอกระยะทางที่เดินทาง (กม.)")
        ev_distance = st.number_input("ระยะทาง (km)", min_value=0.0, key="ev_distance")

        st.write("กรอกราคาค่าไฟฟ้า (บาท/kWh)")
        electricity_price = st.number_input("ราคาค่าไฟฟ้า (บาท/kWh)", min_value=0.0, key="electricity_price")

    # Select Gasoline Car Brand and Model
    with col2:
        st.header("รถใช้น้ำมัน")
        gas_car_brand = st.selectbox("เลือกยี่ห้อรถน้ำมัน", [brand for brand in car_data if car_data[brand][list(car_data[brand].keys())[0]]['type'] == 'Gasoline'])
        gas_car_model = st.selectbox("เลือกรุ่นรถน้ำมัน", list(car_data[gas_car_brand].keys()))

        gas_car_info = car_data[gas_car_brand][gas_car_model]
        st.write(f"คุณเลือกรถใช้น้ำมัน: {gas_car_brand} {gas_car_model}")
        st.write(f"อัตราสิ้นเปลืองน้ำมัน: {gas_car_info['fuel_efficiency']} กม./ลิตร")
        st.write(f"ประเภทน้ำมัน: {gas_car_info['fuel_type']}")

        # Add types of Gasohol available in Thailand
        st.write("เลือกประเภท Gasohol")
        fuel_type = st.selectbox("ประเภทน้ำมัน", ["Gasohol 91", "Gasohol 95", "E20", "E85", "Benzene", "Diesel"])

        # Input for the price of fuel
        st.write("กรอกราคาน้ำมัน (บาท/ลิตร)")
        fuel_price = st.number_input("ราคาน้ำมัน (บาท/ลิตร)", min_value=0.0, key="fuel_price")

        st.write("กรอกความเร็วปกติของรถ (กม./ชม.)")
        gas_speed = st.number_input("ความเร็ว (km/h)", min_value=0.0, key="gas_speed")

        st.write("กรอกระยะทางที่เดินทาง (กม.)")
        gas_distance = st.number_input("ระยะทาง (km)", min_value=0.0, key="gas_distance")

    # Perform calculation and comparison
    if st.button("คำนวณ"):
        # EV calculation
        if ev_distance > 0:
            ev_efficiency = ev_car_info['battery'] / ev_car_info['range']
            ev_total_cost = ev_efficiency * ev_distance * electricity_price
        else:
            ev_efficiency = 0
            ev_total_cost = 0
        
        # Gasoline calculation
        if gas_distance > 0:
            gas_efficiency = gas_distance / gas_car_info['fuel_efficiency']
            gas_total_cost = gas_efficiency * fuel_price
        else:
            gas_efficiency = 0
            gas_total_cost = 0
        
        # Display results
        st.subheader("ผลลัพธ์การคำนวณ")
        
        st.write(f"**รถไฟฟ้า ({ev_car_brand} {ev_car_model})**")
        st.write(f"ประสิทธิภาพ: {ev_efficiency:.2f} kWh/กม.")
        st.write(f"ค่าใช้จ่ายรวม: {ev_total_cost:.2f} บาท")

        st.write(f"**รถใช้น้ำมัน ({gas_car_brand} {gas_car_model})**")
        st.write(f"ประสิทธิภาพ: {gas_car_info['fuel_efficiency']} กม./ลิตร")
        st.write(f"ค่าใช้จ่ายรวม: {gas_total_cost:.2f} บาท")

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
