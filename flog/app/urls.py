from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
from .forms import LoginForm


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^specify/(?P<pk>\d+)$', views.specify, name='specify'),
    url(r'^specify_del/(?P<pk>\d+)$', views.specify_del, name='specify_del'),
    url(r'^specify_new/(?P<pk>\d+)$', views.specify_new, name='specify_new'),
    url(r'^bigcategory_new$', views.bigcategory_new, name='bigcategory_new'),
    url(r'^category_new/(?P<pk>\d+)$', views.category_new, name='category_new'),
    url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^regist_save/$', views.regist_save, name='regist_save'),
    url(r'^login/$', LoginView.as_view(template_name='app/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^profile$', views.profile, name='profile'),

]