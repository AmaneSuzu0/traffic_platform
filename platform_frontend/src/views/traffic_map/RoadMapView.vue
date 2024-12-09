<template>
    <div class="home">
        道路交通流量地图
        <div id="map" style="height: 100vh;"></div> <!-- 地图容器 -->
    </div>
</template>

<script setup>
    import { onMounted, ref, onUnmounted } from 'vue';
    import L from 'leaflet'; // 导入 Leaflet
    import { getColor } from '@/utils/mapUtils'
    import requestUtil from '@/utils/request'
    import { ElMessage } from 'element-plus';
    import { initializeTooltipPopup } from '@/utils/mapUtils';


    // 创建一个 ref 来存储地图实例
    const map = ref(null);
    // 地图初始化逻辑
    const initMap = () => {
        map.value = L.map('map').setView([36.067, 120.387], 12); // 初始化地图

        // 添加地图图层
        L.tileLayer("http://t0.tianditu.gov.cn/vec_w/wmts?" +
            "SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=vec&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles" +
            "&TILECOL={x}&TILEROW={y}&TILEMATRIX={z}&tk=93b39d8073f49ca3ed46bc63841115b7"
        ).addTo(map.value);

        L.tileLayer(
            "https://t0.tianditu.gov.cn/cva_w/wmts?" +
            "SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=cva&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles" +
            "&TILECOL={x}&TILEROW={y}&TILEMATRIX={z}&tk=" +
            "93b39d8073f49ca3ed46bc63841115b7"
        ).addTo(map.value);

        if (map.value) {
            // 调用初始化 Tooltip 和 Popup 的函数
            initializeTooltipPopup();
        }
    };


    const fetchNodes = async () => {
        try {
            let result = await requestUtil.get('/data_query/get_nodes', {
                province: '山东省',
                city: '青岛市',
                node_type: '道路交通',
            });

            let data = result.data;
            if (data.code === 200) {
                // 请求成功，处理节点信息
                console.log(data.nodes); // 假设节点信息在 data.nodes 中
                data.nodes.forEach(node => { // 遍历节点信息 // 根据返回的数据结构获取字段
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

    // 在组件挂载时初始化地图
    onMounted(async () => {
        await initMap(); // 初始化地图
        await fetchNodes(); // 初始请求节点信息
    });
</script>


<style lang="scss" scoped>
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

    .custom-popup {
        font-size: 8px;
        /* 确保字体大小适合显示 */
        line-height: 1.2;
        /* 可选，调整行高 */
        margin: 0;
        /* 确保没有额外的边距 */
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