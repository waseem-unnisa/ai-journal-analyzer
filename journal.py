from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

model = "gemini-2.5-flash"

def get_journal_entry():
    line = []
    while True:
        text = input("Enter text:")
        if text == "":
            break
        line.append(text)
    result = "\n".join(line)
    return result

def analyze_journal(entry):
    prompt = f"""
    You are a Journal Analyzer. The user has written a journal entry. Analyze their emotions, identify their feelings, 
    and give them supportive, encouraging and show empathy hepl them feel better and improve their day.
    
    A user has written the following journal entry:
   {entry}

   Please respond in this format:
   1. MOOD: (detected mood in 2-3 words)
   2.FEELINGS: (2-3 sentences about what the user is feeling)
   3.SUGGESTIONS: (3 practical and kind suggestions to help them feel better)
    """
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt
)
    return response.text

def main():
 print("Welcome to AI Journal Analyzer")
 user_journal =  get_journal_entry()
 result = analyze_journal(user_journal)
 print(result)

if __name__ == "__main__":
    main()

