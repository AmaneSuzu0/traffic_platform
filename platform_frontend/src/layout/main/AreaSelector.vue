<template>
    <div>
        <label class="el-form-item__label">位置</label>
        <el-cascader :options="pcaTextArr" v-model="selectedAddresses" @change="handleChangeAddress" :props="{
        expandTrigger: 'hover',
        multiple: false,
        checkStrictly: true,
        emitPath: true,
      }">
        </el-cascader>
    </div>
</template>

<script setup>
    import { ref, watch } from 'vue';
    import { pcaTextArr } from "element-china-area-data"; //安装中国城市地区级联菜单数组 npm install element-china-area-data
    const props = defineProps(['modelValue']);

    // 使用 defineEmits 来定义 emit
    const emit = defineEmits(['update:modelValue']);
    const selectedAddresses = ref([props.modelValue || []]); // 当前选中的地址数组，例如：['广州市','成都市']

    // 监听 selectedAddresses 的变化并 emit
    watch(selectedAddresses, (newValue) => {
        emit('update:modelValue', newValue);
    });
    const handleChangeAddress = (d) => {
        // 处理地址变化逻辑
        selectedAddresses.value = d;
    };
</script>

<style scoped>
    .el-form-item__label {
        font-size: 18px;
    }
</style>