<template>
    <el-dropdown>
        <span class="el-dropdown-link">
            <el-avatar :size="44" :src="circleUrl"></el-avatar>
            &nbsp;&nbsp;{{ currentUser.username }}
            <el-icon class="el-icon--right">
                <arrow-down />
            </el-icon>
        </span>
        <template #dropdown>
            <el-dropdown-menu>
                <el-dropdown-item>个人中心</el-dropdown-item>
                <el-dropdown-item @click="logout">安全退出</el-dropdown-item>
            </el-dropdown-menu>
        </template>

    </el-dropdown>
</template>

<script setup>
    import { ArrowDown } from '@element-plus/icons-vue'
    import { ref } from 'vue'
    import router from '@/router'
    import requestUtil, { getServerUrl } from '@/utils/request'

    const currentUser = JSON.parse(sessionStorage.getItem('currentUser')) || { username: '用户', avatar: '' }
    const defaultAvatar = '@/assets/images/default_avatar.png' // 设置默认头像 URL
    const circleUrl = currentUser.avatar ? getServerUrl() + 'media/userAvatar/' + currentUser.avatar : defaultAvatar;

    const logout = () => {
        window.sessionStorage.clear()
        router.push({ name: 'user_login' })
    }
</script>

<style lang="scss" scoped>
    .el-dropdown-link {
        cursor: pointer;
        color: var(--el-color-primary);
        display: flex;
        align-items: center;
    }
</style>