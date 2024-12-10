from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from data_query.models import RoadNode


class GetNodesView(View):
    """获取交通节点信息"""

    def get(self, request):
        province = request.GET.get('province')
        city = request.GET.get('city')
        district = request.GET.get('district')
        node_type = request.GET.get('node_type')
        print(province, city, district,node_type)

        # 创建过滤条件字典
        filters = {'node_type': node_type}  # 至少需要 node_type

        # 根据存在的参数动态添加过滤条件
        if province:
            filters['province'] = province
        if city:
            filters['city'] = city
        if district:
            filters['district'] = district

        try:
            # 根据构造的过滤条件查询节点
            nodes = RoadNode.objects.filter(**filters).values()
            node_list = list(nodes)
        except Exception as e:  # 未能获取到节点信息
            print(e)
            return JsonResponse({'code': 500, 'message': '您所查询的地区不存在交通节点信息！'})

        return JsonResponse({'code': 200, 'nodes': node_list})



