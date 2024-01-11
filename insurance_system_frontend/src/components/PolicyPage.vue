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
    <div class="binary-tree">
      <!-- 第一層 -->
      <div class="level-1">
        <div class="node">A</div>
      </div>

      <!-- 第二層 -->
      <div class="level-2">
        <div class="node">B1</div>
        <div class="node">B2</div>
      </div>

      <!-- 第三層 -->
      <div class="level-3">
        <div class="node">C1</div>
        <div class="node">C2</div>
        <div class="node">C3</div>
        <div class="node">C4</div>
      </div>

      <!-- 第四層 -->
      <div class="level-4">
        <div class="node">D1</div>
        <div class="node">D2</div>
        <div class="node">D3</div>
        <div class="node">D4</div>
        <div class="node">D5</div>
        <div class="node">D6</div>
        <div class="node">D7</div>
        <div class="node">D8</div>
      </div>
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
.binary-tree {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.node {
  width: 100px;
  height: 40px;
  border: 1px solid #ccc;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px;
}

/* 調整每一層的樣式 */
.level-1 {
  display: flex;
}

.level-2,
.level-3,
.level-4 {
  display: flex;
}

.level-2 .node {
  margin-right: 20px;
}

.level-3 .node {
  margin-right: 10px;
}

.level-4 .node {
  margin-right: 5px;
}

</style>
