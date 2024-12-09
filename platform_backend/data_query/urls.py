from django.urls import path
from data_query.views import GetNodesView

urlpatterns = [
    path('get_nodes', GetNodesView.as_view(), name='get_nodes'),  # 获取交通节点信息
]