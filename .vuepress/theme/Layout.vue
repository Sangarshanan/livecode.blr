<template>
  <div class="theme-container">
    <Nav />
    <div class="container">
      <!-- If Index Page, show Index page Component -->
      <div v-if="this.$page.path == '/'">
        <Index />
      </div>
      <!-- Otherwise -->
      <div v-else>
        <component :is="layout" />
      </div>
      <Footer />
    </div>
  </div>
</template>

<script>
import Nav from "./components/Nav.vue";
import Footer from "./components/Footer.vue";

import EventList from "./views/EventList.vue";
import EventPage from "./views/EventPage.vue";
import MemberList from "./views/MemberList.vue";
import ToolList from "./views/ToolList.vue";

import Page from "./views/Page.vue";

import Index from "./views/Index.vue";

export default {
  name: "layout",
  components: {
    Index,
    Nav,
    Footer,
    Page,
    MemberList,
    EventList,
    EventPage,
    ToolList
  },
  computed: {
    layout() {
      // This is where routing happens
      const path = this.$page.path;
      if (path.includes("/members")) {
        return "MemberList";
      } else if (path.includes("/events")) {
        return "EventList";
      } else if (path.includes("/event")) {
        return "EventPage";
      } else if (path.includes("/tools")) {
        return "ToolList";
      }
      return "Page";
    }
  }
};
</script>

<style>
@import "./style/main.css";

body {
  /*
    I know this looks bad but it apparently helps
    with an iOS view height resizing issue
  */
  overflow: none;
}

@media screen and (min-width: 700px) {
  body {
    padding-left: 20vw;
  }
}
@media screen and (max-width: 700px) {
  .container::before {
    content: " ";
    display: block;
    padding-top: calc(var(--padding) * 2);
    height: 2.6em;
  }
}
</style>
