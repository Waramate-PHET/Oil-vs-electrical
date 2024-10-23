import streamlit as st

# Set up the Streamlit session state for navigation
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

def main():
    if st.session_state['page'] == 'home':
        home_page()
    elif st.session_state['page'] == 'electric':
        electric_vehicle_page()
    elif st.session_state['page'] == 'gasoline':
        gasoline_vehicle_page()

# Home page: Choose between Electric or Gasoline vehicle
def home_page():
    st.title("รถที่ใช้น้ำมัน vs รถใช้ไฟฟ้า")
    
    st.write("คำอธิบายว่า คุณต้องการทราบว่า รถไฟฟ้า หรือ รถน้ำมัน แบบไหน ดีกว่ากัน")
    
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button('รถใช้ไฟฟ้า'):
            st.session_state['page'] = 'electric'
    with col2:
        if st.button('รถใช้น้ำมัน'):
            st.session_state['page'] = 'gasoline'

# Electric vehicle calculation page
def electric_vehicle_page():
    st.title("รถใช้ไฟฟ้า")

    # Input fields
    st.write("กรอกความจุเชื้อเพลิงของตัวรถ")
    battery_capacity = st.number_input("กรอกความจุแบตเตอรี่ (kWh)", min_value=0)

    st.write("กรอกระยะทางที่รถไปได้")
    distance = st.number_input("ระยะทางที่รถสามารถวิ่งได้ (กิโลเมตร)", min_value=0)

    st.write("แสดงความเร็วปกติของตัวรถที่วิ่ง")
    speed = st.number_input("ความเร็วเฉลี่ย (กม./ชม.)", min_value=0)

    if st.button("คำนวณ"):
        # Calculation for electric vehicle
        efficiency = battery_capacity / distance if distance > 0 else 0
        st.write(f"ประสิทธิภาพของรถ (kWh/กิโลเมตร): {efficiency}")

# Gasoline vehicle calculation page
def gasoline_vehicle_page():
    st.title("รถใช้น้ำมัน")

    # Input fields
    st.write("กรอกความจุเชื้อเพลิงของตัวรถ")
    fuel_capacity = st.number_input("กรอกความจุถังน้ำมัน (ลิตร)", min_value=0)

    st.write("กรอกระยะทางที่รถไปได้")
    distance = st.number_input("ระยะทางที่รถสามารถวิ่งได้ (กิโลเมตร)", min_value=0)

    st.write("แสดงความเร็วปกติของตัวรถที่วิ่ง")
    speed = st.number_input("ความเร็วเฉลี่ย (กม./ชม.)", min_value=0)

    st.write("กรอกราคาที่เราต้องการเติม")
    fuel_price = st.number_input("ราคาน้ำมัน (บาท/ลิตร)", min_value=0)

    if st.button("คำนวณ"):
        # Calculation for gasoline vehicle
        efficiency = fuel_capacity / distance if distance > 0 else 0
        fuel_cost = fuel_capacity * fuel_price
        st.write(f"ประสิทธิภาพของรถ (ลิตร/กิโลเมตร): {efficiency}")
        st.write(f"ค่าใช้จ่ายน้ำมัน (บาท): {fuel_cost}")

# Run the app
if __name__ == '__main__':
    main()
