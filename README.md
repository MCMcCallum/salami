Salami Interface
===

This provides some handy functionality for pulling annotations / audio from the salami dataset.

The dataset and audio files are provided by some excellent third parties. This is just some handy code for using that data from python scripts.

The audio can be downloaded from functions in the `SALAMI` submodule.

The annotation data itself resides in the `salami-data-public` submodule.

Configuration
---

By default this salami interface assumes the audio to be in the directory `./mp3s`, and the annotations to be in the submodule directory `./salami-data-public/annotations`.

The audio and annotation directories can be configured in the config python module here.