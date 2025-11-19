# SPDX-License-Identifier: CERN-OHL-P-2.0

import json
import os
import shutil
import webbrowser
import requests

STANDARDS_FILE = "knowledge/component_description_standards.md"
PREPROMPT_FILE = "knowledge/auto_description_prompt.txt"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

def generate_description(mpn: str) -> str:
    """Generate a component description from the MPN using OpenAI."""
    # If no API key, open the standards file and ask manual input
    if not OPENAI_API_KEY:
        print("No OpenAI API key found. Please fill manually.")
        if os.path.exists(STANDARDS_FILE):
            webbrowser.open(STANDARDS_FILE)
        return input("Enter the component description manually: ")

    if not os.path.exists(PREPROMPT_FILE):
        print(f"Missing {PREPROMPT_FILE}! Please create it with the pre-prompt instructions.")
        return input("Enter the component description manually: ")

    with open(PREPROMPT_FILE, "r", encoding="utf-8") as f:
        preprompt = f.read()

    messages = [
        {"role": "system", "content": preprompt},
        {"role": "user", "content": f"MPN: {mpn}"}
    ]

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
            json={
                "model": OPENAI_MODEL,
                "messages": messages,
                "temperature": 0.2,
            },
            timeout=30,
        )
        response.raise_for_status()
        description = response.json()["choices"][0]["message"]["content"].strip()
        return description
    except Exception as e:
        print(f"(Info) OpenAI generation failed: {e}")
        if os.path.exists(STANDARDS_FILE):
            webbrowser.open(STANDARDS_FILE)
        return input("Enter the component description manually: ")

def create_new_component():
    mpn = input("Enter the MPN (manufacturer part number): ").strip()
    filename = f"components/{mpn}.json"

    value_vary = input("Can the value for the component vary? (y/n): ").strip().lower()
    value = "?" if value_vary == "y" else mpn

    print("Generating description...")
    description = generate_description(mpn)
    print(f"\nFinal description:\n{description}\n")

    # Symbol handling
    symbol_name = input("Enter the symbol name: ").strip()
    symbol_path = f"symbols/{symbol_name}.SchLib"
    os.makedirs("symbols", exist_ok=True)
    if not os.path.exists(symbol_path):
        # Copy the symbol template and rename it to the new symbol name
        shutil.copy("symbols/AA_SymbolTemplate.SchLib", symbol_path)
        os.system(f"start {symbol_path}")

    # Footprint handling
    footprint_name = input("Enter the footprint name: ").strip()
    footprint_path = f"footprints/{footprint_name}.PcbLib"
    os.makedirs("footprints", exist_ok=True)
    if not os.path.exists(footprint_path):
        shutil.copy("footprints/AA_FootprintTemplate.PcbLib", footprint_path)
        os.system(f"start {footprint_path}")

    os.makedirs("components", exist_ok=True)
    component_data = {
        "Library Ref": symbol_name,
        "Library Path": f"{symbol_name}.SchLib",
        "Footprint Ref": footprint_name,
        "Footprint Path": f"{footprint_name}.PcbLib",
        "Name": mpn,
        "Value": value,
        "Description": description,
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(component_data, f, indent=4)

    print(f"Component {mpn} created successfully!")

if __name__ == "__main__":
    create_new_component()
