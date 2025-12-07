# Dice Probability Calculator

A modern web application for calculating dice probabilities. This project was converted from a tkinter GUI to a full-stack web application with a clean, responsive interface.

## Features

- 🎲 Calculate probabilities for multiple dice rolls
- 🎨 Modern, responsive web interface
- ⚡ Real-time probability calculations via REST API
- 📊 Results displayed as both decimal and percentage
- ✅ Input validation and error handling

## Technology Stack

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Math**: Python's `math.comb()` for combinatorial calculations

## Project Structure

```
dice-project/
├── app.py                 # Flask backend server
├── main.py                # Original tkinter version (for reference)
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   ├── css/
│   │   └── style.css    # Styling
│   └── js/
│       └── app.js        # Frontend JavaScript
└── README.md
```

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd dice-project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:
```bash
python app.py
```

The server will start on `http://localhost:5000`. Open this URL in your browser to use the application.

## How to Use

1. Enter the **Number of Dices** you want to roll
2. Enter the **Target Value** (1-6) that you want to reach
3. Enter the **Number of Dices Reaching Target** (how many dice should reach or exceed the target)
4. Click **Calculate Probability** to see the result

The result will show both the decimal probability and percentage, and your last calculation will be displayed below.

## API Endpoint

The application exposes a REST API endpoint:

**POST** `/api/calculate`

Request body:
```json
{
  "num_dices": 3,
  "target_value": 4,
  "num_dices_reaching_target": 2
}
```

Response:
```json
{
  "probability": 0.5,
  "probability_formatted": "0.5000"
}
```

## License

This project is open source and available for personal and educational use.

