from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

def is_leap_year(year):
    # Check if the year is a leap year
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def dayfinder(day_of_year):
    if 1 <= day_of_year <= 28:
        month = "Boozer"
        start_day = 1
    elif 29 <= day_of_year <= 56:
        month = "Chipper"
        start_day = 29
    elif 57 <= day_of_year <= 84:
        month = "Kucheeder"
        start_day = 57
    elif 85 <= day_of_year <= 112:
        month = "Warder"
        start_day = 85
    elif 113 <= day_of_year <= 140:
        month = "Forgorder"
        start_day = 113
    elif 141 <= day_of_year <= 168:
        month = "Crabber"
        start_day = 141
    elif 169 <= day_of_year <= 196:
        month = "Monker"
        start_day = 169
    elif 197 <= day_of_year <= 224:
        month = "Mechanicer"
        start_day = 197
    elif 225 <= day_of_year <= 252:
        month = "Ferrer"
        start_day = 225
    elif 253 <= day_of_year <= 280:
        month = "Penner"
        start_day = 253
    elif 281 <= day_of_year <= 308:
        month = "Juler"
        start_day = 281
    elif 309 <= day_of_year <= 336:
        month = "Slother"
        start_day = 309
    else:
        month = "Skiver"
        start_day = 337

    day_of_month = day_of_year - start_day + 1
    last_digit = day_of_year % 10
    day_of_week = {
        1: "murday",
        2: "duoday",
        3: "tresday",
        4: "issiday",
        5: "wensday",
        6: "sexday",
        7: "curryday",
        8: "friday",
        9: "saturday",
        0: "verday"
    }.get(last_digit, "unknown")
    return month, day_of_month, day_of_week

@app.route("/", methods=["GET", "POST"])
def show_date():
    output_text = ""
    if request.method == "POST":
        # Get month, day, and year from the form
        month = int(request.form.get("month", 1))
        day = int(request.form.get("day", 1))
        year = int(request.form.get("year", datetime.now().year))
        
        # Calculate the day of the year for the Gregorian date
        try:
            gregorian_date = datetime(year, month, day)
            day_of_year = gregorian_date.timetuple().tm_yday
            


            custom_month, custom_day_of_month, custom_day_of_week = dayfinder(day_of_year)
            
            # Determine suffix for the day
            if 11 <= custom_day_of_month <= 13:
                suffix = "th"
            else:
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(custom_day_of_month % 10, "th")
            
            output_text = f"The equivalent date is {custom_day_of_week}, the {custom_day_of_month}{suffix} of {custom_month}."
        
        except ValueError:
            output_text = "Invalid date! Please enter a valid Gregorian date."

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>What day is that?</title>
        <style>
            body {{
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #9066a5;
                font-family: Arial, sans-serif;
            }}
            h1 {{
                font-size: 2em;
                color: #ffffff;
                text-align: center;
            }}
            form {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 20px;
            }}
            label, input {{
                margin: 5px;
                font-size: 1.2em;
                color: #ffffff;
            }}
            button {{
                padding: 10px 20px;
                font-size: 1.2em;
                cursor: pointer;
            }}
            .output {{
                margin-top: 20px;
                font-size: 1.5em;
                color: #ffffff;
            }}
        </style>
    </head>
    <body>
        <h1>Date Converter</h1>
        <form method="POST">
            <label for="month">Month:</label>
            <input type="number" id="month" name="month" min="1" max="12" required>
            
            <label for="day">Day:</label>
            <input type="number" id="day" name="day" min="1" max="31" required>
            
            <label for="year">Year:</label>
            <input type="number" id="year" name="year" min="1" max="9999" required>
            
            <button type="submit">Convert</button>
        </form>
        
        <div class="output">{output_text}</div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
