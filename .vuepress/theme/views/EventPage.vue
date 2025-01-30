<template>
  <div class="content event-page">
    <h1>{{data.title}} • {{ data.location }}</h1>
    <h2>{{ dateFormat(data.date) }}</h2>

    <div class="meta">
      <div v-if="data.link">
        Event Info: <a v-bind:href="data.link">{{data.link}}</a>
      </div>
    </div>

    <img v-if="data.image" v-bind:src="data.image"/>

    <Content />

  </div>
</template>

<script>
export default {
  name: 'EventPage',
  computed: {
      data () {
          let page = this.$page.frontmatter;
          return {
              title: page.title,
              location: page.location,
              date: page.date,
              image: page.image,
              link: page.link
          };
      }
  },
  methods: {
    dateFormat(_date){
      let datetime = new Date(_date);
      let dateString = datetime.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric'});
      let timeString = datetime.toLocaleTimeString('en-US', { timeStyle: 'short' });
      return `${dateString} @ ${timeString}`;
    }
  }
}
</script>

<style scoped>
.event-page img{
    max-width:80%;
    max-height: 60vh;
    margin: 2rem 0;
}
.event-page h2{
  margin-bottom: 1rem;
}
</style>
