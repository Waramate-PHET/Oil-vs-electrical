รถที่ใช้น้ำมัน vs รถใช้ไฟฟ้า (Oil vs Electric Vehicle Comparison)
---

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

----------------------------------------------------------------------------------------------------------------------------------------

รถที่ใช้น้ำมัน vs รถใช้ไฟฟ้า
---

ภาพรวม
โปรเจกต์นี้เป็นแอปพลิเคชัน Streamlit ที่ช่วยให้ผู้ใช้สามารถเปรียบเทียบประสิทธิภาพและค่าใช้จ่ายระหว่าง รถยนต์ไฟฟ้า (EV) และ รถยนต์ที่ใช้น้ำมัน โดยพิจารณาจากปัจจัยต่างๆ เช่น ความจุแบตเตอรี่, อัตราการสิ้นเปลืองน้ำมัน, ระยะทางที่เดินทาง, ราคาค่าไฟฟ้า และราคาน้ำมัน เพื่อนำมาคำนวณและเปรียบเทียบค่าใช้จ่ายทั้งหมด

ฟีเจอร์ของแอปนี้ประกอบด้วย:

การเลือกยี่ห้อและรุ่นของรถยนต์ไฟฟ้าและรถยนต์น้ำมัน
คำนวณค่าใช้จ่ายจากการเดินทางตามระยะทางและราคาค่าไฟฟ้าหรือน้ำมัน
มีระบบนับจำนวนผู้เข้าชม
อินเทอร์เฟซที่สวยงามและใช้งานง่าย
ฟีเจอร์
การเปรียบเทียบรถยนต์ไฟฟ้า: ให้ผู้ใช้เลือกยี่ห้อและรุ่นของรถยนต์ไฟฟ้า และคำนวณค่าใช้จ่ายตามระยะทางที่เดินทางและราคาค่าไฟฟ้า
การเปรียบเทียบรถยนต์ใช้น้ำมัน: ผู้ใช้สามารถเลือกยี่ห้อและรุ่นของรถยนต์ใช้น้ำมัน และคำนวณค่าใช้จ่ายตามระยะทางที่เดินทางและอัตราการสิ้นเปลืองน้ำมัน
ผลลัพธ์การเปรียบเทียบ: แสดงประสิทธิภาพและค่าใช้จ่ายของรถยนต์ทั้งสองประเภทเพื่อให้ผู้ใช้สามารถเปรียบเทียบได้ง่าย
ระบบนับจำนวนผู้เข้าชม: แสดงจำนวนผู้เข้าชมที่ใช้งานแอปนี้
สาธิต
สามารถเข้าชมเวอร์ชันตัวอย่างของแอปได้ที่นี่: Streamlit App ([เพิ่มลิงก์หากมีการโฮสต์](https://car-oil-vs-car-electrical.streamlit.app/))

เริ่มต้นการใช้งาน
สิ่งที่ต้องติดตั้งก่อน
ในการรันแอปนี้ คุณต้องติดตั้งซอฟต์แวร์ดังต่อไปนี้:

Python 3.7+
Streamlit
วิธีการติดตั้ง
Clone โครงการนี้:

bash
Copy code
git clone https://github.com/Waramate-PHET/Oil-vs-electrical?tab=readme-ov-file
cd oil-vs-electric-vehicle-comparison
ติดตั้งไลบรารีที่จำเป็น:

ใช้คำสั่งนี้เพื่อทำการติดตั้งไลบรารีที่จำเป็นจาก requirements.txt:

bash
Copy code
pip install -r requirements.txt
รันแอปพลิเคชัน:

เริ่มต้นแอปพลิเคชัน Streamlit โดยใช้คำสั่ง:

bash
Copy code
streamlit run app.py
เข้าใช้งานแอป:

หลังจากรันคำสั่งข้างต้น Streamlit จะให้ URL ซึ่งปกติจะเป็น http://localhost:8501/ ให้คุณเปิด URL นี้ในเว็บเบราว์เซอร์เพื่อใช้งานแอป

โครงสร้างของไฟล์
bash
Copy code
.
├── app.py                     # ไฟล์หลักของ Streamlit app
├── requirements.txt            # ไลบรารีที่จำเป็นสำหรับแอป
├── README.md                   # ไฟล์เอกสารโปรเจกต์ (ไฟล์นี้)
└── assets/                     # โฟลเดอร์สำหรับเก็บไฟล์ที่เกี่ยวข้อง (ถ้ามี)
ภาพพื้นหลัง
แอปพลิเคชันนี้ดึงภาพพื้นหลังแบบไดนามิกจาก URL ดังนี้:

bash
Copy code
https://images-storage.thaiware.site/tips/2020_11/images/1433_20111714250002_67.png
คุณสามารถเปลี่ยนแปลงหรือแก้ไขภาพพื้นหลังได้ในฟังก์ชัน add_bg_from_url() ภายในไฟล์ app.py

วิธีการใช้งาน
เลือกยี่ห้อและรุ่นของรถยนต์ไฟฟ้าและรถยนต์ที่ใช้น้ำมัน
ป้อนระยะทางที่เดินทาง ราคาค่าไฟฟ้า และราคาน้ำมัน
กดปุ่ม คำนวณ เพื่อเปรียบเทียบประสิทธิภาพและค่าใช้จ่ายของรถยนต์ทั้งสองประเภท
ผลลัพธ์จะแสดงการเปรียบเทียบแบบเคียงข้างกัน
เทคโนโลยีที่ใช้
Python: ภาษาโปรแกรมหลักที่ใช้ในการพัฒนา
Streamlit: Framework สำหรับสร้างแอปพลิเคชันเว็บแบบโต้ตอบ
Requests: ใช้ดึงภาพพื้นหลังจาก URL แบบไดนามิก
Base64: ใช้ในการเข้ารหัสภาพเพื่อแสดงในแอป
การปรับปรุงในอนาคต
เพิ่มยี่ห้อและรุ่นของรถยนต์ให้มากขึ้น
ดึงราคาน้ำมันแบบเรียลไทม์จาก API ภายนอก
เพิ่มกราฟและการแสดงผลที่เข้าใจง่ายขึ้น
เพิ่มฟังก์ชันให้ผู้ใช้สามารถดาวน์โหลดผลลัพธ์การเปรียบเทียบในรูปแบบ PDF หรือ Excel
การร่วมพัฒนา
หากคุณต้องการร่วมพัฒนาและปรับปรุงแอปนี้ สามารถทำได้โดยการ Fork โครงการนี้ และเปิด Pull Request

Fork โปรเจกต์นี้
สร้าง branch ของคุณ (git checkout -b feature/AmazingFeature)
Commit การเปลี่ยนแปลง (git commit -m 'Add some AmazingFeature')
Push ไปยัง branch ของคุณ (git push origin feature/AmazingFeature)
เปิด Pull Request
ใบอนุญาต
โปรเจกต์นี้อยู่ภายใต้การอนุญาตแบบ MIT License สามารถดูรายละเอียดได้ที่ไฟล์ LICENSE