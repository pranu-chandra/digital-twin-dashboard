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

        return stdout

    except Exception as e:
        return f"Error: {str(e)}"


def generate_insight(sleep, energy, stress):
    # LPI TOOL CALLS (IMPORTANT)
    smile_data = call_lpi_tool("smile_overview")
    insight_data = call_lpi_tool("get_insights")

    if sleep < 6:
        explanation = "Low sleep leads to reduced energy levels."
        return f"Recommendation: Improve sleep. Reason: {explanation}"
    elif stress > 7:
        explanation = "High stress impacts productivity."
        return f"Recommendation: Reduce stress. Reason: {explanation}"
    else:
        return "Your habits look stable."


if __name__ == "__main__":
    sleep = 5
    energy = 4
    stress = 7

    result = generate_insight(sleep, energy, stress)

    print("=== Digital Twin Output ===")
    print(result)
