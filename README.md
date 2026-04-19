# LifeTwin – Personal Digital Twin Dashboard

This project is a Level 3 submission for the LifeAtlas LPI Developer Kit (Design & UX Track).

It represents a UI/UX design and a basic agent implementation for a personal digital twin system that tracks health and productivity metrics and provides actionable insights.

---

## Features

* Tracks sleep, activity, stress, and overall health
* Displays trends using charts and visual components
* Provides AI-like insights based on user data
* Generates actionable recommendations
* Clean and intuitive dashboard design for non-technical users

---

## How it Works

The system simulates a digital twin by:

1. Collecting user inputs such as sleep, energy, and stress
2. Processing this data using a simple agent
3. Calling LPI tools to understand patterns
4. Generating insights and recommendations

---

## SMILE Methodology (Conceptual)

This project is inspired by the SMILE framework:

* **Reality Capture** → Collect data (sleep, steps, stress)
* **Modeling** → Represent data in dashboard form
* **Simulation** → Analyze patterns
* **Insights** → Generate meaningful observations
* **Learning** → Improve understanding of habits
* **Evolution** → Suggest continuous improvement

---

## LPI Tool Usage

The agent explicitly calls LPI tools:

* `smile_overview` → Understands system structure
* `get_insights` → Generates insights from patterns

These tools are used inside `agent.py` to simulate how a digital twin system processes data.

---

## Code Implementation

The project includes a simple Python agent (`agent.py`) that:

* Accepts user inputs (sleep, energy, stress)
* Calls LPI tools using subprocess
* Processes responses
* Generates recommendations

### Example Tool Calls

* `smile_overview()`
* `get_insights()`

---

## Example Execution

### Input:

sleep = 5
energy = 4
stress = 7

### Output:

Recommendation: Improve sleep. Reason: Low sleep leads to reduced energy levels.

---

## Explainability

If a user asks:

**"Why is this recommendation given?"**

The system responds:

"This recommendation is based on observed patterns where lower sleep duration leads to reduced energy and productivity. Improving sleep can enhance performance."

This ensures transparency and trust in the system.

---

## Error Handling

The agent includes basic error handling:

* Handles invalid or missing inputs
* Uses try/except blocks to prevent crashes
* Returns meaningful error messages

---
## Execution Evidence

The agent connects to the LPI system and calls tools:

- smile_overview
- get_insights

Execution logs are provided in execution-log.txt.

## Design Approach

* Focused on simplicity and clarity
* Avoided clutter by limiting excessive metrics
* Used visual hierarchy to highlight key insights
* Designed for quick understanding by non-technical users

---

## Files Included

* `agent.py` → Basic agent with LPI tool calls
* `sample-output.txt` → Example output
* `HOW_I_DID_IT.md` → Explanation of approach
* `dashboard.png` → UI design

---

## Design Prototype

Figma Design Link:
(https://www.figma.com/design/5taT2q8AHdeYHWxTAPCj3R/Untitled?node-id=0-1&t=ZqvQPug9TjDNTwTs-1)

---

## Future Improvements

* Add real-time data integration
* Build interactive UI prototype
* Improve AI-based prediction logic
* Connect with backend services

---

## Author

Pranu Chandra
