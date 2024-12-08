<template>
    <div class="navbar">
        <div class="navbar-left">
            <HeaderLeft />
        </div>
        <div class="navbar-right">
            <Avatar />
        </div>

    </div>
</template>

<script setup>
    import Avatar from './components/Avatar.vue'
    import HeaderLeft from './components/HeaderLeft.vue'

</script>

<style lang="scss" scoped>
    .navbar {
        width: 100%;
        height: 60px;
        overflow: hidden;
        box-shadow: 0 1px 4px rgba(176, 195, 213, 0.08);
        padding: 0 16px;
        display: flex;
        align-items: center;
        box-sizing: border-box;
        position: relative;

        .navbar-left {
            color: aliceblue;
            font-size: 16px;
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: flex-start;
        }

        .navbar-right {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: flex-end;

            ::v-deep .navbar-item {
                display: inline-block;
                margin-left: 18px;
                font-size: 22px;
                color: #5a5e66;
                box-sizing: border-box;
                cursor: pointer;
            }
        }
    }
</style>