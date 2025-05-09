import google.generativeai as genai

genai.configure(api_key="AIzaSyA0CR77I3MBuM0e9jisUgTD6suA_PWfaXU")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("What is Reliability Engineeriing?")
print(response.text)
