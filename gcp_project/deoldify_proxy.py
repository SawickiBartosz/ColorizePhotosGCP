from pathlib import Path

from PIL import Image

from DeOldify.deoldify.filters import MasterFilter, ColorizerFilter
from DeOldify.deoldify.generators import gen_inference_deep


def colorize_image(orig_image: Image.Image):
    # unwrapped functions from deoldify module and demo notebook
    weights_name: str = 'ColorizeArtistic_gen'
    render_factor: int = 35  # value proposed by authors, higher means more compute complexity
    root_folder = Path('./DeOldify/')
    learn = gen_inference_deep(root_folder=root_folder, weights_name=weights_name)
    filtr = MasterFilter([ColorizerFilter(learn=learn)], render_factor=render_factor)
    filtered_image = filtr.filter(
        orig_image, orig_image, render_factor=render_factor,post_process=True
    )
    return filtered_image
