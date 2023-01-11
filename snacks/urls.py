from django.urls import path
from .views import HomePage,SnackListView,SnackDetail,SnackCreate,SnackUpdate,SnackDelete

urlpatterns=[
    path('',HomePage.as_view(), name='home'),
    path('snacks/',SnackListView.as_view(), name='snacks' ),
    path('snacks/<int:pk>',SnackDetail.as_view(), name='detail'),
    path("create/", SnackCreate.as_view(), name="create"),
    path("update/<int:pk>", SnackUpdate.as_view(), name="update"),
    path("delete/<int:pk>", SnackDelete.as_view(), name="delete"),

]