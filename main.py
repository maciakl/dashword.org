from flask import Flask
import random

Words = [
    "administration",
    "administrator",
    "agricultural",
    "approximately",
    "championship",
    "characteristic",
    "characterize",
    "circumstance",
    "communication",
    "comprehensive",
    "concentration",
    "congressional",
    "consciousness",
    "considerable",
    "consideration",
    "constitutional",
    "construction",
    "contemporary",
    "contribution",
    "controversial",
    "conventional",
    "conversation",
    "correspondent",
    "demonstration",
    "discrimination",
    "distribution",
    "dramatically",
    "entertainment",
    "environmental",
    "establishment",
    "extraordinary",
    "headquarters",
    "identification",
    "increasingly",
    "independence",
    "institutional",
    "intellectual",
    "intelligence",
    "international",
    "interpretation",
    "intervention",
    "introduction",
    "investigation",
    "investigator",
    "manufacturer",
    "manufacturing",
    "neighborhood",
    "nevertheless",
    "occasionally",
    "organization",
    "participation",
    "particularly",
    "photographer",
    "prescription",
    "presentation",
    "presidential",
    "professional",
    "recommendation",
    "relationship",
    "representation",
    "representative",
    "responsibility",
    "satisfaction",
    "significance",
    "significantly",
    "sophisticated",
    "specifically",
    "successfully",
    "surprisingly",
    "transformation",
    "transportation",
    "understanding",
    "unfortunately"
    ]

Html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>dashword.org</title>
    <link rel="icon"
      href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🔐</text></svg>">
    <style>
        body {{
            font-family: Consolas, Monaco, monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }}
        .dashword {{
            font-size:5vw;
            color: #333;
        }}
        footer {{
            position: fixed;
            bottom: 10px;
            font-size: 1em;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="dashword">{word}</div>
    <footer>dashword.org &copy; Luke Maciak 2026</footer>
</body>
</html>"""

app = Flask(__name__)


@app.route("/")
def main():
    return dashword()


def dashword():
    number = random.randint(100, 999)
    word = random.choice(Words).capitalize()
    dashword = word + "-" + str(number)
    out = Html.format(word=dashword)
    return out


if __name__ == "__main__":
    app.run(debug=True)
