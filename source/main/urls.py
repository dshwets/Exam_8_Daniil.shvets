"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from webapp.views import IndexView,CreateTodoView, DeleteTodoView, WatchTodoView, UpdateTodoView, Project_view, \
#     Watch_project_view, Create_project_view,ProjectToDoCreateView, ProjectUpdateView, ProjectDeleteView, ManageTeamView


from webapp.views.ProductView import Products_view, Watch_product_view, Create_product_view, ProductUpdateView, \
    ProductDeleteView
from webapp.views.Comment_views import ProductReviewCreateView, ReviewUpdateView,ReviewDeleteView
from django.contrib.auth.views import LogoutView, LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Products_view.as_view(), name='index_view'),
    # path('add/', CreateTodoView.as_view(), name='add'),
    # path('todo/<int:pk>/', WatchTodoView.as_view(), name='watch_todo'),
    # path('todo/<int:pk>/delete/', DeleteTodoView.as_view(), name='delete_todo'),
    # path('todo/<int:pk>/update/', UpdateTodoView.as_view(), name='update_todo'),
    #
    # path('projects/', Project_view.as_view(), name='projects'),
    path('products/<int:pk>/', Watch_product_view.as_view(), name='watch_product'),
    path('products/add/', Create_product_view.as_view(), name='add_product'),
    # path('projects/<int:pk>/to_do_action/add/', ProjectToDoCreateView.as_view(),
    #      name='project_todo_add'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    # path('projects/<int:pk>/manage_team/', ManageTeamView.as_view(), name='manage_team'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('products/<int:pk>/comments/add', ProductReviewCreateView.as_view(), name='add_review'),
    path('products/<int:pk>/comments/update', ReviewUpdateView.as_view(), name='update_review'),
    path('products/<int:pk>/comments/delete', ReviewDeleteView.as_view(), name='delete_review'),
    #
    path('accounts/', include('accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
