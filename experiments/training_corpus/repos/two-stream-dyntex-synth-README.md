# Two-Stream Convolutional Networks for Dynamic Texture Synthesis

![Dynamic texture synthesis](teaser.gif "Dynamic texture synthesis")

## Requirements
- Tensorflow 1.3 (or latest, although not tested)
- Preferably a Titan X for synthesizing 12 frames
- Appearance-stream [tfmodel](https://drive.google.com/open?id=19KkFi92oWLzuOWnGo6Zsqe-2CCXFAoXZ)
- Dynamics-stream [tfmodel](https://drive.google.com/open?id=1DHnzoNO-iTgMUTbUOLrigEmpPHmn_mT1)
- [Dynamic textures](https://drive.google.com/open?id=0B5T9jWfa9iDySWJHZnpNZ2dHWUk)
- [Static textures](https://drive.google.com/open?id=11yMiPXiuYvLCyoLfQf_dEG6kuav8h6_3) (for dynamics style transfer)

## Setup
1. Store the appearance-stream tfmodel in `./models`.
2. Store the dynamics-stream tfmodel in `./models`. The filepath to this model is your `--dynamics_model` path.

## Dynamic texture synthesis
```
python synthesize.py --type=dts --gpu=<NUMBER> --runid=<NAME> --dynamics_target=data/dynamic_textures/<FOLDER> --dynamics_model=models/<TFMODEL>
```

Store your chosen dynamic texture image sequence in a folder in `/data/dynamic_textures`. This folder is your `--dynamics_target` path.

#### Example usage
```
python synthesize.py --type=dts --gpu=0 --runid="my_cool_fish" --dynamics_target=data/dynamic_textures/fish --dynamics_model=models/MSOEnet_ucf101train01_6e-4_allaug_exceptscale_randorder.tfmodel
```

## Dynamics style transfer
```
python synthesize.py --type=dst --gpu=<NUMBER> --runid=<NAME> --dynamics_target=data/dynamic_textures/<FOLDER> --dynamics_model=models/<TFMODEL> --appearance_target=data/textures/<IMAGE>
```

Store your chosen static texture in `./data/textures`. The filepath to this texture is your `--appearance_target` path.

#### Example usage
```
python synthesize.py --type=dst --gpu=0 --runid="whoa_water!" --dynamics_target=data/dynamic_textures/water_4 --appearance_target=data/textures/water_paint_cropped.jpeg --dynamics_model=models/MSOEnet_ucf101train01_6e-4_allaug_exceptscale_randorder.tfmodel
```

## Temporally-endless dynamic texture synthesis
```
python synthesize.py --type=inf --gpu=<NUMBER> --runid=<NAME> --dynamics_target=data/dynamic_textures/<FOLDER> --dynamics_model=models/<TFMODEL>
```

## Incremental dynamic texture synthesis
```
python synthesize.py --type=inc --gpu=<NUMBER> --runid=<NAME> --dynamics_target=data/dynamic_textures/<FOLDER> --dynamics_model=models/<TFMODEL> --appearance_target=data/textures/<IMAGE>
```

Store your chosen static texture in `/data/textures`. The filepath to this texture is your `--appearance_target` path. This texture should be the last frame of a previously generated sequence.

## Static texture synthesis
```
python synthesize.py --type=sta --gpu=<NUMBER> --runid=<NAME> --appearance_target=data/textures/<IMAGE>
```

[Gatys et al.'s](https://arxiv.org/abs/1505.07376) method of texture synthesis.

## Notes
The network's output is saved at `data/out/<RUNID>`.

Use `./useful_scripts/makegif.sh` to create a gif from a folder of images, e.g.,
```
./useful_scripts/makegif.sh "data/out/calm_water/iter_6000*" calm_water.gif
```
will create the gif `calm_water.gif` from the images `iter_6000*` in the `calm_water` output folder.

Logs and snapshots are created and stored in `./logs/<RUNID>` and `./snapshots/<RUNID>`, respectively. You can view the loss progress for a particular run in Tensorboard.

## Citation
```
@inproceedings{tesfaldet2018,
  author = {Matthew Tesfaldet and Marcus A. Brubaker and Konstantinos G. Derpanis},
  title = {Two-Stream Convolutional Networks for Dynamic Texture Synthesis},
  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2018}
}
```

## License
Two-Stream Convolutional Networks for Dynamic Texture Synthesis
Copyright (C) 2018  Matthew Tesfaldet

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.


For questions, please contact Matthew Tesfaldet ([mtesfald@eecs.yorku.ca](mailto:mtesfald@eecs.yorku.ca)).
