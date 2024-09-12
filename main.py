import utils as ut
import argparse
import os
import cv2

import DexiNed.main as Dx

if __name__ == "__main__":
    ut.folderCreate()
    calib_data,img_ppmm = ut.calib_json_read(f"images/calibJson/1209_cam1.json")
    for path in os.listdir("images/camera"):
        img = cv2.imread(f"images/camera/{path}")
        if not(os.path.exists(f"images/calibCamera/{path}")):
            img_ud = cv2.undistort(img, calib_data["camera_matrix"], 
                                    calib_data["distortion_coeffs"], None, 
                                    calib_data["new_camera_matrix"])
            cv2.imwrite(f"images/calibCamera/{path}",img_ud)
        
        if not(os.path.exists(f"images/dexined/BIPED2CLASSIC/fused/{path[:-4]}.png")):
            Dx.main(Dx.parse_args())

        if not(os.path.exists(f"images/subpixel/{path}")):
            pass