from django.urls import path
from member_app.api.views import MemberListAV, MemberDetailsAV
from member_app.api.views import MemberConfigListAV

urlpatterns = [
    path('', MemberListAV.as_view(), name='member-list-info'),  
    path('<int:pk>/', MemberDetailsAV.as_view(), name='member-details'),

    path('config/', MemberConfigListAV.as_view(), name='member-config-list-info'),  
]