<template>
    <el-menu active-text-color="#ffd04b" background-color="#2d3a4b" class="el-menu-vertical-demo" text-color="#fff"
        router:default-active="'/index'">
        <el-menu-item index="/index" @click="toIndex()">
            <el-icon>
                <home-filled />
            </el-icon>
            <span>首页</span>
        </el-menu-item>
        <el-sub-menu :index="menu.path" v-for="menu in menuList">
            <template #title>
                <el-icon>
                    <svg-icon :icon="menu.icon" />
                </el-icon>
                {{ menu.name }}
            </template>
            <el-menu-item :index="item.path" v-for="item in menu.children" :key="item.path"
                @click="navigateTo(item.path)">
                <el-icon>
                    <svg-icon :icon="item.icon" />
                </el-icon>
                {{ item.name }}
            </el-menu-item>

        </el-sub-menu>
    </el-menu>
</template>
<script setup>
    import { HomeFilled } from '@element-plus/icons-vue'
    import { useRouter } from 'vue-router'
    const router = useRouter()
    const menuList = JSON.parse(sessionStorage.getItem("menuList"))
    const navigateTo = (path) => {
        router.push(path)
    }
    const toIndex = () => {
        router.push({ name: 'index' })
    }
</script>

<style lang="scss" scoped>
</style>