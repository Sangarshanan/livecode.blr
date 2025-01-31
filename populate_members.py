import os
import requests
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")

BASE_ID = "app1ABXyx1mUnMWil"


def fetch_member_data(record_id):
    url = f"https://api.airtable.com/v0/app1ABXyx1mUnMWil/Directory/{record_id}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()


def fetch_all_records():
    url = "https://api.airtable.com/v0/app1ABXyx1mUnMWil/Directory?view=Grid%20view"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()


def populate_markdown_file(member_data):
    name = member_data["fields"]["Name"]
    location = member_data["fields"]["Location"]
    tools = ",".join(member_data["fields"]["Tools"])
    image = member_data["fields"].get("Image")
    instagram = member_data["fields"].get("Instagram")
    soundcloud = member_data["fields"].get("Soundcloud")
    website = member_data["fields"].get("Website")
    bio = member_data["fields"]["Bio"]

    links = []
    if instagram:
        links.append(f"instagram: {instagram}")
    if soundcloud:
        links.append(f"soundcloud: {soundcloud}")
    if website:
        links.append(f"website: {website}")
    links_content = "\n    ".join(links)

    content = f"""---
name: {name}
tools: {tools}
location: {location}
image: {image}
links:
    {links_content}
---

{bio}
"""

    file_path = f"member/{name}.md"
    with open(file_path, "w") as file:
        file.write(content)


def main():
    records = fetch_all_records().get("records", [])
    print(records)
    for record in records:
        member_data = fetch_member_data(record["id"])
        if "fields" in member_data:
            populate_markdown_file(member_data)


if __name__ == "__main__":
    main()
