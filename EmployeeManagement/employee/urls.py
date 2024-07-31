from django.urls import path

from employee import views

urlpatterns = [

    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('add_employee',views.add,name='add'),
    path('home',views.home,name='home'),
    path('view_employee',views.view,name='view'),
    path('employee/<int:emp_id>/update/',views.update,name='update'),
    path('employee/<int:emp_id>/delete/',views.delete,name='delete'),
    path('logout',views.logout,name="logout")
]
