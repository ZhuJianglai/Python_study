from django.conf.urls import url
from sign import views_if, view_if_sign
from sign import view_if_sec

urlpatterns = [
     # sign system interface:
     # ex : /api/add_event/
     url( r'^add_event/', views_if.add_event, name='add_event' ),
     # ex :/api/add_guest/
     url( r'^add_guest/', views_if.add_guest, name='add_guest' ),
     # ex :/api/get_event_list/
     url( r'^get_event_list/', views_if.get_event_list, name='get_event_list' ),
     # ex :/api/get_guest_list/
     url( r'^get_guest_list/', views_if.get_guest_list, name='get_guest_list' ),
     # ex :/api/user_sign/
     url( r'^user_sign/', views_if.user_sign, name='user_sign' ),

     # sign system interface:带auth认证
     # ex : /api/add_event/
     url(r'^add_event_sec/', view_if_sec.add_event_sec, name='add_event_sec'),
    # ex :/api/add_guest/
     url( r'^add_guest_sec/', view_if_sec.add_guest_sec, name='add_guest_sec'),
    # ex :/api/get_event_list/
     url( r'^get_event_list_sec/', view_if_sec.get_event_list_sec, name='get_event_list_sec'),
    # ex :/api/get_guest_list/
     url( r'^get_guest_list_sec/', view_if_sec.get_guest_list_sec, name='get_guest_list_sec'),
    # ex :/api/user_sign/
     url( r'^user_sign_sec/', view_if_sec.user_sign_sec, name='user_sign_sec'),

     # sign system interface:带数字签名
     # ex : /api/add_event_sign/
     url( r'^add_event_sign_sign/', view_if_sign.add_event_sign, name='add_event_sign' ),
     # ex :/api/add_guest_sign/
     url( r'^add_guest_sign_sign/', view_if_sign.add_guest_sign, name='add_guest_sign' ),
     # ex :/api/get_event_list_sign/
     url( r'^get_event_list_sign/', view_if_sign.get_event_list_sign, name='get_event_list_sign' ),
     # ex :/api/get_guest_list_sign/
     url( r'^get_guest_list_sign/', view_if_sign.get_guest_list_sign, name='get_guest_list_sign' ),
     # ex :/api/user_sign_sign/
     url( r'^user_sign_sign/', view_if_sign.user_sign_sign, name='user_sign_sign' ),

]