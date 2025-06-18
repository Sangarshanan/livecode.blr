<template>
  <div class="content">
    <h1>Live Coding Tools</h1>
    <Content />
  </div>
</template>

<script>
export default {
  name: "ToolList",
  computed: {
    allTools() {
      return this.$site.pages.filter(page => page.path.includes("/tool/"));
    }
  }
};
</script>

<style>
.tool-card {
  display: flex;
  margin-bottom: 2rem;
}
.tool-card h3 {
  display: inline;
}
.tool-card .image {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background-size: cover;
  background-position: center;
  margin-bottom: 1rem;


  flex-shrink: 0;
  transform: translate(0px, -0.2rem);
}
@media screen and (max-width: 900px) {
  .tool-card .image {
    width: 100px;
    height: 100px;
  }
}
.tool-card > div:nth-child(2) {
  padding-left: 2rem;
}

.pad-top {
  padding-top: 2rem;
}
.tool-card .content__default {
  color: var(--gray);
  padding: 1rem 0;
}

h2 a,
h3 a {
  display: inline-block;
  font-size: 1rem;
  font-weight: normal;
  border: 1px solid var(--color);
  margin-top: -0.25em;
  border-radius: 20px;
  padding: 0.2rem 0.7rem;
  margin-left: 0.25rem;
  margin-bottom: 0;
  vertical-align: middle;
  color: var(--color);
}
h2 a.header-anchor,
h3 a.header-anchor {
  display: none;
}

.content__default {
  color: var(--gray);
}
.content__default p {
  padding-top: 0.5rem;
  padding-bottom: 1.5rem;
  color: var(--text);
}
.content__default p a {
  color: var(--text);
}
.content__default p a:hover {
  color: var(--color);
}
.content__default h1,
.content__default h2,
.content__default h3 {
  color: var(--text);
}
</style>
