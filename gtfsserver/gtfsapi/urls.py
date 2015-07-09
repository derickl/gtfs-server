#from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from .views import FeedViewSet, AgencyViewSet, RouteViewSet, GeoRouteViewSet, StopViewSet, GeoStopViewSet

router = routers.SimpleRouter()
router.register(r'feeds', FeedViewSet)

feeds_router = routers.NestedSimpleRouter(router, r'feeds', lookup='feed')

feeds_router.register('agencies', AgencyViewSet)
feeds_router.register('routes.geojson', GeoRouteViewSet)
feeds_router.register('routes', RouteViewSet)
feeds_router.register('stops.geojson', GeoStopViewSet)
feeds_router.register('stops', StopViewSet)


urlpatterns = router.urls + feeds_router.urls
    