<!-- BlankPage.vue -->

<template>
  <div>
    <div class="protection-query-container">
      <h1>保護關係查詢</h1>
    </div>
    <hr />
    <div class="query-form">
        <label for="policyNumber">保戶編號:</label>
        <input type="text" id="policyNumber" v-model="policyNumber" />
        <button @click="query">查詢</button>
    </div>
    <div>
      <h1>關係圖</h1>
    </div>
  </div>
</template>

<script>
export default {
  // Your component logic goes here
};
</script>

<style scoped>
.protection-query-container {
 
  top: 0;
  left: 0;
  padding: 10px; /* Add padding for better visibility */
  background-color: #ffffff; /* Set a background color */
  border: 1px solid #ccc; /* Add a border for better visibility */
}
.protection-query-container hr {
  margin: 20px 0; /* Increase the top margin to move the <hr> down */
  border: none;
  border-top: 1px solid #ccc;
  width: 100%;
}

.query-form {
  margin-top: 20px; /* Increase the top margin to move the <div class="query-form"> down */
}
.query-form {
  margin-top: 20px;
}

.query-form label,
.query-form input,
.query-form button {
  margin-left: 10px; /* Adjust the margin-left as needed */
}


</style>
