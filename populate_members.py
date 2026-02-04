import os

def readme():
    msg = f"""
---- - - - - - - - - - ----
    initialize thyself!
---- - - - - - - - - - ----

* fork livecode.blr repo:https://github.com/Sangarshanan/livecode.blr
* git clone to your system
* git checkout -b <thy_branch_name>
* python populate_members.py (<- you are here)
* enter details prompted by the script
* edit generated markdown file till satisfaction ensues
* git add thy files
* git commit -m "thy commit msg"
* git push -u origin <thy_branch_name>
* raise pull request
* pester admin to merge PR
* post merge, gawk at https://livecode-blr.vercel.app/members.html

"""
    print(msg)

def populate_markdown_file():
    name = input('Name / alias: ')
    location = input('Location (press enter to leave blank): ')
    tools = input('Tools (comma separated): ')
    image = input('Image link (press enter to leave blank): ')
    instagram = input('Instagram (press enter to leave blank): ')
    soundcloud = input('Soundcloud (press enter to leave blank): ')
    website = input('Website (press enter to leave blank): ')
    bio = input('Bio: ')

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
        
    return file_path


def main():
    readme()
    fp=populate_markdown_file()
    
    print(f"\nGreetings user, your markdown file is: {fp}")
    print("Thank you!")


if __name__ == "__main__":
    main()
