import L from 'leaflet';

export const getColor = (value) => { // 帮助计算节点颜色的函数
    const minValue = 0;
    const maxValue = 2000;
    const normalizedValue = Math.max(minValue, Math.min(maxValue, value));
    const hue = 120 - (normalizedValue / maxValue) * 120;
    return `hsl(${hue}, 100%, 50%)`;
};

export const getMap = (containerId, latitude, longitude, zoom) => { // 帮助创建地图的函数

    const map = L.map(containerId).setView([latitude, longitude], zoom); // 使用传入的容器 ID

    // 添加地图图层
    L.tileLayer("http://t0.tianditu.gov.cn/vec_w/wmts?" +
        "SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=vec&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles" +
        "&TILECOL={x}&TILEROW={y}&TILEMATRIX={z}&tk=93b39d8073f49ca3ed46bc63841115b7"
    ).addTo(map);

    L.tileLayer(
        "https://t0.tianditu.gov.cn/cva_w/wmts?" +
        "SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=cva&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles" +
        "&TILECOL={x}&TILEROW={y}&TILEMATRIX={z}&tk=93b39d8073f49ca3ed46bc63841115b7"
    ).addTo(map);

    return map; // 返回地图实例
};

export function initializeTooltipPopup() {
    // 重新定义 Tooltip 的动画缩放方法
    L.Tooltip.prototype._animateZoom = function (e) {
        if (!this._map) return;
        let pos = this._map._latLngToNewLayerPoint(this._latlng, e.zoom, e.center);
        this._setPosition(pos);
    };

    L.Tooltip.prototype._updatePosition = function () {
        if (!this._map) return;
        let pos = this._map.latLngToLayerPoint(this._latlng);
        this._setPosition(pos);
    };

    // 重新定义 Popup 的动画缩放方法
    L.Popup.include({
        _animateZoom(e) {
            if (this._map) {
                const pos = this._map._latLngToNewLayerPoint(this._latlng, e.zoom, e.center);
                const anchor = this._getAnchor();
                L.DomUtil.setPosition(this._container, pos.add(anchor));
            }
        },
    });
}