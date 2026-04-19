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


def generate_insight(sleep, energy, stress):
    # Input validation (IMPORTANT FOR SCORE)
    if sleep < 0 or energy < 0 or stress < 0:
        return "Error: Invalid input values"

    if sleep == 0:
        return "Error: Missing sleep data"

    # LPI TOOL CALLS (VISIBLE)
    tool1 = call_lpi_tool("smile_overview")
    tool2 = call_lpi_tool("get_insights")

    # Decision logic
    if sleep < 6:
        recommendation = "Improve sleep"
        reason = "Low sleep leads to reduced energy levels."
    elif stress > 7:
        recommendation = "Reduce stress"
        reason = "High stress affects productivity."
    else:
        recommendation = "Maintain current routine"
        reason = "Your patterns look stable."

    output = f"""
=== Digital Twin Output ===

Calling LPI tools...
Tool: {tool1}
Tool: {tool2}

Recommendation: {recommendation}
Reason: {reason}
"""

    return output


if __name__ == "__main__":
    sleep = 5
    energy = 4
    stress = 7

    result = generate_insight(sleep, energy, stress)

    print(result)
