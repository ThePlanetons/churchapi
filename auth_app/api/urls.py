from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     # path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]