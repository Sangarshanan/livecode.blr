<template>
  <footer>
    <div>
      <h3>Social</h3>
      <ul>
        <a href="https://instagram.com/livecode.blr">Instagram</a>
      </ul>
    </div>
    <div>
      <h3>Site</h3>
      <ul>
        <li><a href="https://github.com/Sangarshanan/livecode.blr/issues/new?template=Blank+issue">Report Issue with Site</a></li>
        <li><a href="https://vuepress.vuejs.org">Built with VuePress</a></li>
        <li><a href="https://zachkrall.com">Theme by Zach Krall</a></li>
      </ul>
    </div>
  </footer>
</template>
<script>
export default {
  name: "Footer",
  computed: {
    data() {
      let theme = this.$site.themeConfig;

      return {
        year: new Date().getFullYear(),
        repo: theme.repo,
        social: theme.social,
        mailingList: theme.mailingList,
        footerLinks: theme.footerLinks
      };
    }
  }
};
</script>

<style scoped>
footer {
  margin-top: 1.5rem;
  padding-bottom: 2rem;
}
footer > div {
  padding: var(--padding);
  display: inline-block;
  vertical-align: top;
}
footer > div.full {
  display: block;
  max-width: 100%;
}
footer h3 {
  font-size: inherit;
  opacity: 0.4;
  font-weight: normal;
}
footer ul {
  list-style: none;
  margin: 0;
}
footer ul li a {
  color: var(--text);
}
footer ul li a:hover {
  color: var(--color);
}
</style>
