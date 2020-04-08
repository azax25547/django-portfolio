from django.urls import path
from .views import all_blogs, detail

urlpatterns = [
    path("", all_blogs, name="all_blogs"),
    path("<int:blog_id>", detail, name="detail"),
]
