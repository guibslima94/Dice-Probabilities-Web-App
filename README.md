# Dice Probability Calculator

A web application for calculating dice probabilities. This project has been converted from a tkinter GUI to a modern web application.

## Features

- Calculate the probability of rolling dice with specific target values
- Clean, modern web interface
- Real-time probability calculations

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:
```bash
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

## How to Use

1. Enter the **Number of Dices** you want to roll
2. Enter the **Target Value** (1-6) that you want to reach
3. Enter the **Number of Dices Reaching Target** (how many dice should reach or exceed the target)
4. Click **Calculate Probability** to see the result

The result will show both the decimal probability and percentage, and your last calculation will be displayed below.

