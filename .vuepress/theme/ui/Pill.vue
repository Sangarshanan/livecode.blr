<template>
  <a
    :style="style"
    :href="$props.src"
    rel="noopener"
    v-on:mouseover="hover"
    v-on:mouseout="unhover"
  >
    <slot></slot>
  </a>
</template>

<script>
export default {
  name: "Pill",
  props: ["color", "src"],
  data() {
    return {
      style: {
        backgroundColor: "#c6c6c6",
        color: "#ffffff"
      }
    };
  },
  mounted() {
    this.style.backgroundColor = this.$props.color;
    this.style.color = "var(--white)";
  },
  methods: {
    hover() {
      this.style.backgroundColor = "var(--white)";
      this.style.color = "var(--black)";
    },
    unhover() {
      this.style.backgroundColor = this.$props.color;
      this.style.color = "var(--white)";
    }
  }
};
</script>

<style scoped>
a {
  padding: 0.2em 0.6em;
  border-radius: 1em;
  font-size: 0.7em;
}
</style>
