from io import BytesIO

from google.cloud import storage
from PIL import Image

# based on https://cloud.google.com/storage/docs/downloading-objects#storage-download-object-python
# https://cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_download_as_bytes

def get_photo(bucket_name, blob_name) -> Image.Image:
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob_bytes = blob.download_as_bytes()
    img = Image.open(BytesIO(blob_bytes)).convert('RGB')
    return img
