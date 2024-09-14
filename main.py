import utils as ut
import argparse
import os
import cv2

import DexiNed.main as Dx
from subpixelEedges.main import edgeDetection

if __name__ == "__main__":
    ut.folderCreate()
    for path in os.listdir("images/calibCamera"):
        img = cv2.imread(f"images/calibCamera/{path}")
        if not(os.path.exists(f"images/dexined/BIPED2CLASSIC/fused/{path[:-4]}.png")):
            Dx.main(Dx.parse_args())
        if not(os.path.exists(f"images/subpixelEedges/{path}")):
            edgeDetection(path)
