<template>
    <div class="home">道路交通流量地图
        <div class="selector-container">
            <AreaSelector v-model="selectedAddresses"></AreaSelector>
            <el-button type="primary" plain class="query_button" @click="fetchNodes">查询</el-button>
        </div>
        <div class="selected_info">
            <h3>当前选中的地址:</h3>
            <p>{{ selectedAddresses}}</p>
        </div>
        <div id="map" style="height: 100vh;"></div> <!-- 地图容器 -->
    </div>
</template>

<script setup>
    import { onMounted, ref, onUnmounted } from 'vue';
    import L from 'leaflet'; // 导入 Leaflet
    import { getColor, getMap, initializeTooltipPopup } from '@/utils/mapUtils'
    import requestUtil from '@/utils/request'
    import { ElMessage } from 'element-plus';
    import AreaSelector from '@/layout/main/AreaSelector.vue';


    // 创建一个 ref 来存储地图实例
    const map = ref(null);
    const selectedAddresses = ref(["山东省", "青岛市"]); // 存储选中的地址
    const markers = ref([]); // 存储所有的标记

    // 地图初始化逻辑
    const initMap = () => {
        // 调用分离的 getMap 函数
        map.value = getMap('map', 36.067, 120.387, 12); // 传入容器 ID、纬度和经度
        // 初始化 Tooltip 和 Popup
        initializeTooltipPopup();
    };



    const fetchNodes = async () => {
        try {
            // 清除之前的标记
            markers.value.forEach(marker => {
                map.value.removeLayer(marker); // 从地图上移除标记
            });
            markers.value = []; // 清空标记数组

            let province = selectedAddresses.value[0] || ''; // 确保有值
            let city = selectedAddresses.value[1] || '';
            let district = selectedAddresses.value[2] || ''; // 如果没有区可以设置为 ''
            let result = await requestUtil.get('/data_query/get_nodes', {
                province: province,
                city: city,
                district: district,
                node_type: '道路交通',
            });

            let data = result.data;
            if (data.code === 200) {
                // 请求成功，处理节点信息
                console.log(data.nodes); // 假设节点信息在 data.nodes 中
                data.nodes.forEach(node => {
                    const latitude = node.latitude;
                    const longitude = node.longitude;
                    const node_name = node.node_name;
                    const max_traffic = 2000; // 最大流量值
                    const min_traffic = 0; // 最小流量值
                    const value = Math.floor(Math.random() * (max_traffic - min_traffic + 1)) + min_traffic; // 随机生成流量值

                    // 添加圆形标记到地图
                    const color = getColor(value); // 获取颜色
                    // 创建圆形标记
                    const marker = L.circleMarker([latitude, longitude], {
                        radius: 10, // 圆圈半径
                        fillColor: color,
                        color: color,
                        weight: 1,
                        opacity: 1,
                        fillOpacity: 0.8, // 透明度
                    }).addTo(map.value);

                    // 为标记绑定弹出窗口
                    marker.bindPopup(`位置: ${node_name}<br>流量为: ${value}`,);

                    // 将标记加入到数组中
                    markers.value.push(marker);
                });
            } else {
                // 请求失败,处理错误消息
                console.log(data.message);
                ElMessage.error(data.message);
            }
        } catch (error) {
            console.error("请求错误:", error);
            ElMessage.error('请求时发生错误，请稍后重试。');
        }
    };

    const clickQueryButton = () => {
        initMap(); // 重新初始化地图
        fetchNodes(); // 重新请求节点信息
    }

    // 在组件挂载时初始化地图
    onMounted(async () => {
        await initMap(); // 初始化地图
        await fetchNodes(); // 初始请求节点信息
    });
</script>


<style lang="scss">
    .home {
        padding: 40px;
        font-size: 30px;
        font-weight: bold;
    }

    .map {
        height: 90%;
        /* 确保地图容器有足够的高度 */
        width: 100%;
        /* 确保地图容器占满可用宽度 */
        margin-top: 20px;
    }

    .selector-container {
        display: flex;
        /* 使用 flexbox 布局 */
        align-items: center;
        /* 垂直居中对齐 */
    }

    .selector-container el-button {
        margin-left: 10px;
        /* 设置选择器和按钮之间的边距 */
    }

    .query_button {
        margin-left: 10px;
        /* 设置查询按钮的边距 */
    }

    .selected_info {
        font-size: 20px;
        margin-top: 5px;
    }
</style>

<style>
    /* 全局更改Leaflet popup的样式 */
    .leaflet-popup-content {
        font-size: 13px !important;
        line-height: 1.2 !important;
        margin: 14px !important;
    }

    .leaflet-popup-content-wrapper {
        padding: 2px !important;
        border-radius: 8px !important;
    }

    .leaflet-popup {
        margin-bottom: 5px !important;
    }

    .leaflet-container {
        font: 12px/1.2 Arial, Helvetica, sans-serif !important;
    }
</style>