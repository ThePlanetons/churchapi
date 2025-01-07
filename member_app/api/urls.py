from django.urls import path
from member_app.api.views import MemberListAV, MemberDetailsAV

urlpatterns = [
    path('list/', MemberListAV.as_view(), name='member-list-info'),       
    path('<int:pk>/', MemberDetailsAV.as_view(), name='member-details'),      
]