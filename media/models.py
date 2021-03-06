from django.db import models


# -id: Unique id will be generated by in Serializer function
# -name: string ( Name of the file )
# -media_type: string ( Type of the file)
# -created_at: time ( Timestamp of file created )
# -updated_at: time ( Timestamp of file last updated )

class Media(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    media_type = models.CharField(max_length=50, blank=False, default='')
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
