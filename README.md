# krita-apply-mask
A krita plugin that adds a way to apply masks and layer styles while keeping the layer opacity intact.
It works like the flatten layer but if the layer has lower opacity this opacity is kept intact. 

Right now the only way to apply a mask or layer style in krita is by using the flatten layer action. however this has a huge problem. When using flatten layer option to apply masks to a layer and the layer has the opacity different from 100%, the result of the flattened layer opacity will change to 100% but this 100% will be previous opacity value.

Example: a layer with 58% opacity when flattening with a transparency or transform mask, the result will be the layer at 100% but this 100% is the 58% that was previously.

This plugin avoids that by doing these steps:
1. saves the original opacity of the layer
2. change the layer opacity to 100%
3. flattens the layer using the krita action
4. changes the opacity back to what it was

Which would be the same steps to avoid this behavior if done manually.

## Installation

Download the file either by going to code> download zip or go to the releases page and download there.

Have your krita resource folder open. for that, open krita go to settings>manage resources>open resource folder. 

After downloading, unzip the contents. copy the `apply-mask.desktop` and `apply-mask` and paste inside the `pykrita` folder inside the resource folder.
copy the `apply-mask.action` to the `actions` folder in the resource folder. if you dont have an actions folder you can just copy the folder to the resource folder.

After copying the contents, open krita (if you already have it open close and open it again), go to settings> configure krita>python manager activate the `Apply mask` plugin.
Close and open krita again and open the layer menu, if you see a new entry with "apply mask to current layer" at the bottom its working

## How to use

Select the layer with masks or layer styles you want to apply, go to layer>"apply mask to current layer" and it should apply keeping the opacity intact.
You can also set a shortcut to it in the keyboard shortcuts.
