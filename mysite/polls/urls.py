from django.conf.urls import url
from . import views
# from collection import views

# urlpatterns = [
#     url(r'^index/$', views.AboutUsView.as_view(), name='index'),
# ]

# urlpatterns = [
#     url(r'^$', views.AboutUsView.as_view(), name='index'),
# ]
#
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

# urlpatterns = [
#     # we're using a class-based view here!
#     url(r'^about-us/$', views.AboutUsView.as_view(), name='about_us'),
#  ]

# url(r'^about-us/$', views.AboutUsView.as_view(), name='about_us'),


urlpatterns = [
    # ex: /polls/
    url(r'^$', views.AboutUsView.as_view(), name='index'),

    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
