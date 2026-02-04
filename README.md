# Livecode BLR

We are a collective that practices and promotes live coding as a sound and visual creation technique, generating a technological appropriation through the use and development of free and open software focused on generating its own relationships and discourses.

## Add yourself/ A Member

* fork livecode.blr repo: https://github.com/Sangarshanan/livecode.blr
* git clone to your system
* git checkout -b `<thy_branch_name>`
* python populate_members.py
* enter details prompted by the script
* edit generated markdown file till satisfaction ensues
* git add thy files
* git commit -m "thy commit msg"
* git push -u origin `<thy_branch_name>`
* raise pull request
* pester admin to merge PR
* post merge, gawk at https://livecode-blr.vercel.app/members.html

## Setup locally

Prerequisites
* nodejs
* npm

NOTE: install nvm first and use it to setup node/npm to save lifespan and prevent hair tearing troubleshooting sessions.

after git cloning as usual...

```sh
npm i -g vuepress
yarn docs:start
```

## Troubleshooting

Some setup issues you might encounter

> Cannot find module 'vue-template-compiler'
```sh
npm i vue-template-compiler
```

NOTE: add your resolved setup issues to make future troubleshooting easier for everyone :)
