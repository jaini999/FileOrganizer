import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CATEGORIES = ["Finance", "College", "Others"]

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

def classify_text(text):
    # Handle empty or low-content input
    if not text or len(text.strip()) < 50:
        return "Others"
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY environment variable not set.")
    prompt = (
        "You are a document and media classifier. "
        "Classify the following content into one of these categories: Finance, College, Others. "
        "If the content is related to computer science, engineering, or technology education, classify it as College. "
        "If the content is related to financial documents, banking, or money matters, classify it as Finance. "
        "For audio/video files, consider: educational content goes to College, entertainment goes to Others, financial content goes to Finance. "
        "Respond with only the category name.\n\n"
        f"Content:\n{text}\n\nCategory:"
    )
    try:
        print('Calling Gemini SDK...')
        response = model.generate_content(prompt)
        print('RAW GEMINI SDK RESPONSE:', response.text, flush=True)
        category = response.text.strip()
        # Normalize and validate
        for cat in CATEGORIES:
            if cat.lower() in category.lower():
                return cat
        return "Others"
    except Exception as e:
        print('Exception occurred:', repr(e), flush=True)
        return "Others"

# TODO: Implement Gemini API call for classification
# def classify_text(text):
#     pass 