import json
import numpy as np
import os

def folderCreate():
    if not(os.path.exists("images")):
        os.mkdir("images")
    if not(os.path.exists("checkpoints")):
        os.mkdir("checkpoints")

def calib_json_read(filename):
    with open(filename) as json_file:
        json_data = json.load(json_file)
        json_file.close()

    cal_data = {}
    file_ok = True
    try:
        cal_data["camera_matrix"] = np.asarray(json_data["camera_matrix"])
        cal_data["distortion_coeffs"] = np.asarray(json_data["distortion_coeffs"])
        cal_data["new_camera_matrix"] = np.asarray(json_data["new_camera_matrix"])
        cal_data["perspective_transformation"] = np.asarray(json_data["perspective_transformation"])
        ppmm = json_data["ppmm"]
    except:
        file_ok = False
    else:
        if (cal_data["camera_matrix"].shape != (3, 3) or
            cal_data["distortion_coeffs"].shape != (1, 5) or
            cal_data["new_camera_matrix"].shape != (3, 3) or
            cal_data["perspective_transformation"].shape != (3, 3) or
            not(isinstance(ppmm, (int, float)))):
            file_ok = False
    
    if file_ok:
        img_ppmm = ppmm
        return cal_data,img_ppmm