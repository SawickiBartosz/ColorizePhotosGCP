# GCP Project
## DeOldify model for image colorization


## How to run?
Download `ColorizeArtistic_gen.pth` pretrained weights from [original repo-pretrained weights](https://github.com/ArielReplicate/DeOldify#pretrained-weights) 
and copy to `DeOldify/models`.

Add `DeOldify.` after cloning the submodule. My way was to try to run function and see where there is an import error.  

Run using `functions-framework`. [link to tutorial](https://cloud.google.com/functions/docs/running/function-frameworks#functions-local-ff-configure-python).
Run command `functions-framework --target=transformed_image` in main directory to get transformed image at localhost:8080.
Run command `functions-framework --target=original_image` in main directory to get original image at localhost:8080. 
You can open in browser to see.

## What was added?

`gcp_project` module. it's a patchwork of stackoverflow, google cloud tutorials, and unwrapped functions
used in notebook `DeOldify/ImageColorizer.ipynb`. I added links in the comments in code.


## TO DO
* Change paths (imports) to `fastai` package, such that implementation from `DeOldify` is used. Especially 293 line of `core.py`. 
`collections.Sized` in original (not working) vs. `collections.abc.Sized` in `DeOldify.fastai` (works).
* add storage triggers to functions [tutorial](https://cloud.google.com/functions/docs/tutorials/storage#functions_tutorial_helloworld_storage-python)
* optimize requirements and modules
* link functions and storage (probably via firebase project)
* deploy
