<template>
    <div class="app-wrapper">
        <el-container>
            <el-header>
                <Header></Header>
            </el-header>
            <el-container>
                <el-aside width="200px" class="sidebar-container">
                    <SideBar></SideBar>
                </el-aside>
                <el-container>
                    <el-main>
                        <Main></Main>
                    </el-main>
                    <el-footer>
                        <Footer></Footer>
                    </el-footer>
                </el-container>
            </el-container>
        </el-container>
    </div>
</template>

<script setup>
    import SideBar from '@/layout/sidebar/SideBar'
    import Header from '@/layout/header/Header'
    import Footer from '@/layout/footer/Footer'
    import Main from '@/layout/main/MainTest'
</script>

<style scoped>
    .app-wrapper {
        position: relative;
        width: 100%;
        height: 100%;
    }

    .sidebar-container {
        background-color: #2d3a4b;
        height: 100%;
    }

    .el-container {
        height: 100%
    }

    .el-header {
        padding-left: 0px;
        padding-right: 0px;
        background-color: rgb(46, 46, 46)
    }

    :deep(ul.el-menu) {
        border-right-width: 0px
    }
</style>