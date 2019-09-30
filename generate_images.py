'''
Author: Mark Harvey

Description:

Converts Keras datasets in numpy array format to image files
in .png or .jpg formats. Mainly intended for use in calibration 
during quantization or for testing.

Note that the MNIST and Fashion MNIST arrays are 2D arrays (single-channel) but
will be converted to 3-channel RGB images.


Command line arguments:

--dataset: Choice of Keras dataset to download and convert.
         : Only possible valid choices are 'cifar10', 'cifar100', 'mnist', 'fashion_mnist'.
         : Default is 'mnist'.

--image_dir: Path to folder for saving the images and images list file.
           : If it doesn't already exist, it will be created.
           : Default is 'image_dir'.

--image_list: Name of images list file.
            : Will be written to folder specified by --image_dir.
            : Default is 'image_list.txt'.

--image_format: Specifies image file format.
              : Only possible valid choices are 'png','jpg' or 'bmp'.
              : Default is png

--max_images: Number of images to generate.
            : The conversion will start from the first element of the dataset.
            : Default is 1000
'''

import os
import argparse
import cv2
import tensorflow as tf

#from keras.preprocessing.image import save_img, array_to_img
from tensorflow.keras.datasets import cifar10, cifar100, mnist, fashion_mnist



def gen_images(dataset, image_dir, image_list, max_images, image_format):
  
  # make the calibration images folder if it doesn't exist
  if not os.path.isdir(image_dir):
    os.makedirs(image_dir)

  # Fetch the Keras dataset
  if (dataset=='fashion_mnist'):
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    is_color=False
  elif (dataset=='cifar100'):
    (x_train, y_train), (x_test, y_test) = cifar100.load_data()
    is_color=True
  elif (dataset=='cifar10'):
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    is_color=True
  else:
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    is_color=False

  # create file for list of calibration images
  f = open(os.path.join(image_dir, image_list), 'w')


  # Convert numpy arrays of training dataset into image files.
  # If you prefer to convert the test dataset, then change x_train to x_test:
  for i in range(len(x_train[:max_images])):

    img_file=os.path.join(image_dir,'image_'+str(i)+'.'+image_format)

    if (is_color):
      img = cv2.cvtColor(x_train[i], cv2.COLOR_BGR2RGB)
    else:
      img = x_train[i]

    cv2.imwrite(img_file, img)
    
    # write image file name to image list (not including path)
    #f.write('image_'+str(i)+'.'+image_format+'\n')

    # write full path of image file to image list
    f.write(img_file+'\n')

  f.close()
  print ('FINISHED GENERATING IMAGES')

  return


# only used if script is run as 'main' from command line
def main():
  # construct the argument parser and parse the arguments
  ap = argparse.ArgumentParser()
  
  ap.add_argument('-d', '--dataset',
                  type=str,
                  default='mnist',
                  choices=['cifar10','cifar100','mnist','fashion_mnist'],
                  help='Dataset - valid choices are cifar10, cifar100, mnist, fashion_mnist. Default is mnist')  
  ap.add_argument('-dir', '--image_dir',
                  type=str,
                  default='./image_dir',
                  help='Path to folder for saving images and images list file. Default is ./image_dir')  
  ap.add_argument('-l', '--image_list',
                  type=str,
                  default='./image_list.txt',
                  help='Name of images list file. Default is ./image_list.txt')  
  ap.add_argument('-f', '--image_format',
                  type=str,
                  default='png',
                  choices=['png','jpg','bmp'],
                  help='Image file format - valid choices are png, jpg, bmp. Default is png')  
  ap.add_argument('-m', '--max_images',
                  type=int,
                  default=1000,
                  help='Number of images to generate. Default is 1000')
  
  args = ap.parse_args()  
  
  print ('Command line options:')
  print (' --dataset      : ', args.dataset)
  print (' --image_dir    : ', args.image_dir)
  print (' --image_list   : ', args.image_list)
  print (' --image_format : ', args.image_format)
  print (' --max_images   : ', args.max_images)


  gen_images(args.dataset, args.image_dir, args.image_list, args.max_images, args.image_format)


if __name__ == '__main__':
  main()

