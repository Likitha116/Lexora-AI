import warnings

warnings.filterwarnings(
    "ignore",
    category=FutureWarning
)
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Check your .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")


import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Check your .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config={
        "temperature": 0.2,
        "top_p": 0.9,
        "top_k": 40,
    }
)

def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text