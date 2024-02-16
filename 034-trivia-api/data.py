import requests
import html

OTDB_BASE_URL = "https://opentdb.com/api.php"

# If category param not included, questions are across all subjects
response = requests.get(url=OTDB_BASE_URL,
                        params={
                            "amount": 10,
                            # "category": 18,     # 18 = Computer Science
                            "type": "boolean"
                        })
response.raise_for_status()

question_data = response.json()['results']

# For each dict in the list, unescape all HTML entities in the dict's 'question' field
for q in question_data:
    q.update(('question', html.unescape(v)) for (k, v) in q.items() if k == 'question')
