from django.urls import path
from .views import CustomTokenObtainPairView, UserListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
#     path('me/', UserProfileView.as_view(), name='user-profile'),

#     path('password/reset/', PasswordResetView.as_view(), name='password-reset'),
#     path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
#     path('password/change/', PasswordChangeView.as_view(), name='password-change'),
#     # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     # path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

#     path('social/google/', GoogleLoginView.as_view(), name='google-login'),
#     path('social/facebook/', FacebookLoginView.as_view(), name='facebook-login'),
# ]