<!-- App.vue -->

<template>
  <div id="app">
    <router-view></router-view>
    <policy-page></policy-page> 
  </div>
</template>

<script>
import PolicyPage from "@/components/PolicyPage.vue";

export default {
  components: {
    PolicyPage,
  },
};
</script>

<style>
/* Your styles go here */
</style>
