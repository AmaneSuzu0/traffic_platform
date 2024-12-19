from django.db import models
from rest_framework import serializers


# Create your models here.

class RoadNode(models.Model):
    """道路节点表"""
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=100, verbose_name="省份")
    city = models.CharField(max_length=100, verbose_name="城市")
    district = models.CharField(max_length=100, verbose_name="区县")
    node_name = models.CharField(max_length=255, verbose_name="道路节点名称")
    node_type = models.CharField(max_length=50, verbose_name="节点类型")  # 新增节点类型字段
    longitude = models.FloatField(verbose_name="经度")
    latitude = models.FloatField(verbose_name="纬度")
    description = models.TextField(null=True, blank=True, verbose_name="描述信息")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="最近更新时间")

    class Meta:
        db_table = "road_nodes"


class RoadNodeSerializer(serializers.ModelSerializer):
    """用于把一个道路节点对象转换成序列号json数据"""

    class Meta:
        model = RoadNode  # 指明是哪个模型类
        fields = '__all__'  # 指明要序列化的字段，这里是全部字段


class TrafficHistory(models.Model):
    """历史流量表"""
    id = models.AutoField(primary_key=True)
    node = models.ForeignKey(RoadNode, on_delete=models.CASCADE, related_name="traffic_history", verbose_name="道路节点")
    date = models.DateField(verbose_name="日期")
    time_slot = models.CharField(max_length=50, verbose_name="时间段")
    traffic_value = models.IntegerField(verbose_name="流量值")
    weather_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="天气信息")
    special_events = models.CharField(max_length=255, null=True, blank=True, verbose_name="特殊事件")

    class Meta:
        db_table = "traffic_history"


class TrafficHistorySerializer(serializers.ModelSerializer):
    """用于把一个历史流量对象转换成序列号json数据"""

    class Meta:
        model = TrafficHistory  # 指明是哪个模型类
        fields = '__all__'  # 指明要序列化的字段，这里是全部字段


class TrafficForecast(models.Model):
    """流量预测表"""
    id = models.AutoField(primary_key=True)
    node = models.ForeignKey(RoadNode, on_delete=models.CASCADE, related_name="traffic_forecast", verbose_name="道路节点")
    forecast_date = models.DateField(verbose_name="预测日期")
    time_slot = models.CharField(max_length=50, verbose_name="时间段")
    forecast_value = models.IntegerField(verbose_name="预测流量值")
    model_version = models.CharField(max_length=100, null=True, blank=True, verbose_name="模型版本")

    class Meta:
        db_table = "traffic_forecast"


class TrafficForecastSerializer(serializers.ModelSerializer):
    """用于把一个流量预测对象转换成序列号json数据"""

    class Meta:
        model = TrafficForecast  # 指明是哪个模型类
        fields = '__all__'  # 指明要序列化的字段，这里是全部字段


class TaxiTrace(models.Model):
    """出租车数据表"""
    id = models.AutoField(primary_key=True)
    taxi_id = models.CharField(max_length=100, verbose_name="出租车车牌号")
    longitude = models.FloatField(verbose_name="经度")
    latitude = models.FloatField(verbose_name="纬度")
    speed = models.FloatField(verbose_name="速度")
    direction = models.IntegerField(verbose_name="方向")
    gps_time = models.DateTimeField(verbose_name="GPS 时间")
    base_time = models.DateTimeField(verbose_name="基准时间")
    status = models.IntegerField(verbose_name="状态")

    class Meta:
        db_table = "taxi_trace"


class TaxiTraceSerializer(serializers.ModelSerializer):
    """用于把一个出租车数据对象转换成序列号json数据"""
    class Meta:
        model = TaxiTrace  # 指明是哪个模型类
        fields = '__all__'  # 指明要序列化的字段，这里是全部字段


class TaxiInfo(models.Model):
    """出租车信息表"""
    id = models.AutoField(primary_key=True)
    taxi_name = models.CharField(max_length=100, verbose_name="出租车车牌号")

    class Meta:
        db_table = "taxi_info"
