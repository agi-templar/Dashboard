from django.conf.urls import url
from django.contrib import admin
from dashboardapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.home, name='home'),

    # SIGN IN ROUTES
     url(r'^restaurant/sign-in/$', auth_views.login,
        {'template_name': 'restaurant/sign_in.html'},
        name = 'restaurant-sign-in'),

    # SIGN OUT ROUTES
    url(r'^restaurant/sign-out', auth_views.logout,
        {'next_page': '/'},
        name = 'restaurant-sign-out'),

    # SIGN UP ROUTES
    url(r'^restaurant/sign-up', views.restaurant_sign_up,
    name = 'restaurant-sign-up'),

    # RESTAURANT PAGE
    url(r'^restaurant/$', views.restaurant_home, name = 'restaurant-home')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
