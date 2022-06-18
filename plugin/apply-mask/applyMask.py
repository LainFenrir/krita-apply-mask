"""
    apply mask is a plugin made to apply masks and layer styles while keeping the opacity of the layer intact.
    Copyright (C) 2022  LunarKreatures

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# For autocomplete
import time
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *
else:
    from krita import *

class ApplyMask(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    # Krita.instance() exists, so do any setup work
    def setup(self):
        pass

    # called after setup(self)
    def createActions(self, window):
        # added action to layer menu cause it makes much more sense to be there than in scripts
        action = window.createAction("applyMask", "Apply masks to current layer", "layer")
        action.triggered.connect(self.applyMask)
        pass

    def applyMask(self):
        application = Krita.instance()
        currentDoc = application.activeDocument()
        currentLayer = currentDoc.activeNode()
        
        # allows user to have one of the masks selected when using apply mask
        # also avoids the plugin breaking when having one of the masks selected
        if currentLayer.type() in ["transparencymask","filtermask","transformmask","selectionmask","colorizemask"]:
            currentLayer = currentLayer.parentNode()
        # when the layer is flattened the selection mask is set to inactive, but i cant change it back to active from code
        # there is no function i can call to set it to active (from what i looked)

        originalOP = currentLayer.opacity()
        currentLayer.setOpacity(255)
        application.action('flatten_layer').trigger()
        # the sleep is necessary otherwise the flatten layer is executed in parallel with the next instructions
        # probably an async process. since the sleep is fixed, any flatten that takes longer than it will mess up the next instructions
        # but i cant do anything about it cause flatten is only an action and i didnt find any signal that is sent when its over.
        time.sleep(1)

        # when the layer is merged, the string merged is added at the end of it, unless the layer already has it at the end
        # this avoids errors when the layer was already merged. also seems needed to look for the the merged name
        # Looking for active layer or trying to use the one before was not working
        if ' Merged' in currentLayer.name():
            layerMerged = currentDoc.nodeByName(currentLayer.name())
        else:
            layerMerged = currentDoc.nodeByName(currentLayer.name()+' Merged')
        layerMerged.setOpacity(originalOP)
        currentDoc.refreshProjection()
    

