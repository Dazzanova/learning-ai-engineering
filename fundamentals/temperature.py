import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

prompt = "Give me an unusual startup idea for software engineers."

temperatures = [0.1, 0.5, 1.0, 1.5]

for temperature in temperatures:
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=200,
        ),
    )

    print(f"\nTemperature: {temperature}")
    print(response.text)
    print("-" * 60)
