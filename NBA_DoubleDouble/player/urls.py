from django.conf.urls import url ,include

from .views import (
    welcome_page,
    list_result,
    )
    
urlpatterns = [
    url(r'^$', welcome_page),
    url(r'list/$', list_result),
]
