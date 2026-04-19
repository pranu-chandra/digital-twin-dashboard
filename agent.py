import subprocess
import json

def call_tool(tool_name, query=""):
    try:
        request = {
            "tool": tool_name,
            "query": query
        }

        result = subprocess.run(
            ["node", "dist/src/index.js"],
            input=json.dumps(request),
            text=True,
            capture_output=True
        )

        return result.stdout

    except Exception as e:
        return f"Error: {str(e)}"


def generate_insight(sleep, energy, stress):
    # Simple logic + tool usage

    overview = call_tool("smile_overview")
    insights = call_tool("get_insights")

    if sleep < 6:
        return "Low sleep detected. This may reduce your energy levels."
    elif stress > 7:
        return "High stress detected. Consider relaxation."
    else:
        return "Your patterns look stable. Keep maintaining your habits."


if __name__ == "__main__":
    sleep = 6
    energy = 5
    stress = 7

    insight = generate_insight(sleep, energy, stress)

    print("=== Digital Twin Insight ===")
    print(insight)
