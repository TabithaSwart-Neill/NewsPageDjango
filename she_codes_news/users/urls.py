from django.urls import path
from .views import CreateAccountView
from .views import ChangeAccountView
from .views import AccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
name='createAccount'),
    path('change-account/', ChangeAccountView.as_view(),
name='changeAccount'),  
    path('view-account/<int:pk>', AccountView.as_view(),
name='viewAccount'),
]