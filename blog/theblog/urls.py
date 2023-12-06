from django.urls import path
#from . import views
from .views import HomeView
from .views import ArticleDetailView
from .views import ProfileView
from .views import AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView
from .views import CategoryView
urlpatterns = [
    #path('',views.home,name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('author/<int:pk>', ProfileView.as_view(), name='Auth_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]