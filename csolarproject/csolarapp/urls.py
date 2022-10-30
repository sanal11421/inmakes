from . import views
from django.urls import path



    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('detail/',views.detail,name='detail'),
    path('thanks/',views.thanks,name='thanks')
# ]
app_name='csolarapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_solar,name='add_solar'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]