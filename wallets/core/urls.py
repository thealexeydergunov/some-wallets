from rest_framework import routers

from core import views


router_v1 = routers.DefaultRouter()
router_v1.register('wallets', views.WalletViewSet)
router_v1.register('transactions', views.TransactionViewSet)
