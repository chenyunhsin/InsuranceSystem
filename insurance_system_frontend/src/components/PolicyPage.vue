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
     <div v-if="response.value && response.value.introducer_code !== null"><a class="custom-link" @click="query2(response.value.code)" style="color: blue; text-decoration: underline; cursor: pointer;">上一層</a></div>
      <!-- 第一層 -->
      <div class="level-1">
        <div v-if="response.value">
              <div class="node" style="background-color: #DAA520;">
                {{response.value.code}} <br/>{{response.value.name}} 
              </div>
             
        </div>
        <div v-else>
            請搜尋。
        </div>
      </div>

      <!-- 第二層 -->
      <div class="level-2">
          <div v-if="response.value">
                 <div class="node" v-if="response.value.l && response.value.l[0]">/</div>
                <div class="node" v-if="response.value.l && response.value.l[0]" :style="{ 'background-color': response.value.l[0].is_direct ? '#006400' : '#808080' }">
                 
                  <a class="custom-link" @click="query3(response.value.l[0].code)">{{response.value.l[0].code}}</a>  
                  <span >{{response.value.l[0].name}}</span>
                </div>
                <div v-else><div class="node"></div></div>
                
          </div>
          <div v-else><div class="node"></div></div>
          <div v-if="response.value">
           <div class="node" v-if="response.value.r && response.value.r[0]">\</div>
                <div class="node" v-if="response.value.r && response.value.r[0]" :style="{ 'background-color': response.value.r[0].is_direct ? '#006400' : '#808080' }">
                   <a class="custom-link" @click="query3(response.value.r[0].code)">{{response.value.r[0].code}}</a> 
                    <span >{{response.value.r[0].name}}</span>
                </div>
                <div v-else><div class="node"></div></div>
          </div>
          <div v-else> <div class="node"></div></div>
      </div>

      <!-- 第三層  -->
      <div class="level-3">
          <div v-if="response.value">
                 <div class="node" v-if="response.value.l && response.value.l[1]">/</div>
                <div class="node" v-if="response.value.l && response.value.l[1]" :style="{ 'background-color': response.value.l[1].is_direct ? '#006400' : '#808080' }">
                  <a class="custom-link" @click="query3(response.value.l[1].code)">{{response.value.l[1].code}}</a> 
                   <span >{{response.value.l[1].name}}</span>
                </div>
                <div v-else><div class="node"></div></div>
          </div>
          <div v-else><div class="node"></div></div>
          <div v-if="response.value">
                <div class="node" v-if="response.value.l && response.value.l[2]">\</div>
                <div class="node" v-if="response.value.l && response.value.l[2]" :style="{ 'background-color': response.value.l[2].is_direct ? '#006400' : '#808080' }">
                 <a class="custom-link" @click="query3(response.value.l[2].code)"> {{response.value.l[2].code}}</a> 
                  <span >{{response.value.l[2].name}}</span>
                </div>
                <div v-else><div class="node"></div></div>
          </div>
          <div v-else><div class="node"></div></div>
          <div v-if="response.value">
                <div class="node" v-if="response.value.r && response.value.r[1]">/</div>
                <div class="node" v-if="response.value.r && response.value.r[1]" :style="{ 'background-color': response.value.r[1].is_direct ? '#006400' : '#808080' }">
                  <a class="custom-link" @click="query3(response.value.r[1].code)">{{response.value.r[1].code}}</a> 
                  <span >{{response.value.r[1].name}}</span>
                </div>
                <div v-else><div class="node"></div></div>
          </div>
          <div v-else> <div class="node"></div></div>
          <div v-if="response.value">
                <div class="node" v-if="response.value.r && response.value.r[2]">/</div>
                <div class="node" v-if="response.value.r && response.value.r[2]" :style="{ 'background-color': response.value.r[2].is_direct ? '#006400' : '#808080' }">
                   <a class="custom-link" @click="query3(response.value.r[2].code)">{{response.value.r[2].code}}</a> 
                    <span>{{response.value.r[2].name}}</span>
                </div>
                <div v-else><div class="node"></div></div>
          </div>
          <div v-else> <div class="node"></div></div>
      </div>
    
      <!-- 第四層 -->
      <div class="level-4">
         <div v-if="response.value">
                <div class="node" v-if="response.value.l && response.value.l[3]">/</div>
                <div class="node" v-if="response.value.l  && response.value.l[3]" :style="{ 'background-color': response.value.l[3].is_direct ? '#006400' : '#808080' }">
                   <a class="custom-link" @click="query3(response.value.l[3].code)">{{response.value.l[3].code}}</a> 
                    <span>{{response.value.l[3].name}}</span>
                </div>
                <div v-else><div class="node"></div></div>
          </div>
          <div v-else> <div class="node"></div></div>
        <div v-if="response.value">
                <div class="node" v-if="response.value.l && response.value.l[4]">\</div>
                <div class="node" v-if="response.value.l && response.value.l[4]" :style="{ 'background-color': response.value.l[4].is_direct ? '#006400' : '#808080' }">
                  <a class="custom-link" @click="query3(response.value.l[4].code)">{{response.value.l[4].code}} </a> 
                  <span>{{response.value.l[4].name}}</span>
                </div>
                <div v-else><div class="node"></div></div>
          </div>
          <div v-else> <div class="node"></div></div>
         <div v-if="response.value">
                <div class="node" v-if="response.value.l && response.value.l[5]">/</div>
                <div class="node" v-if="response.value.l  && response.value.l[5]" :style="{ 'background-color': response.value.l[5].is_direct ? '#006400' : '#808080' }">
                  <a class="custom-link" @click="query3(response.value.l[5].code)">{{response.value.l[5].code}}</a> 
                   <span>{{response.value.l[5].name}}</span>
                </div>
                <div v-else><div class="node"></div></div>
          </div>
          <div v-else> <div class="node"></div></div>
         <div v-if="response.value">
                <div class="node" v-if="response.value.l && response.value.l[6]">\</div>
                <div class="node" v-if="response.value.l  && response.value.l[6]" :style="{ 'background-color': response.value.l[6].is_direct ? '#006400' : '#808080' }">
                   <a class="custom-link" @click="query3(response.value.l[6].code)">{{response.value.l[6].code}}</a> 
                  <span>{{response.value.l[6].name}}</span>
                </div>
                <div v-else><div class="node"></div></div>
          </div>
          <div v-else> <div class="node"></div></div>
        <div v-if="response.value">
                <div class="node" v-if="response.value.r && response.value.r[3]">/</div>
                <div class="node" v-if="response.value.r && response.value.r[3]" :style="{ 'background-color': response.value.r[3].is_direct ? '#006400' : '#808080' }">
                   <a class="custom-link" @click="query3(response.value.r[3].code)">{{response.value.r[3].code}} </a> 
                   <span>{{response.value.r[3].name}}</span>
                </div>
                <div v-else> <div class="node"></div></div>
          </div>
          <div v-else> <div class="node"></div></div>
        <div v-if="response.value">
                <div class="node" v-if="response.value.r && response.value.r[4]">\</div>
                <div class="node" v-if="response.value.r && response.value.r[4]" :style="{ 'background-color': response.value.r[4].is_direct ? '#006400' : '#808080' }">
                  <a class="custom-link" @click="query3(response.value.r[4].code)">{{response.value.r[4].code}} </a> 
                  <span>{{response.value.r[4].name}}</span>
                </div>
                 <div v-else> <div class="node"></div></div>
          </div>
         <div v-else> <div class="node"></div></div>
        <div v-if="response.value">
                <div class="node" v-if="response.value.r && response.value.r[5]">/</div>
                <div class="node" v-if="response.value.r && response.value.r[5]" :style="{ 'background-color': response.value.r[5].is_direct ? '#006400' : '#808080' }">
                  <a class="custom-link" @click="query3(response.value.r[5].code)">{{response.value.r[5].code}}</a>
                  <span>{{response.value.r[5].name}}</span>
                </div>
                <div v-else> <div class="node"></div></div>
          </div>
          <div v-else> <div class="node"></div></div>
        <div v-if="response.value ">
                <div class="node" v-if="response.value.r && response.value.r[6]">\</div>
                <div class="node" v-if="response.value.r && response.value.r[6]" :style="{ 'background-color': response.value.r[6].is_direct ? '#006400' : '#808080' }">
                  <a class="custom-link" @click="query3(response.value.r[6].code)">{{response.value.r[6].code}}</a>
                  <span>{{response.value.r[6].name}}</span>
                </div>
                <div v-else> <div class="node"></div></div>
          </div>
          <div v-else> <div class="node"></div></div>
          
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      policyNumber: '0000000001',
      response: {} // 初始化為空的響應對象
    };
  },
  methods: {
    query() {
      axios.get(`http://127.0.0.1:8000/api/policyholders/${this.policyNumber}/`, { withCredentials: true })
        .then(res => {
          this.response.value = res.data;
          console.log(this.response);
        })
        .catch(error => {
          const errorMessage = 'API 請求失敗: ' + error;
          alert(errorMessage);
          console.error('API 請求失敗:', error);
        });
    },
    query2(introducerCode){
       axios.get(`http://127.0.0.1:8000/api/policyholders/${introducerCode}/top/`, { withCredentials: true })
        .then(res => {
          this.response.value = res.data;
          console.log(this.response);
        })
        .catch(error => {
          const errorMessage = 'API 請求失敗: ' + error;
          alert(errorMessage);
          console.error('API 請求失敗:', error);
        });
    },query3(num) {
      axios.get(`http://127.0.0.1:8000/api/policyholders/${num}/`, { withCredentials: true })
        .then(res => {
          this.response.value = res.data;
          console.log(this.response);
        })
        .catch(error => {
          const errorMessage = 'API 請求失敗: ' + error;
          alert(errorMessage);
          console.error('API 請求失敗:', error);
        });
    },
  },
  
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
  width: 150px;
 
  height: auto;
  flex-direction: column;
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

.custom-link {
    color: blue;
    text-decoration: underline;
    cursor: pointer;
    display: flex 
  }

  .connected-node::before {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  border-left: 20px solid transparent;  /* 調整箭頭的寬度 */
  border-right: 20px solid transparent; /* 調整箭頭的寬度 */
  border-bottom: 20px solid #ccc;  /* 調整箭頭的顏色 */
  top: -20px;  /* 調整箭頭位置 */
  left: 50%;  /* 將箭頭置於節點的中央 */
  transform: translateX(-50%);  /* 將箭頭置於節點的中央 */
}
</style>
