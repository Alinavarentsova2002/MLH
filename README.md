# Water Tracker

A simple web application built with Flask that allows users to track their daily water intake. The app includes user authentication and CRUD operations for water entries.

## Features

- User registration and login
- Track daily water intake
- View past entries
- Responsive design

## Setup

1. Clone the repository:
    git clone https://github.com/your-username/water-tracker.git
    cd water-tracker

2. Set up a virtual environment:
    python3 -m venv venv
    source venv/bin/activate

3. Install the required packages:
 and initialize the databasepython init_db.py
    pip install -r requirements.txt
   pip install email_validator
   pip install --upgrade watchdog

6. Run the application:
    python run.py

## Technologies Used

- Flask
- SQLAlchemy
- Flask-WTF
- Flask-Bcrypt
- Flask-Login
