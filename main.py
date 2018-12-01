import multiprocessing
import time
import cv2
import sys


def comparePixels(i):
	same = 0
	for j in range(width):
		if (imageA[i,j] == imageB[i,j]).all():
			same += 1
	time.sleep(0.1)
	return same


total_num_cores = multiprocessing.cpu_count()
num_cores = eval(input("Enter number of cores: "))
filenameA = input("Enter Image1 filename: ")
filenameB = input("Enter Image2 filename: ")

if num_cores > total_num_cores:
	num_cores = total_num_cores
	print("Number of cores is equal with your total number of cores " + str(total_num_cores))

imageA = cv2.imread(filenameA)
imageB = cv2.imread(filenameB)

if imageA is None or imageB is None:
	print("Please enter images that exist!")
	sys.exit(1)

if imageA.shape[0] != imageB.shape[0] or imageA.shape[1] != imageB.shape[1]:
	print("These images has different size!")
	sys.exit(1)

height,width,rgb = imageA.shape
total = height * width

pool = multiprocessing.Pool(processes=num_cores)
start = time.time()
results = pool.map(comparePixels, range(height))
end = time.time()

print("Result: " + str(sum(results)/total * 100) + " %")
print("Time: " + str(end - start))