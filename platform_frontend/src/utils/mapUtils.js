import L from 'leaflet';

export const getColor = (value) => { // 帮助计算节点颜色的函数
    const minValue = 0;
    const maxValue = 2000;
    const normalizedValue = Math.max(minValue, Math.min(maxValue, value));
    const hue = 120 - (normalizedValue / maxValue) * 120;
    return `hsl(${hue}, 100%, 50%)`;
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
