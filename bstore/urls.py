from django.urls import path

from bstore.models import comments
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newbook", views.newbook, name="newbook"),
    path('book/<int:id>', views.book, name='book'),
    path('chapters/<int:idd>',views.chapterssubmit,name='chapters'),
    path('rewards/<int:iddd>', views.rewardssubmit, name='rewards'),
    path('comments', views.addcomments, name='comments'),
    path('test', views.testing, name='testing'),
    path('testt', views.testt, name='testt'),
    path('cards', views.cards, name='cards'),
    path('categories/<int:idddd>', views.allcategories, name='allcategries'),
    path('cart/<int:book_id>', views.cart, name='cart'),
    path('thecart', views.thecart, name='thecart'),
    path('requests', views.therequests, name='requests'),
    path('finished/<int:iddddd>',views.finished, name='finished'),
    path('details/<int:idddddd>',views.requestdetails, name='details')
]