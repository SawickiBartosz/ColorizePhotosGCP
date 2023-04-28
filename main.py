from pathlib import Path

import functions_framework
import torch
from PIL import Image
import os
from gcp_project.deoldify_proxy import colorize_image
from gcp_project.cloud_functions_utils import serve_pil_image
from DeOldify.deoldify import device
from DeOldify.deoldify.device_id import DeviceId

@functions_framework.http
def transformed_image(request):
    # Your code here
    #choices:  CPU, GPU0...GPU7
    device.set(device=DeviceId.CPU)
    torch.backends.cudnn.benchmark=True
    image = Image.open(Path("DeOldify/test_images/image.png"))
    transformed = colorize_image(image)
    # Return an HTTP response
    return serve_pil_image(transformed)


@functions_framework.http
def original_image(request):
    # Your code here
    #choices:  CPU, GPU0...GPU7
    device.set(device=DeviceId.CPU)
    torch.backends.cudnn.benchmark=True
    image = Image.open(Path("DeOldify/test_images/image.png"))
    # Return an HTTP response
    return serve_pil_image(image)
