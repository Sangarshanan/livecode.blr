import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')

def extract_base_id_and_table_name(url):
    match = re.search(r'app([a-zA-Z0-9]+).*tbl([a-zA-Z0-9]+)', url)
    if match:
        base_id = match.group(1)
        table_name = match.group(2)
        return base_id, table_name
    return None, None

BASE_ID = "app1ABXyx1mUnMWil"
TABLE_NAME = "shr6NXKESJBDd12w5"

def fetch_member_data(record_id):
    url = f'https://api.airtable.com/v0/app1ABXyx1mUnMWil/Directory/{record_id}'
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_KEY}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def fetch_all_records():
    url = 'https://api.airtable.com/v0/app1ABXyx1mUnMWil/Directory?view=Grid%20view'
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_KEY}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def populate_markdown_file(member_data):
    name = member_data['fields']['Name']
    location = member_data['fields']['Location']
    tools = ','.join(member_data['fields']['Tools'])
    image = member_data['fields']['Image']
    instagram = member_data['fields']['Instagram']
    soundcloud = member_data['fields']['Soundcloud']
    website = member_data['fields']['Website']
    bio = member_data['fields']['Bio']

    content = f"""---
name: {name}
tools: {tools}
location: {location}
image: {image}
links:
    instagram: {instagram}
    soundcloud: {soundcloud}
    website: {website}
---

{bio}
"""

    file_path = f'member/{name}.md'
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    records = fetch_all_records().get('records', [])
    print(records)
    for record in records:
        member_data = fetch_member_data(record['id'])
        if 'fields' in member_data:
            populate_markdown_file(member_data)

if __name__ == "__main__":
    main()
