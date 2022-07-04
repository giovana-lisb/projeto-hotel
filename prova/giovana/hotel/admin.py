from django.contrib import admin

# Register your models here.
from .models import Hospede
from .models import Cidade
from .models import Estadia 
from .models import TidoEstadia
from .models import Produto

admin.site.register(Hospede)
admin.site.register(Cidade)
admin.site.register(Estadia)
admin.site.register(TidoEstadia)
admin.site.register(Produto)