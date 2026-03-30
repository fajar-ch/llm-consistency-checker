from multi_prompt import create_variations
from consistency import check_consistency
from report import generate_report

def fake_llm(prompt):
    if "sun rises" in prompt:
        return "The sun rises in the east."
    elif "sun direction" in prompt:
        return "The sun rises in the west."  # inconsistent
    return "No clear answer."

def run():
    query = "Where does the sun rise?"

    prompts = create_variations(query)
    responses = []

    for p in prompts:
        res = fake_llm(p)
        responses.append(res)

    consistency_result = check_consistency(responses)
    generate_report(query, responses, consistency_result)

if __name__ == "__main__":
    run()