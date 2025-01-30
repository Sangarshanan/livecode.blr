<template>
  <div style="padding:var(--padding)" class="basic-page">
    <script type="text/javascript" src="js/eventList.js"></script>
    <script type="text/javascript">
        document.addEventListener('DOMContentLoaded', function(event){
            updateIndexEventsList();
        });
    </script>

    <div
      style="display:inline-block;margin-bottom:var(--padding);border:2px solid var(--color);border-radius:calc(var(--padding)*0.25);padding:var(--padding);"
    >
      <b style="color:var(--color);">Are you a creative coder from India?</b>
      Add yourself to the registry!!
      <a :href="this.$themeConfig.discord" class="underline">Click here</a>
      &hearts;
    </div>

    <div class="pb .content__default">
      <Content :page-key="about.key" />
    </div>

  </div>
</template>

<script>
export default {
  name: "Index",
  computed: {
    about() {
      return this.$site.pages.filter(page => page.path == "/");
    },
    events() {
      const sort = arr => {
        arr.sort(function(a, b) {
          var dateA = new Date(a.frontmatter.date.split(" ")[0]),
            dateB = new Date(b.frontmatter.date.split(" ")[0]);
          if (dateA < dateB)
            //sort string ascending
            return -1;
          if (dateA > dateB) return 1;
          return 0; //default return value (no sorting)
        });
        return arr;
      };

      let myevents = this.$site.pages.filter(page => {
        const correctPage = page.path.includes("/event/") && !page.path.includes("blank.html");
        const eventNotPast = new Date() < new Date(page.frontmatter.date?.split(" ")[0]);
        return correctPage && eventNotPast;
      });

      let sorted = sort(myevents);
      sorted.forEach(i => (i.nice_date = this.date(i.frontmatter.date)));
      return sorted;
    }
  },
  methods: {
    genStyle(url) {
      if (url) {
        return { backgroundImage: "url('" + url + "')" };
      } else {
        return { backgroundColor: "var(--color)" };
      }
    },
    date(_date) {
      let date = new Date(_date.split(" ")[0]);
      let month = date.getMonth() + 1;
      date = date.toUTCString().split(" ");
      let day = date[1] < 10 ? date[1].slice(1) : date[1];
      let year = date[3];

      let string = `${month}/${day}/${year}`;
      return string;
    }
  }
};
</script>

<style scoped>
.right {
  text-align: right;
}
.pb {
  padding-bottom: var(--padding);
}
.space-between {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
h1.space-between a {
  color: var(--gray);
}
h1.space-between a:hover {
  color: var(--white);
}

ul#events {
  padding: 0;
  margin: 0;
}
@media screen and (min-width: 800px) {
  ul#events {
    display: flex;
    justify-content: space-between;
  }
}
ul#events li {
  list-style: none;
  margin: 0;
  padding: 0;
  width: 22%;
  /* font-size: 0.7em; */
  /* border: 1px solid red; */
}
ul#events li a div.image {
  position: relative;
  width: 100%;
  height: 0px;
  padding-bottom: 100%;
  background-position: center;
  /* border: 1px solid var(--white); */
  background-size: cover;
  background-repeat: no-repeat;
  margin-bottom: 0.4em;
}
ul#events li a div.image div.fixed {
  position: absolute;
  top: 0px;
  left: 0px;
  width: 90%;
  line-height: 1;
}
ul#events li a:hover {
  color: var(--color);
}
@media screen and (max-width: 800px) {
  ul#events li {
    width: 100%;
  }
  ul#events li a {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  ul#events li a div.image {
    flex-shrink: 0;
    display: inline-block;
    width: 150px !important;
    height: 150px;
    padding-bottom: 0;
  }
  ul#events li a div.grow {
    display: inline-block;
    flex-grow: auto;
    padding-left: 1rem;
    width: 100%;
  }
}
</style>
