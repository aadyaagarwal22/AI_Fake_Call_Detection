from flask import Flask, request, render_template_string
from spam_detector import SpamDetector

app = Flask(__name__)

model = SpamDetector()

# Sample training data
X_train = [
    [1, 10, 1],  # spam
    [1, 8, 1],   # spam
    [0, 1, 0],   # genuine
    [0, 2, 0]    # genuine
]

y_train = [1, 1, 0, 0]

model.train(X_train, y_train)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Fake Call Detection</title>
</head>
<body>
    <h2>AI Fake Call Detection</h2>
    <form method="post">
        Unknown Number (0 or 1): <input name="unknown"><br><br>
        Call Frequency: <input name="frequency"><br><br>
        Short Duration (0 or 1): <input name="duration"><br><br>
        <button type="submit">Predict</button>
    </form>

    {% if result %}
    <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        features = [[
            int(request.form["unknown"]),
            int(request.form["frequency"]),
            int(request.form["duration"])
        ]]
        prediction = model.predict(features)[0]
        result = "Spam Call 🚫" if prediction == 1 else "Genuine Call ✅"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)