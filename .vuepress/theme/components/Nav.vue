<template>
  <nav id="nav" class="closed" tabindex="1">
    <ul>
      <li id="logo" ref="logo">
        <a href="/" class="nostyle"
          ><img
            :src="$withBase('/media/algorave_in.png')"
            alt="Algorave.In Logo"
        /></a>
      </li>
      <li class="link" v-for="(link, key) in navLinks" :key="link + key">
        <a :href="link.path">{{ link.title }}</a>
      </li>
      <li class="link">
        <a :href="'//' + 'algorave.in'" target="_blank"> Algorave </a>
      </li>
    </ul>
    <!-- TODO: figure out vue onclick stuff doesn't work, maybe client hydration? https://vuejs.org/guide/scaling-up/ssr.html#client-hydration -->
    <button
      id="mobile-menu"
      ref="mobilemenu"
      onclick="document.querySelector('#nav').classList.toggle('open'); document.querySelector('#nav').classList.toggle('closed')"
      tabindex="2"
    >
      <div></div>
    </button>
  </nav>
</template>

<script>
export default {
  name: "Nav",
  data() {
    return {
      closed: true,
      open: false
    };
  },
  computed: {
    navLinks() {
      let links = this.$themeConfig.navLinks;
      return links;
    }
  },
  methods: {
    toggleNav() {
      this.closed = !this.closed;
      this.open = !this.open;

      if (this.open) {
        console.log(this.$refs.mobilemenu);
        this.$refs.mobilemenu.focus();
      }
    }
  }
};
</script>

<style scoped>
nav {
  padding: var(--padding);
  background: var(--background);

  position: fixed;
  top: 0;
  left: 0;

  width: 20vw;
  height: 100vh;

  overflow-y: auto;

  z-index: 999; /* always on top */

  /* transition: 0.2s ease all; */
}
ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
li {
  display: block;
  padding: 0;
  margin: 0 0 calc(var(--padding) * 0.25) 0;
}
li:focus {
  border: 1px solid red;
}
li a {
  color: #fff;
  /* margin-left: 1rem; */
}
li a:hover {
  color: var(--gray);
}
.margin-top {
  margin-top: calc(var(--padding) * 0.5);
}

li#logo img {
  height: 2.44em;
}

@media screen and (max-width: 600px) {
  nav {
    font-size: 0.8rem;
  }
}

#mobile-menu {
  display: none;
  position: absolute;
  top: var(--padding);
  right: var(--padding);
  width: 4em;
  height: 2.44em;
  /* border: 1px solid red; */
  border: 0;
  background: transparent;
  appearance: none;
  font-size: inherit;
  cursor: pointer;
  color: inherit;
}
#mobile-menu div {
  position: absolute;
  top: 50%;
  left: 50%;
  display: block;
  content: " ";
  width: 10px;
  height: 10px;
  border-radius: 10px;
  background: var(--white);
  transform: translate(-5px, -5px);
  transition: 0.3s ease all;
}
#mobile-menu div:before {
  position: absolute;
  top: 0;
  left: 16px;
  display: block;
  content: " ";
  width: 10px;
  height: 10px;
  border-radius: 10px;
  background: var(--white);
  transition: 0.3s ease all;
}
#mobile-menu div:after {
  position: absolute;
  top: 0;
  left: -16px;
  display: block;
  content: " ";
  width: 10px;
  height: 10px;
  border-radius: 10px;
  background: var(--white);
  transition: 0.3s ease all;
}

nav ul li:nth-child(0n + 2) {
  margin-top: calc(var(--padding) * 1.2);
}

@media screen and (max-width: 700px) {
  nav {
    width: 100%;
    height: auto;
  }
  nav.open {
    height: 100vh;
    overflow-y: auto;
    background: rgba(20, 20, 20, 0.9);
    transition: 0.3s ease all;
  }
  nav ul li#logo {
    margin-bottom: 0;
  }
  nav ul li.link {
    font-size: 1.8em;
  }
  nav.closed ul li.link {
    display: none;
    transition: 0.3s ease all;
  }
  #mobile-menu {
    display: block;
  }

  nav.open #mobile-menu div {
    position: absolute;
    top: 50%;
    left: 50%;
    display: block;
    content: " ";
    width: 30px;
    height: 2px;
    /* border-radius: 10px; */
    background: var(--white);
    transform: translate(-50%, -50%) rotate(-45deg);
  }
  nav.open #mobile-menu div:before {
    position: absolute;
    top: 50%;
    left: 50%;
    display: block;
    content: " ";
    width: 30px;
    height: 2px;
    background: var(--white);
    transform: translate(-50%, -50%) rotate(-90deg);
  }
  nav.open #mobile-menu div:after {
    display: none;
  }
}
</style>
