<template>
    <div class="header">
        <img src="@/assets/images/logo.png" alt="Logo" class="logo" />
        SDUST 大数据交通流量预测平台
    </div>
</template>

<script setup>
</script>

<style lang="scss" scoped>
    .header {
        display: flex;
        align-items: center;
        /* 使图片和文本垂直居中对齐 */
    }

    .logo {
        width: 52px;
        /* 设置logo的宽度，可以根据需要调整 */
        height: auto;
        /* 避免变形 */
        margin-right: 10px;
        /* 图片与文本之间的间距 */
        margin-left: 10px;
    }
</style>