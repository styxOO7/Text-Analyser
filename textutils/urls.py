"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import veiws

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', veiws.index, name='index2'),
    # path('/redirect/', redirect_view),
    path('analyze', veiws.analyze, name='analyze2')
    # path('removePun', veiws.removePun, name='removepun'),
    # # path(x, y, z); x is path; y is function; z is name for further reference
    # path('spaceRemover', veiws.spaceRemover, name='spaceRemover'),
    # path('capitalizeFirst', veiws.capitalizeFirst, name='capitalizeFirst'),
    # path('newlineRemover', veiws.newlineRemover, name='newlineRemover'),
    # path('charCount', veiws.charCount, name='charCount')
]

