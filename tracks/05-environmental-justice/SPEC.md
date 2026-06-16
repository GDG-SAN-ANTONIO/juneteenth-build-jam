# Block Scan

**Pitch:** A photo or text of a neighborhood hazard + Gemini → a drafted, formal 311 service request or petition.

## What you'll build (45 minutes)
Describe a neighborhood environmental hazard (like a chemical smell or a massive illegal tire dump). The AI classifies the violation (e.g., Clean Air Act, Public Health Hazard) and instantly drafts a formal, structured service request or petition ready to be sent to Code Enforcement or the EPA.

## The moment it clicks
*"It turned my angry rant about the smell into a perfectly formatted, legally-sound EPA petition."*

## Things to think about
- **Keep the output format strict.** The magic is in making the output look like a real ticket. Instruct Gemini to use headers, bullet points, and a formal tone.
- **Your signature detail.** Does it generate a single email, a mass petition, or a social media blast? Decide on the medium.
- **Test with a vague description.** "It smells weird near the train tracks" — see if the AI asks clarifying questions or defaults to a general environmental complaint.

## Where to take it after the jam (Polished Version)
- Image upload (Gemini Vision) to analyze photos of the hazard
- Direct email integration via SendGrid to actually file the 311 ticket
- Geolocation API to auto-fill the address
- Heatmap dashboard showing where the most tickets are generated
- AI generated follow-up scripts for calling the city

## Tech you'll touch
- Antigravity (AI-driven IDE)
- Python + google-genai SDK (backend)
- Google Gemini API (Classification and formal text generation)
- HTML / CSS / JS (frontend)
