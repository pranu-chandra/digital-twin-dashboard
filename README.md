# LifeTwin – Personal Digital Twin Dashboard

This project is a UI/UX design concept for a personal digital twin system built as part of the LifeAtlas LPI Developer Kit (Level 3 – Design & UX Track).

## Features
- Tracks key personal metrics such as sleep, activity, nutrition, and stress
- Displays overall health score and daily performance indicators
- Visualizes trends using charts and graphs
- Provides insights and actionable recommendations
- Clean and intuitive dashboard layout for quick understanding

## How it works
The dashboard represents how a digital twin system could collect and process personal data such as sleep hours, physical activity, and stress levels.

This data is then analyzed to:
- Identify patterns in user behavior
- Highlight strengths and weak areas
- Generate insights
- Suggest improvements through recommendations

## SMILE Methodology (Conceptual)
This design is inspired by the SMILE framework:

- **Reality Capture** → Collect user data (sleep, steps, stress)
- **Modeling** → Represent data in structured dashboard form
- **Simulation** → Analyze trends and possible outcomes
- **Insights** → Identify patterns from user behavior
- **Learning** → Improve understanding of habits
- **Evolution** → Enable continuous personal improvement

## LPI Tools (Conceptual Reference)
The design was guided using concepts from LPI tools:

- `smile_overview` → Understanding the lifecycle structure
- `get_insights` → Designing insight generation
- `query_knowledge` → Structuring meaningful outputs

These tools influenced how insights and recommendations are presented in the UI.

## Example Insight
Input:
Sleep = 6 hours  
Stress = High  
Activity = Low  

Output:
"Your energy levels may drop in the afternoon due to insufficient sleep. Consider improving sleep duration and taking short breaks."

## Explainability
If a user asks:
**"Why is this recommendation given?"**

The system responds:
"This recommendation is based on observed patterns where lower sleep duration correlates with reduced energy and productivity. Improving sleep can enhance performance."

This ensures transparency and trust in the system.

## Design Approach
- Focused on simplicity and clarity
- Avoided clutter by limiting unnecessary metrics
- Used visual hierarchy to highlight important data
- Designed for non-technical users to understand quickly

## Setup
This is a design prototype created using Figma.

Figma Design Link:
https://www.figma.com/design/5taT2q8AHdeYHWxTAPCj3R/Untitled?node-id=0-1&t=ZqvQPug9TjDNTwTs-1

## Future Improvements
- Add interactive prototype
- Connect real-time data sources
- Integrate AI-driven predictions
- Build a functional backend system
- 
## Code Implementation

This project includes a simple agent (`agent.py`) that simulates how a digital twin system processes user inputs and generates insights.

The agent:
- Accepts inputs like sleep, energy, and stress
- Calls LPI tools such as `smile_overview` and `get_insights`
- Generates insights based on patterns

## Example Run

Input:
sleep = 6, energy = 5, stress = 7

Output:
"Low sleep detected. This may reduce your energy levels."

## Explainability

If a user asks "Why this recommendation?", the system explains:

"This recommendation is based on observed patterns where lower sleep leads to reduced energy and performance."
