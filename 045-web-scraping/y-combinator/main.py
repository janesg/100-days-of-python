from bs4 import BeautifulSoup
import requests

WEBSITE_URL = "https://news.ycombinator.com"

response = requests.get(WEBSITE_URL)

soup = BeautifulSoup(response.text, "html.parser")

title_anchor = None
title_anchors = []
score_spans = []
high_score = 0
highest_scorers = []

# Get all <tr> table row elements
all_trs = soup.select("tr")

# Iterate through rows looking for titles or scores
for tr in all_trs:
    score_span = tr.select_one("span.subline > span.score")

    # First look for a score
    if score_span is not None and title_anchor is not None:
        score_spans.append(score_span)
        title_anchors.append(title_anchor)
        title_anchor = None
    else:
        # Look for a title
        title_anchor = tr.select_one("span.titleline > a")

# Check for consistency
if len(title_anchors) != len(score_spans):
    raise Exception("Number of titles and scores should match")

for idx in range(0, len(title_anchors)):
    title = title_anchors[idx].get_text()
    link = title_anchors[idx].get('href')
    score = int(score_spans[idx].get_text().split(" ")[0])
    entry = f"{title} : {link}"
    print(f"{idx + 1}\t{entry} : {score}")
    # Handle possibility of 2 or more items having highest score
    if score == high_score:
        highest_scorers.append(entry)
    elif score > high_score:
        high_score = score
        highest_scorers.clear()
        highest_scorers.append(entry)

print(f"\nWith {high_score} points, the highest scoring news item(s) are :")
for item in highest_scorers:
    print(f"\t{item}")