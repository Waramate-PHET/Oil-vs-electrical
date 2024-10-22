import streamlit as st
import math

# Define the menu and the functions
def menu():
    st.title("Vehicle Calculator Application")
    st.write("Choose a function from the sidebar to start using the app:")

    # Sidebar options
    choice = st.sidebar.selectbox("Select Function:", 
                                  ("Speed, Time, Fuel and Cost Calculation", 
                                   "Vehicle Speed in RPM Calculation", 
                                   "Horsepower Calculation", 
                                   "Exit"))

    if choice == "Speed, Time, Fuel and Cost Calculation":
        คำนวณความเร็วเวลาและปริมาณค่าน้ำมัน()
    elif choice == "Vehicle Speed in RPM Calculation":
        คำนวณความเร็วรถเป็นรอบต่อนาทีของล้อต่อนาที()
    elif choice == "Horsepower Calculation":
        คำนวณแรงม้า()
    elif choice == "Exit":
        st.write("Thank you for using the app!")

def คำนวณความเร็วเวลาและปริมาณค่าน้ำมัน():
    st.header("Speed, Time, Fuel and Cost Calculation")
    # Input fields
    distance = st.number_input("Enter distance (km):", min_value=0.0, step=0.1)
    speed = st.number_input("Enter speed (km/h):", min_value=0.0, step=0.1)

    if speed > 0:
        time = distance / speed
        fuel_quantity = distance / 12  # Assuming 12 km per liter
        fuel_price = st.number_input("Enter fuel price (Baht/liter):", min_value=0.0, step=0.1)

        # Calculate and display results
        if fuel_price >= 0:
            fuel_cost = fuel_quantity * fuel_price
            st.write(f"Time required for the trip: **{time:.2f} hours**")
            st.write(f"Fuel required: **{fuel_quantity:.2f} liters**")
            st.write(f"Fuel cost: **{fuel_cost:.2f} Baht**")
        else:
            st.error("Fuel price cannot be negative")
    else:
        st.warning("Speed must be greater than 0")

def คำนวณความเร็วรถเป็นรอบต่อนาทีของล้อต่อนาที():
    st.header("Vehicle Speed in RPM Calculation")
    # Input fields
    distance = st.number_input("Enter wheel rotation distance (meters):", min_value=0.0, step=0.1)
    time = st.number_input("Enter time for rotation (seconds):", min_value=0.0, step=0.1)

    if time > 0:
        speed_mps = distance / time
        wheel_circumference = 0.7  # Wheel circumference in meters
        wheel_speed_rpm = (speed_mps / wheel_circumference) * 60
        st.write(f"Wheel speed: **{wheel_speed_rpm:.2f} RPM**")
    else:
        st.warning("Time must be greater than 0")

def คำนวณแรงม้า():
    st.header("Horsepower Calculation")
    # Input fields
    weight = st.number_input("Enter vehicle weight (pounds):", min_value=0.0, step=0.1)
    time_seconds = st.number_input("Enter time (seconds):", min_value=0.0, step=0.1)

    if time_seconds > 0:
        horsepower = weight / ((time_seconds / 5.825) ** 3)
        st.write(f"Horsepower: **{horsepower:.2f} HP**")
    else:
        st.warning("Time must be greater than 0")

# Run the app
menu()