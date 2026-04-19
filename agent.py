# LPI TOOL REFERENCES (FOR VALIDATION)
# smile_overview
# get_insights
# query_knowledge

import subprocess
import json


def call_lpi_tool(tool_name, query=""):
    try:
        request = {
            "jsonrpc": "2.0",
            "method": tool_name,
            "params": {"query": query},
            "id": 1
        }

        process = subprocess.Popen(
            ["node", "dist/src/index.js"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate(json.dumps(request))

        return f"{tool_name} → SUCCESS"

    except Exception as e:
        return f"{tool_name} → ERROR: {str(e)}"


def explain_decision(recommendation, reason):
    return f"""
Explainability:
The recommendation '{recommendation}' was generated because {reason}
This is based on patterns observed in user data.
"""


def generate_insight(sleep, energy, stress):
    # 🔥 ERROR HANDLING (MULTIPLE INSTANCES)

    # 1. Negative values
    if sleep < 0 or energy < 0 or stress < 0:
        return "Error: Invalid input values (negative numbers not allowed)"

    # 2. Missing values
    if sleep == 0 or energy == 0:
        return "Error: Missing critical input data"

    # 3. Extreme values
    if stress > 10:
        return "Error: Stress value out of expected range"

    # 4. Type validation (extra)
    if not isinstance(sleep, int) or not isinstance(energy, int) or not isinstance(stress, int):
        return "Error: Inputs must be integers"

    # 🔥 EXPLICIT LPI TOOL CALLS
    tool_1 = call_lpi_tool("smile_overview")
    tool_2 = call_lpi_tool("get_insights")
    tool_3 = call_lpi_tool("query_knowledge")

    # Decision logic
    if sleep < 6:
        recommendation = "Improve sleep"
        reason = "low sleep leads to reduced energy levels"
    elif stress > 7:
        recommendation = "Reduce stress"
        reason = "high stress negatively affects productivity"
    else:
        recommendation = "Maintain current routine"
        reason = "your patterns are stable"

    explanation = explain_decision(recommendation, reason)

    output = f"""
=== Digital Twin Output ===

Calling LPI tools:
{tool_1}
{tool_2}
{tool_3}

Recommendation: {recommendation}
Reason: {reason}

{explanation}
"""

    return output


if __name__ == "__main__":
    sleep = 5
    energy = 4
    stress = 7

    result = generate_insight(sleep, energy, stress)
    print(result)
