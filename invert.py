from glob import glob
from scipy.misc import imread, imsave
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
from skimage.morphology import square, erosion

files = glob('*.jpg')

for i in files:
	image = rgb2gray(imread(i))
	try:
		global_thresh = threshold_otsu(image)
		binary_global = image < global_thresh
		binary_global = erosion(binary_global, square(3))
	except Exception as e:
		binary_global = image
		print e, i
	imsave('bw/'+i[:-4] + '__' + '.jpg', binary_global)
	print i, i[:-4] + '__' + '.jpg'
