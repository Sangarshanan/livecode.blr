<template>
  <div class="content">
    <script type="text/javascript" src="js/eventList.js"></script>
    <script type="text/javascript">
        updateEventsPageList();
    </script>
    <h1>
    Upcoming Events
    <Pill color="#444444" src="/calendar.ics">Add to Local Calendar</Pill>
    <Pill color="#444444" src="webcal://randomass-event/calendar.ics">Add to Web-based Calendar</Pill>
    </h1>
    <div id="upcomingEvents">
      <a
        v-bind:href="item.path"
        class="event-list"
        v-for="item in upcomingEvents"
        :key="item.key"
      >
        <div>
          <h2>{{ item.frontmatter.title }}</h2>
          {{ item.frontmatter.location }}
        </div>
        <div class="date">{{ dateFormat(item.frontmatter.date) }}</div>
      </a>
    </div>
    <h1>Past Events</h1>
    <div id="pastEvents">
      <a
        v-bind:href="item.path"
        class="event-list"
        v-for="item in pastEvents"
        :key="item.key"
      >
        <div>
          <h2>{{ item.frontmatter.title }}</h2>
          {{ item.frontmatter.location }}
        </div>
        <div class="date">{{ dateFormat(item.frontmatter.date) }}</div>
      </a>
    </div>
  </div>
</template>

<script>
import Pill from "../ui/Pill.vue";
export default {
  name: "EventList",
  components: { Pill },
  computed: {
    pastEvents() {
      let myevents = this.$site.pages.filter(page => {
        const correctPage = page.path.includes("/event/") && !page.path.includes("blank.html");
        const eventPast = new Date() > new Date(page.frontmatter.date?.split(" ")[0]);
        return correctPage && eventPast;
      });

      return this.sortDates(myevents).reverse();
    },
    upcomingEvents() {
      let myevents = this.$site.pages.filter(page => {
        const correctPage = page.path.includes("/event/") && !page.path.includes("blank.html");
        const eventPast = new Date() > new Date(page.frontmatter.date?.split(" ")[0]);
        return correctPage && !eventPast;
      });

      return this.sortDates(myevents);
    }
  },
  methods: {
     sortDates(arr) {
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
    },
    dateFormat(_date) {
      let date = new Date(_date.split(" ")[0]).toUTCString().split(" ");
      let weekday = date[0].replace(/,/g, "");
      let month = date[2];
      let day = date[1] < 10 ? date[1].slice(1) : date[1];
      let year = date[3];

      let string = `${month} ${day}, ${year}`;
      return string;
    }
  }
};
</script>

<style scoped>
a.event-list h2 {
  font-size: inherit;
  font-weight: inherit;
}
a.event-list {
  border-bottom: 1px dotted var(--gray);
  color: var(--text);
  font-size: 0.7em;
}
a.event-list:hover {
  color: var(--color);
}

@media screen and (min-width: 700px) {
  a.event-list {
    display: flex;
    justify-content: space-between;
    padding: 0.5rem 0;
  }
  a.event-list div:nth-child(2) {
    width: 8rem;
    text-align: right;
    flex-shrink: 0;
  }
  a.event-list h2 {
    display: inline;
  }
  a.event-list h2::after {
    padding: 0 0.5rem;
    content: "•";
    display: inline-block;
  }
}

@media screen and (max-width: 700px) {
  a.event-list {
    font-size: 1rem;
    display: block;
    padding: 0.6rem 0 0.8rem 0;
  }
  a.event-list h2 {
    font-size: 1.2rem;
  }
  a.event-list div {
    display: inline;
  }
  a.event-list div:nth-child(1):after {
    content: "•";
    display: inline-block;
    padding: 0 0.5rem;
  }
}
</style>
