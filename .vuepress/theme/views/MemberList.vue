<template>
  <div class="content grid">
    <h1>
      <input type="text" v-model="searchQuery" class="search-bar" placeholder="Search by name, tools & location ..." />
      <button @click="clearFilters" class="refresh-button">Refresh</button>
    </h1>
      <div class="card" v-for="person in filteredMembers" :key="person.key">
        <div
          class="profile-image"
          v-bind:style="{
            backgroundImage: 'url(' + person.frontmatter.image + ')',
            backgroundColor: 'var(--color)'
          }"
        ></div>
        <div>
          {{ person.frontmatter.name }}

          <div style="font-size:0.6em">
            📍 <a href="#" @click.prevent="filterByLocation(person.frontmatter.location)" class="location-link">{{ person.frontmatter.location }}</a>
          </div>
          <div v-if="person.frontmatter.tools">
            <span v-for="tool in person.frontmatter.tools.split(',')" :key="tool" class="tool-pill">
              <a href="#" @click.prevent="filterByTool(tool.trim())">{{ tool.trim() }}</a>
            </span>
          </div>
          <div style="font-size:0.8em"><Content :page-key="person.key" /></div>
          <ul class="profile-links">
            <li v-for="(url, key) in person.frontmatter.links">
              <a v-bind:href="url">{{ key[0].toUpperCase() + key.slice(1) }}</a>
            </li>
          </ul>
        </div>
      </div>
  </div>
</template>

<script>
function shuffle(array) {
  let result = [];
  while (result.length < array.length) {
    let int = parseInt(array.length * Math.random());
    let random = array[int];
    if (!result.includes(array[int])) {
      result.push(array[int]);
    }
  }
  return result;
}

export default {
  name: "MemberList",
  data() {
    return {
      searchQuery: "",
      locationFilter: "",
      toolFilter: ""
    };
  },
  computed: {
    allMembers() {
      let array = this.$site.pages.filter(page =>
        page.path.includes("/member/")
      );
      return shuffle(array);
    },
    filteredMembers() {
      return this.allMembers.filter(person => {
        const nameMatch = person.frontmatter.name.toLowerCase().includes(this.searchQuery.toLowerCase());
        const toolsMatch = person.frontmatter.tools && person.frontmatter.tools.toLowerCase().includes(this.searchQuery.toLowerCase());
        const locationMatch = person.frontmatter.location && person.frontmatter.location.toLowerCase().includes(this.searchQuery.toLowerCase());
        const locationFilterMatch = this.locationFilter ? person.frontmatter.location === this.locationFilter : true;
        const toolFilterMatch = this.toolFilter ? person.frontmatter.tools && person.frontmatter.tools.split(',').map(tool => tool.trim()).includes(this.toolFilter) : true;
        return (nameMatch || toolsMatch || locationMatch) && locationFilterMatch && toolFilterMatch;
      });
    }
  },
  methods: {
    filterByLocation(location) {
      this.locationFilter = location;
    },
    filterByTool(tool) {
      this.toolFilter = tool;
    },
    clearFilters() {
      this.searchQuery = "";
      this.locationFilter = "";
      this.toolFilter = "";
    }
  }
};
</script>

<style scoped>
ul.profile-links {
  list-style: none;
  padding: 0.6rem 0;
  margin: 0;
}
ul.profile-links li {
  display: inline-block;
  margin-right: 0.2em;
  margin-bottom: 0.1em;
}
ul.profile-links li a {
  font-size: 0.7em;
  border: 1px solid var(--gray);
  border-radius: 20px;
  color: var(--color);
  padding: 0.2em 0.7em;
}

.profile-image {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background-size: cover;
  background-position: center;
  margin-bottom: 1rem;

  /* Back up image for broken links */
  background-image: url("/media/algorave_in.png");
}

@media screen and (min-width: 820px) {
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }
}
.grid h1 {
  grid-column: span 3;
}
.grid p {
  grid-column: span 3;
}
.grid h1:nth-child(2n + 0) {
  margin-top: 4rem;
}
.card {
  padding: var(--padding);
}
.card div .content__default {
  color: var(--gray);
}
@media screen and (max-width: 820px) {
  .card {
    display: flex;
    padding-left: 0;
  }
  .profile-image {
    width: 100px;
    height: 100px;
    flex-shrink: 0;
  }
  .card > div:last-child {
    padding-left: calc(var(--padding) * 2);
  }
}

.tool-pill {
  display: inline-block;
  background-color: var(--color);
  color: white;
  padding: 0.2em 0.5em;
  border-radius: 10px;
  margin-right: 0.3em;
  font-size: 0.7em;
}

.search-bar {
  width: 80%;
  padding: 0.3em;
  margin-bottom: 1em;
  border: 1px solid var(--color);
  border-radius: 5px;
  font-size: 0.9em;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.search-bar:focus {
  outline: none;
  border-color: var(--color);
  box-shadow: 0 0 5px var(--color);
}

.refresh-button {
  margin-left: 1em;
  padding: 0.3em 0.6em;
  border: 1px solid var(--color);
  border-radius: 5px;
  background-color: var(--color);
  color: white;
  font-size: 0.9em;
  cursor: pointer;
}

.refresh-button:hover {
  background-color: darken(var(--color), 10%);
}

.location-link {
  color: var(--white);
  text-decoration: underline;
  cursor: pointer;
}

.location-link:hover {
  text-decoration: none;
  font-weight: bold;
}
</style>
