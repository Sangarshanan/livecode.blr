const Settings = require("../global_settings.js");

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

};
