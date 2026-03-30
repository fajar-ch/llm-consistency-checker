def generate_report(query, responses, result):
    print("\n=== Analysis Report ===")
    print("Query:", query)

    print("\nResponses:")
    for r in responses:
        print("-", r)

    print("\nResult:", result)