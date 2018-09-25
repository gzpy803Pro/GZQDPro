from django.conf.urls import url

from art import views


urlpatterns = [
    # 四种贪婪模式(次数):  *, +, ?, {m, n}
    url(r'^show/(\d+)/', views.show),
    url(r'^qbuy/(\d+)/', views.qbuy_book),
    url(r'^query_qbuy/(\d+)/', views.query_qbuy),
]
