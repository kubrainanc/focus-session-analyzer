*Focus Session Analyzer

This is a simple Python command-line project that tracks focus or study sessions and analyzes productivity.

The program allows the user to record focus sessions with start time, end time, label (like study, reading, etc.), and a productivity score. The data is saved into a CSV file and later analyzed to generate insights and charts.

*Project Purpose

The goal of this project is to practice basic Python programming and simple data analysis.

While building this project I practiced:
	•	Working with user input in Python
	•	Saving and reading data from CSV files
	•	Using pandas for data analysis
	•	Creating charts using matplotlib
	•	Organizing a small Python project into multiple files

*Features

The program includes the following features:
	•	Add a new focus session
	•	Save sessions into a CSV file
	•	Display the last 10 recorded sessions
	•	Analyze session data
	•	Generate productivity charts automatically

*How the Program Works

When the program runs, the user sees a simple menu:
	1.	Add session
	2.	Show last 10 sessions
	3.	Analyze sessions and generate charts
	4.	Exit

If the user selects Add session, the program asks for:
	•	Date
	•	Start time
	•	End time
	•	Label (example: study, coding, reading)
	•	Productivity score from 1 to 5

The session duration is calculated automatically and stored in a CSV file.

*Data Analysis

When the user selects Analyze + charts, the program calculates:
	•	Total focus time
	•	Average session length
	•	Best start hour based on productivity
	•	Best label/topic based on productivity

The program also generates charts using matplotlib.

*Generated Charts

The analysis creates the following charts:
	•	Average productivity by start hour
	•	Total focus minutes by weekday
	•	Average productivity by label

These charts are automatically saved in the reports folder.

*Project Structure
focus-session-analyzer
│
├── data
│   └── sessions.csv
│
├── reports
│   ├── avg_productivity_by_hour.png
│   ├── minutes_by_weekday.png
│   └── avg_productivity_by_label.png
│
└── src
    ├── main.py
    └── analysis.py

*Technologies Used
Python
Pandas
Matplotlib

*Future Improvements
Possible improvements for this project:
	•	Adding a graphical interface
	•	Exporting analysis results into a report
	•	Adding more statistics about productivity
	•	Tracking weekly or monthly progress
