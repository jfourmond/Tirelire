from rest_framework.routers import DefaultRouter
from bank import views

router = DefaultRouter()
router.register(r'', views.BankView, basename="bank")


urlpatterns = router.urls
