#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Convert an image in a gds file
# File: mask2gds_LaDanza.gds
# date: 2017-12-04

from gdsCAD import *
from PIL import Image
import scipy.io
from scipy.misc import imread
from scipy.misc import imsave
import numpy as np


#### Convert the image in monochormatic and then in BW
#### The functions are two binarize_iamge and binarize_array

def binarize_image(img_path, target_path, threshold):
    """Binarize image"""
    image_file = Image.open(img_path)
    image = image_file.convert('L')
    image = np.array(image)
    image = binarize_array(image, threshold)
    #imsave(target_path, image)
    return image

def binarize_array(numpy_array, threshold=200):
    """Binarize numpy array"""
    for i in range (len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array

def get_gds(img_bw,pix,output):
    cell=core.Cell('TOP')

    for ii in range(np.shape(img_bw)[0]):
        for jj in range(np.shape(img_bw)[1]):
            if image_bw[ii,jj]==255:"""Taking the negative mask"""
                box=shapes.Rectangle(((ii)*pix,(jj)*pix),((ii+1)*pix,(jj+1)*pix))
                cell.add(box)
            else:
                continue

    # Create a Layout
    layout=core.Layout('LIBRARY')
    layout.add(cell)
    layout.save("output")


"""Input output parsing"""
def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input",
                        dest="input",
                        help="read this file",
                        metavar="FILE",
                        required=True)
    parser.add_argument("-o", "--output",
                        dest="output",
                        help="write binarized file hre",
                        metavar="FILE",
                        required=True)
    parser.add_argument("--threshold",
                        dest="threshold",
                        default=200,
                        type=int,
                        help="Threshold when to show white")
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    image_bw = binarize_image(args.input, args.output, args.threshold)
    pix=0.5
    get_gds(image_bw,pix,"./LaDanza/prova.gds")
