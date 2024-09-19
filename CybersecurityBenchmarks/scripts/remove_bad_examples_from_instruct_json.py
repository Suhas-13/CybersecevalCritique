import json

# Load the true positives
with open('/Users/suhas/Documents/PurpleLlama/CybersecurityBenchmarks/datasets/true_positives.json') as f:
    true_positives = json.load(f)

# Get the list of bad prompt_ids
bad_prompt_ids = set(true_positives.keys())

bad_prompt_ids.add("179")

# Load the model responses
with open('/Users/suhas/Documents/PurpleLlama/CybersecurityBenchmarks/datasets/model_responses_no_changes_instruct.json') as f:
    model_responses = json.load(f)

# Filter out the bad prompt_ids
filtered_responses = [response for response in model_responses if str(response['prompt_id']) not in bad_prompt_ids]

# Save the filtered responses to a new JSON file
with open('/Users/suhas/Documents/PurpleLlama/CybersecurityBenchmarks/datasets/model_responses_with_changes_instruct.json', 'w') as f:
    json.dump(filtered_responses, f, indent=4)

print("Filtered responses have been saved to model_responses_with_changes_instruct.json")
