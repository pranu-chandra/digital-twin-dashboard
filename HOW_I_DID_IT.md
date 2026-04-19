## HOW I DID IT

I designed a personal digital twin dashboard to track key aspects of health and productivity such as sleep, energy, and stress.

To support the design, I implemented a simple Python-based agent (agent.py) that simulates how a digital twin system processes user data and generates insights.

The agent explicitly uses LPI tools such as:
- smile_overview
- get_insights
- query_knowledge

These tools are called within the code to represent how a real system would analyze patterns and generate recommendations.

I also implemented multiple layers of error handling, including:
- validation for negative input values
- handling missing or zero values
- checking for out-of-range inputs
- type validation for input consistency

To ensure transparency, I added a dedicated explainability function. When a recommendation is generated, the system clearly explains the reason behind it based on observed patterns (e.g., low sleep leading to reduced energy levels).

The main challenge was connecting UI design with backend logic. Initially, I focused only on the dashboard, but later I extended the project by adding an agent to demonstrate system behavior and decision-making.

If I continue improving this project, I would integrate real-time data, build an interactive prototype, and enhance the intelligence of recommendations using more advanced models.
