from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path("eventpage",views.eventpage,name="eventpage"),
    path("clubpage",views.clubpage,name="clubpage"),
    path("gallerypage",views.gallerypage,name="gallerypage"),
    path("clubdash",views.clubdash,name="clubdash"),
    path("Dash",views.Dash,name="Dash"),
    path("eventdash",views.eventdash,name="eventdash"),
    path("messagedash",views.messagedash,name="messagedash"),
    path("forgotp",views.forgotp,name="forgotp"),
    path("usercal",views.usercal,name="usercal"),
    path("payment",views.payment,name="payment"),
    path('event_list', views.event_list, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/book/', views.book_event, name='book_event'),
]