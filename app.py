from spam_detector import SpamDetector
from call_features import extract_features

# Sample call data (fake data for learning)
calls = [
    {
        "duration": 10,
        "call_frequency": 15,
        "unknown_number": 1,
        "international_call": 1
    },
    {
        "duration": 300,
        "call_frequency": 1,
        "unknown_number": 0,
        "international_call": 0
    }
]

# Labels: 1 = Spam, 0 = Genuine
labels = [1, 0]

# Convert call data into numbers
X = [extract_features(call) for call in calls]

# Create and train AI model
detector = SpamDetector()
detector.train(X, labels)

# Predict results
result = detector.predict(X)
print("Prediction (1 = Spam, 0 = Genuine):", result)