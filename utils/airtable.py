from datetime import datetime
import requests
import os


def post_results(prompt: str, story: str, type_: str) -> None:
    """
    Write results to Airtable.

    Args:
        prompt: Plot / user inputted prompt
        story: Generated story
        type_: Prompted or Random
    """
    requests.post(
        url="https://api.airtable.com/v0/appZJEELvJrHMxCHq/Table%201",
        headers={
            "Authorization": f"Bearer {os.environ.get('AIRTABLE_API_KEY')}",
            "Content-Type": "application/json",
        },
        json={
            "records": [
                {
                    "fields": {
                        "Prompt": prompt,
                        "Story": story,
                        "Date": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                        "Type": type_,
                    }
                }
            ]
        }
    )
