# custom_storages.py
from django.conf import settings
from storages.backends import s3boto

class StaticStorage(S3BotoStorage):
	location = settings.STATICFILES_LOCATION
	#location = 'static'

class MediaStorage(S3BotoStorage):
        location = settings.MEDIAFILES_LOCATION
	#location = 'media'
