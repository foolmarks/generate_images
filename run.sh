# example of script usage

conda activate decent_q31

rm -rf cifar10_jpg
rm -rf cifar10_png
rm -rf cifar10_bmp

rm -rf cifar100_jpg
rm -rf cifar100_png
rm -rf cifar100_bmp

rm -rf mnist_jpg
rm -rf mnist_png
rm -rf mnist_bmp

rm -rf fashion_mnist_jpg
rm -rf fashion_mnist_png
rm -rf fashion_mnist_bmp



python generate_images.py  \
    --dataset=cifar10 \
    --image_dir=./cifar10_jpg \
    --image_format=jpg \
    --max_images=5

python generate_images.py  \
    --dataset=cifar10 \
    --image_dir=./cifar10_png \
    --image_format=png \
    --max_images=5

python generate_images.py  \
    --dataset=cifar10 \
    --image_dir=./cifar10_bmp \
    --image_format=bmp \
    --max_images=5

################################

python generate_images.py  \
    --dataset=cifar100 \
    --image_dir=./cifar100_jpg \
    --image_format=jpg \
    --max_images=5

python generate_images.py  \
    --dataset=cifar100 \
    --image_dir=./cifar100_png \
    --image_format=png \
    --max_images=5

python generate_images.py  \
    --dataset=cifar100 \
    --image_dir=./cifar100_bmp \
    --image_format=bmp \
    --max_images=5

###############################

python generate_images.py  \
    --dataset=mnist \
    --image_dir=./mnist_jpg \
    --image_format=jpg \
    --max_images=5

python generate_images.py  \
    --dataset=mnist \
    --image_dir=./mnist_png \
    --image_format=png \
    --max_images=5

python generate_images.py  \
    --dataset=mnist \
    --image_dir=./mnist_bmp \
    --image_format=bmp \
    --max_images=5


###############################

python generate_images.py  \
    --dataset=fashion_mnist \
    --image_dir=./fashion_mnist_jpg \
    --image_format=jpg \
    --max_images=5

python generate_images.py  \
    --dataset=fashion_mnist \
    --image_dir=./fashion_mnist_png \
    --image_format=png \
    --max_images=5

python generate_images.py  \
    --dataset=fashion_mnist \
    --image_dir=./fashion_mnist_bmp \
    --image_format=bmp \
    --max_images=5



