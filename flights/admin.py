from django.contrib import admin

from flights.models import (
Airplane,
AirplaneType,
Airport,
Crew,
Flight,
Order,
Route,
Ticket,
)

class TicketInLine(admin.TabularInline):
    model = Ticket
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin)
    inlines = (TicketInLine,)

admin.site.register(Airplane)
admin.site.register(AirplaneType)
admin.site.register(Airport)
admin.site.register(Crew)
admin.site.register(Flight)
admin.site.register(Route)
admin.site.register(Ticket)
