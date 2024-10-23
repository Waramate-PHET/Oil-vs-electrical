ถที่ใช้น้ำมัน vs รถใช้ไฟฟ้า (Oil vs Electric Vehicle Comparison)
Overview
This is a Streamlit web app that allows users to compare the performance and cost of electric vehicles (EV) versus gasoline-powered vehicles. The app takes into account factors such as battery capacity, fuel efficiency, distance traveled, and electricity/fuel costs to calculate and compare the overall cost of using both types of vehicles.

The app features:

Car selection for both EV and gasoline vehicles.
Calculation of cost for electricity and fuel based on user input.
A visitor counter that tracks the number of users who visited the app.
A clean and interactive user interface for input and results comparison.
Features
Electric Vehicle Comparison: Allows users to select EVs from a predefined list and calculate their cost based on distance traveled and electricity price.
Gasoline Vehicle Comparison: Users can select gasoline cars and calculate fuel costs based on distance traveled and fuel efficiency.
Comparison Results: Displays the efficiency and total cost for both vehicle types side by side, making it easy to compare which vehicle is more cost-effective.
Visitor Counter: Tracks and displays the number of visitors to the app.
Demo
Check out a live version of the app here: Streamlit App ([add link if hosted](https://car-oil-vs-car-electrical.streamlit.app/))

Getting Started
Prerequisites
To run this app, you need to have the following installed:

Python 3.7+
Streamlit
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Waramate-PHET/Oil-vs-electrical
cd oil-vs-electric-vehicle-comparison
Install the required Python packages:

Use the following command to install the necessary dependencies listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
Run the app:

Start the Streamlit app by running:

bash
Copy code
streamlit run app.py
Access the app:

After running the above command, Streamlit will provide a URL, typically http://localhost:8501/. Open this URL in your web browser to access the app.

File Structure
bash
Copy code
.
├── app.py                     # Main Streamlit app
├── requirements.txt            # Required packages for the app
├── README.md                   # Project documentation (this file)
└── assets/                     # Folder for storing additional assets (if any)
Background Image
The background image for the app is fetched dynamically from the following URL:

bash
Copy code
https://images-storage.thaiware.site/tips/2020_11/images/1433_20111714250002_67.png
You can modify or change the background image in the app.py file within the add_bg_from_url() function.

Usage
Choose a brand and model for both the Electric Vehicle and Gasoline Vehicle.
Input the travel distance, electricity price, and fuel price.
Click the Calculate button to compare the efficiency and cost of the selected vehicles.
View the results displayed side by side.
Technologies Used
Python: The programming language used for the backend logic.
Streamlit: A framework for building interactive web applications in Python.
Requests: To fetch background images dynamically from a URL.
Base64: Used for encoding images to display them in the app.
Future Improvements
Adding more car brands and models to the comparison list.
Implementing real-time fuel price fetching from external APIs.
Adding charts and visualizations to make comparisons more intuitive.
Allowing users to export comparison results as a PDF or Excel file.
Contributing
Contributions are welcome! If you have suggestions for improving this app, please feel free to submit an issue or a pull request.

Fork the project.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.