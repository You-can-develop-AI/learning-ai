import json
from pathlib import Path

# Read current topics.json
topics_file = Path("topics.json")
with open(topics_file, 'r') as f:
    data = json.load(f)

# Transform all subtopics to objects with resources and notes
for category in data['learning_path']:
    for topic in category['topics']:
        new_subtopics = []
        for subtopic in topic['subtopics']:
            if isinstance(subtopic, str):
                # Convert string to object
                new_subtopics.append({
                    "name": subtopic,
                    "resources": [],
                    "notes": ""
                })
            else:
                # Already an object, keep it
                new_subtopics.append(subtopic)
        topic['subtopics'] = new_subtopics

# Save back
with open(topics_file, 'w') as f:
    json.dump(data, f, indent=2)

print("Topics.json updated successfully!")
