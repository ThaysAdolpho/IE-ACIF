from ieacif.viewsets import HomeViewset,ConsumoViewset,ConsumidoresViewset,EmpresasViewset,PesquisaViewset,TutoriaisPalestrasViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('homeapi', HomeViewset)
router.register('consumoapi', ConsumoViewset)
router.register('consumidoresapi', ConsumidoresViewset)
router.register('empresasapi', EmpresasViewset)
router.register('pesquisaapi', PesquisaViewset)
router.register('tutoriaispalestrasapi', TutoriaisPalestrasViewset)