import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    # 1. Initialize the client (Make sure you set GEMINI_API_KEY in your .env file)
    client = genai.Client()

    # 2. This is the persona for this track. Feel free to edit it!
    system_instruction = """You are a public health navigator. Your mission is to help residents overcome barriers in food deserts and medical access. Analyze user descriptions of their situation or location, and map their needs to actionable public health resources, translating complex jargon into clear, empathetic next steps."""

    print("Welcome to the Juneteenth Build Jam Starter Kit!")
    print("-" * 50)
    
    # 3. Get the user's input
    user_input = input("Enter your description or issue: ")

    # 4. Generate the response
    print("\nGenerating response...\n")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
        ),
    )

    print(response.text)

if __name__ == "__main__":
    main()
