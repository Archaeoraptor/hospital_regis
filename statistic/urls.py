from django.urls import path
from . import views
import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()


urlpatterns = [

    path('', views.statistic, name='statistic'),
    # path('<int:id>.html', views.model_index),
    # path(r'xadmin', xadmin.site.urls),

]




