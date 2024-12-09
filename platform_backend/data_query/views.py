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
        print(province, city)
        try:
            nodes = RoadNode.objects.filter(province=province, city=city).values()
            node_list = list(nodes)
        except Exception as e:  # 未能获取到节点信息
            print(e)
            return JsonResponse({'code': 500, 'message': '您所查询的地区不存在交通节点信息！'})

        return JsonResponse({'code': 200, 'nodes': node_list})



