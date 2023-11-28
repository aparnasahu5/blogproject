from django.urls import path
#from . import views
from .views import HomeView
from .views import ArticleDetailView
from .views import ProfileView

urlpatterns = [
    #path('',views.home,name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('author/<int:pk>', ProfileView.as_view(), name='Auth_detail'),
]