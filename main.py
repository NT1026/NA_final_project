import argparse
import cv2
import enlarge_method_gray
import enlarge_method_rgb
import time 

method_help = """
Enlarge method: 
Use Nearest-Neighbor please set value as 1.
Use Bilinear Interpolation please set value as 2.
Use Bicubic Interpolation please set value as 3.
Use Lagrange Interpolation please set value as 4.
"""

method = {
    1: enlarge_method_gray.nearest_neighbor,
    2: enlarge_method_gray.bilinear_interpolation,
    3: enlarge_method_gray.bicubic_interpolation,
    4: enlarge_method_gray.lagrange_interpolation,
    5: enlarge_method_rgb.nearest_neighbor,
    6: enlarge_method_rgb.bilinear_interpolation,
    7: enlarge_method_rgb.bicubic_interpolation,
    8: enlarge_method_rgb.lagrange_interpolation
}

mode = {
    "GRAY": 1,
    "RGB": 3
}

filename = {
    1: "nearest_gray",
    2: "bilinear_gray",
    3: "bicubic_gray",
    4: "lagrange_gray",
    5: "nearest_rgb",
    6: "bilinear_rgb",
    7: "bicubic_rgb",
    8: "lagrange_rgb"
}

img_name = {
    "images/100x100.jpg": "100x100",
    "images/316x316.jpg": "316x316",
    "images/600x600.jpg": "600x600",
    "images/1600x1200.jpg": "1600x1200"
}


if __name__ == "__main__":
    # Parameter settings
    parser = argparse.ArgumentParser()
    configs = parser.add_argument_group(title="configurations")
    configs.add_argument("--enlarge", help="Enlarge magnitude.", type=int)
    configs.add_argument("--image", help="Path of your image.")
    configs.add_argument("--method", help=method_help, type=int)
    configs.add_argument("--mode", help="GRAY or RGB")
    args = parser.parse_args()

    # Parse parameter
    _magni = args.enlarge
    _img_path = args.image
    _method = args.method
    _mode = args.mode    

    # Result
    start_time = time.time()

    if _mode == "GRAY":
        src = cv2.imread(_img_path, cv2.IMREAD_GRAYSCALE)
        dst = method[_method](src, dst_shape=(src.shape[0] * _magni, src.shape[1] * _magni, mode[_mode]), magni=_magni)

    elif _mode == "RGB":
        src = cv2.imread(_img_path)
        _method += 4
        dst = method[_method](src, dst_shape=(src.shape[0] * _magni, src.shape[1] * _magni, mode[_mode]), magni=_magni)
        
    print(f"{_img_path}\t{_magni}\t{method[_method]}\t{time.time() - start_time} s")

    if _mode == "GRAY":
        cv2.imwrite(f"output/{_magni}x_{img_name[_img_path]}_{filename[_method]}.jpg", dst)

    elif _mode == "RGB":
        cv2.imwrite(f"output/{_magni}x_{img_name[_img_path]}_{filename[_method]}.jpg", dst)

    # Output
    # cv2.namedWindow('src', cv2.WINDOW_NORMAL) 
    # cv2.resizeWindow('src', src.shape[1], src.shape[0])
    # cv2.imshow("src",src) 

    # cv2.namedWindow('dst', cv2.WINDOW_NORMAL) 
    # cv2.resizeWindow('dst', dst.shape[1], dst.shape[0])
    # cv2.imshow("dst",dst)

    # Press any key to close the windows
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
