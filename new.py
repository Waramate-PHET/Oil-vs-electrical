import streamlit as st
import math

# Function to track the number of visits
def update_visit_count():
    if 'visit_count' not in st.session_state:
        st.session_state['visit_count'] = 1
    else:
        st.session_state['visit_count'] += 1

# Add background image and styling adjustments for bright background
def add_custom_css():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images-storage.thaiware.site/tips/2020_11/images/1433_20111714250002_67.png");
             background-size: cover;
             background-position: center;
             background-repeat: no-repeat;
             background-attachment: fixed;
             color: #000000;  /* Dark color for good contrast with bright background */
         }}
         .stButton > button {{
             background-color: #FF6347;  /* Tomato color for buttons */
             color: black;
             padding: 10px 20px;
             border: none;
             border-radius: 8px;
             text-align: center;
             text-decoration: none;
             display: inline-block;
             font-size: 16px;
         }}
         .stButton > button:hover {{
             background-color: #FF4500;  /* Darker shade of tomato */
         }}
         h1, h2, h3, h4, h5 {{
             color: #000000 !important;  /* Ensure headers are dark */
         }}
         .stTextInput > div > div > input {{
             color: #000000; /* Make sure input text is visible and black */
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Define the functions
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

# Main menu with buttons
def menu():
    # Replace st.title with st.markdown for colored title
    st.markdown("<h1 style='color: #000000;'>Vehicle Calculator Application</h1>", unsafe_allow_html=True)

    # Display visit count with colored text
    st.markdown(f"<h4 style='color: #000000;'>Number of visits to the app: {st.session_state['visit_count']}</h4>", unsafe_allow_html=True)

    # Add colored heading for functionality selection
    st.markdown("<h3 style='color: #000000;'>Choose a function below:</h3>", unsafe_allow_html=True) 
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Speed, Time, Fuel and Cost Calculation"):
            คำนวณความเร็วเวลาและปริมาณค่าน้ำมัน()
    
    with col2:
        if st.button("Vehicle Speed in RPM Calculation"):
            คำนวณความเร็วรถเป็นรอบต่อนาทีของล้อต่อนาที()
    
    with col3:
        if st.button("Horsepower Calculation"):
            คำนวณแรงม้า()

# Run the app
if __name__ == "__main__":
    add_custom_css()  # Add custom styling
    update_visit_count()  # Track the number of visits
    menu()
