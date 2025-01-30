const Settings = require("../global_settings.js");

const feedOptions = {
  canonical_base: "https://creative-coding-india.vercel.app/",
}

module.exports = {
  base: '/',
  title: Settings.title,
  description: Settings.description,

  dest: "./public",

  themeConfig: {
    repo: Settings.repository,
    mailingList: Settings.mailingList,
    discord: Settings.discord,
    social: Settings.social,
    navLinks: Settings.navLinks,
    footerLinks: Settings.footerLinks
  },

  markdown: {
    anchor: {
      permalink: true,
      permalinkBefore: false,
      permalinkSymbol: ""
    }
  },

  plugins: [
    [ "feed", feedOptions ],
  ],

};
