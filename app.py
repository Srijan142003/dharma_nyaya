from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv
from prompt_engine import build_prompt

load_dotenv()

app = Flask(__name__)

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-2.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        plaintiff = request.form["plaintiff"]
        defendant = request.form["defendant"]
        facts = request.form["facts"]

        prompt = build_prompt(plaintiff, defendant, facts)

        response = model.generate_content(prompt)
        verdict = response.text

        return render_template("result.html", verdict=verdict)
    except Exception as e:
        return render_template("result.html", verdict=f"Error: {str(e)}<br><br>Please try again or check your API key.")

if __name__ == "__main__":
    app.run(debug=True)
