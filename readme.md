# Smart Food Decision Engine

## Problem
Most food apps track calories but do not help users make real-time decisions.

## Solution
This system uses context (time, previous meals, user intent) to suggest optimal food choices.

## Features
- Context-aware recommendations
- AI-powered reasoning using Google Gemini
- Nearby food discovery using Google Maps

## Tech Stack
- Python (Streamlit)
- Google Gemini API
- Google Maps Places API

## How It Works
1. User enters situation
2. Context is extracted
3. Gemini generates smart recommendations
4. Nearby restaurants are suggested

## Assumptions
- User location default set to Delhi
- Context inferred from keywords

## Future Improvements
- Personal history tracking
- Nutrition scoring
- Real-time ordering integration