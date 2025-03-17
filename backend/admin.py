from django.contrib import admin
from backend.models import LegalDb
from Frontend.models import LawyerDb
import logging
logger = logging.getLogger(__name__)
# Register your models here.
admin.site.register(LegalDb)
class LawyerDbAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Qualification', 'Specialization', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['Name', 'Specialization']
    actions = ['approve_lawyers']

    def approve_lawyers(self, request, queryset):
        try:
            count = queryset.update(is_approved=True)
            self.message_user(request, f"{count} lawyer(s) approved successfully.")
        except Exception as e:
            logger.exception("Error approving lawyers: %s", str(e))
            self.message_user(request, "Error approving lawyers. Please check logs for details.", level="ERROR")
    approve_lawyers.short_description = "Approve selected lawyers"

admin.site.register(LawyerDb, LawyerDbAdmin)
