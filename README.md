Vehicle Calculation Program
This Python program provides three main functionalities related to vehicle performance and fuel consumption. The user can calculate travel time, fuel consumption, wheel speed in revolutions per minute (RPM), and horsepower.

Features
Calculate Speed, Time, Fuel Quantity, and Fuel Cost:

This function calculates the travel time, fuel required, and fuel cost based on the input distance, speed, and fuel price.
Calculate Wheel Speed in Revolutions per Minute (RPM):

This function calculates the wheel speed in revolutions per minute based on the distance covered by the wheel and the time taken.
Calculate Horsepower:

This function calculates the horsepower based on the vehicle's weight and the time taken to cover a certain distance.
Prerequisites
Python 3.x must be installed on your system.
Import the math library, which is useful for future extensions of this program. Although this program currently does not require math, it can be used for more complex calculations like trigonometric functions, square roots, or logarithms.
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/Waramate-PHET/Oil-vs-electrical
Run the script:

Copy code
python app2.py
Main Menu:

The program will display a menu with the following options:
Calculate speed, time, fuel quantity, and fuel cost.
Calculate wheel speed in RPM.
Calculate horsepower.
Exit the program.
Example:

When you select option 1, you will be prompted to enter the distance (in kilometers), speed (in kilometers per hour), and fuel price (in baht per liter). The program will then calculate and display the time required for the trip, the amount of fuel used, and the total fuel cost.
Code Structure
The menu() function provides an interactive menu to choose the desired calculation.
The คำนวณความเร็วเวลาและปริมาณค่าน้ำมัน() function handles the calculation of speed, time, and fuel cost.
The คำนวณความเร็วรถเป็นรอบต่อนาทีของล้อต่อนาที() function calculates the vehicle's wheel speed in RPM.
The คำนวณแรงม้า() function calculates the horsepower based on the vehicle's weight and travel time.
Example Output
makefile
Copy code
เลือกฟังก์ชันที่ต้องการใช้:
1. คำนวณความเร็ว เวลา ปริมาณและค่าน้ำมันตามระยะทาง
2. คำนวณความเร็วรถเป็นรอบต่อนาทีของล้อต่อนาที
3. คำนวณแรงม้า
4. ออกจากโปรแกรม
ป้อนหมายเลข (1-4): 1

======== คำนวณความเร็ว เวลา ปริมาณและค่าน้ำมันตามระยะทาง ========
ป้อนระยะทาง (กิโลเมตร): 150
ป้อนความเร็ว (กิโลเมตรต่อชั่วโมง): 60
เวลาที่ใช้ในการเดินทาง: 2.50 ชั่วโมง
ปริมาณน้ำมันที่ใช้ในการเดินทาง: 12.50 ลิตร
ป้อนราคาน้ำมัน (บาทต่อลิตร): 35
ค่าน้ำมันที่ใช้ในการเดินทาง: 437.50 บาท