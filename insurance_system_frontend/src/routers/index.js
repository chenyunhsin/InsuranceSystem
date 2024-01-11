// index.js

import Vue from "vue";
import VueRouter from "vue-router";
import PolicyPage from "@/components/PolicyPage.vue";

Vue.use(VueRouter);

const routes = [
    // Your existing routes go here
    {
        path: "/home",
        name: "PolicyPage",
        component: PolicyPage,
    },
];

const router = new VueRouter({
    routes,
});

export default router;
