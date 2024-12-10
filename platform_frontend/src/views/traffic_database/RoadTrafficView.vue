<template>
    <div class="home">
        道路交通数据库
    </div>
    <div class="selector-container">
        <AreaSelector v-model="selectedAddresses"></AreaSelector>
        <el-button type="primary" plain class="query_button" @click="getTableData">查询</el-button>
    </div>
    <el-table :data="tableData" style="width: 100%" stripe="true" height="450">
        <el-table-column label="ID" prop="id"></el-table-column>
        <el-table-column label="省" prop="province"></el-table-column>
        <el-table-column label="市" prop="city"></el-table-column>
        <el-table-column label="区/县" prop="district"></el-table-column>
        <el-table-column label="交通节点" prop="node_name"></el-table-column>

        <el-table-column label="操作">
            <template #default="scope">
                <el-button type="primary" plain size="small" @click="viewDetails(scope.row)">查看</el-button>
                <el-button type="primary" plain size="small" @click="editItem(scope.row)">预测</el-button>
            </template>
        </el-table-column>
    </el-table>

    <el-dialog v-model="dialogVisible" title="详细信息" width="50%">
        <div class="detail-container">
            <div class="detail-item">
                <span class="detail-label">省：</span>
                <span class="detail-value">{{ selectedItem.province }}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">市：</span>
                <span class="detail-value">{{ selectedItem.city }}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">区/县：</span>
                <span class="detail-value">{{ selectedItem.district }}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">交通节点：</span>
                <span class="detail-value">{{ selectedItem.node_name }}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">交通类型：</span>
                <span class="detail-value">{{ selectedItem.node_type }}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">经度：</span>
                <span class="detail-value">{{ selectedItem.longitude }}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">纬度：</span>
                <span class="detail-value">{{ selectedItem.latitude }}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">详细描述：</span>
                <span class="detail-value">{{ selectedItem.description }}</span>
            </div>
        </div>
        <template #footer>
            <span class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
            </span>
        </template>
    </el-dialog>
</template>

<script setup>
    import { ref } from 'vue';
    import AreaSelector from '@/layout/main/AreaSelector.vue';
    import requestUtil from '@/utils/request'
    import { ElMessage } from 'element-plus';

    const selectedAddresses = ref(["山东省", "青岛市"]);
    const tableData = ref([]);
    const dialogVisible = ref(false);
    const selectedItem = ref({});

    const getTableData = async () => {
        try {
            let province = selectedAddresses.value[0] || '';
            let city = selectedAddresses.value[1] || '';
            let district = selectedAddresses.value[2] || '';
            let result = await requestUtil.get('/data_query/get_nodes', {
                province: province,
                city: city,
                district: district,
                node_type: '道路交通',
            });

            let data = result.data;
            if (data.code === 200) {
                tableData.value = data.nodes;
            } else {
                console.log(data.message);
                ElMessage.error(data.message);
            }
        } catch (error) {
            console.error("请求错误:", error);
            ElMessage.error('请求时发生错误，请稍后重试。');
        }
    };

    const viewDetails = (item) => {
        selectedItem.value = item;
        dialogVisible.value = true;
    };

    const editItem = (item) => {
        console.log("编辑:", item);
    };

    getTableData();
</script>

<style lang="scss">
    .operate-button {
        margin-right: 5px;
    }

    .dialog-footer {
        display: flex;
        justify-content: flex-end;
        gap: 12px;
        margin-top: 20px;
    }

    .detail-container {
        padding: 20px;
    }

    .detail-item {
        display: flex;
        margin-bottom: 16px;
        line-height: 24px;

        &:last-child {
            margin-bottom: 0;
        }
    }

    .detail-label {
        width: 100px;
        color: #606266;
        font-weight: 500;
    }

    .detail-value {
        flex: 1;
        color: #303133;
    }
</style>