import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    # 1. Initialize the client (Make sure you set GEMINI_API_KEY in your .env file)
    client = genai.Client()

    # 2. This is the persona for this track. Feel free to edit it!
    system_instruction = """You are an expert economic consultant specializing in community wealth building and supporting minority-owned businesses. Your job is to take unstructured business descriptions or local data and turn them into optimized business plans, SEO-friendly descriptions, or match them to local civic grant eligibility criteria."""

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
