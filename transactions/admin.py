from django.contrib import admin

from .models import (
    IncomingTransactionDetail,
    IncomingTransactionHeader,
    OutgoingTransactionDetail,
    OutgoingTransactionHeader,
)


class IncomingTransactionHeaderAdmin(admin.ModelAdmin):
    pass


class IncomingTransactionDetailAdmin(admin.ModelAdmin):
    pass


class OutgoingTransactionHeaderAdmin(admin.ModelAdmin):
    pass


class OutgoingTransactionDetailAdmin(admin.ModelAdmin):
    pass


admin.site.register(IncomingTransactionHeader, IncomingTransactionHeaderAdmin)
admin.site.register(IncomingTransactionDetail, IncomingTransactionDetailAdmin)
admin.site.register(OutgoingTransactionHeader, OutgoingTransactionHeaderAdmin)
admin.site.register(OutgoingTransactionDetail, OutgoingTransactionDetailAdmin)
