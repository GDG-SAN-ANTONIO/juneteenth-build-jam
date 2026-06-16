# PlainCare

**Pitch:** Confusing medical bills & transit gaps + Gemini → a clear, actionable neighborhood health plan.

## What you'll build (45 minutes)
Type in a complex health or logistics hurdle (e.g., "I have a $2,000 ER bill and no car to get to the food pantry"). The AI translates the medical jargon, assesses the community logistics, and generates a simple, 2-step Action Plan connecting the user to charity care and local mutual aid transit.

## The moment it clicks
*"It didn't just tell me to eat healthy; it told me what time the mobile pantry stops at the church."*

## Things to think about
- **No real medical advice today.** Ensure your system prompt has strict guardrails. Focus on *navigation* and *logistics*, not diagnosis.
- **Your signature detail.** How do you present the information? Is it an SMS-style chatbot, or a printed "prescription" checklist?
- **Test with a fake bill.** Grab a sample medical invoice online and paste the confusing line items to see if the AI can translate them into plain English.

## Where to take it after the jam (Polished Version)
- Twilio integration for SMS-based interaction (for folks without smartphones)
- Live transit API integration to check bus schedules
- Multi-language translation for non-English speaking households
- Document upload feature to OCR actual paper bills
- Local database integration of active community pantries

## Tech you'll touch
- Antigravity (AI-driven IDE)
- Python + google-genai SDK (backend)
- Google Gemini API (Complex jargon translation & logistical reasoning)
- HTML / CSS / JS (frontend)
