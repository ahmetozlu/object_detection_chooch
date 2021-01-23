import requests
import json
import cv2
import csv

# change apikey with yours
url = 'https://api.chooch.ai/predict/image?apikey=8b534527-eb6b-4293-b653-de6eee231882'


input_image = "input7.png"
input_image_directory = "./input/" + input_image

files = {'image': open(input_image_directory, 'rb')}

response = requests.post(url, files=files)
                              
print(response.content)

json_data = json.loads(response.text)

# initialize csv files
with open('object_detection.csv', 'w') as f:
	writer = csv.writer(f)                          
	csv_line = "object, x1, x2, y1, y2"
	writer.writerows([csv_line.split(',')])

with open('text_detection.csv', 'w') as f:
	writer = csv.writer(f)                          
	csv_line = "text, x1, x2, y1, y2"
	writer.writerows([csv_line.split(',')])

# write data to csv function
def write_csv (data1, data2, data3, data4, data5, detection_category):

	if (detection_category == "object_detection"):
		with open('object_detection.csv', 'a') as f:
			writer = csv.writer(f)                          
			csv_line = data1 + "," + data2 + "," + data3 + "," + data4 + "," + data5
			writer.writerows([csv_line.split(',')])

	if (detection_category == "text_detection"):
		with open('text_detection.csv', 'a') as f:
			writer = csv.writer(f)                          
			csv_line = data1 + "," + data2 + "," + data3 + "," + data4 + "," + data5
			writer.writerows([csv_line.split(',')])

# crop the detected objects and texts
def crop_custom(img, x1, y1, x2, y2): # crop custom
	return img[y1:y2, x1:x2]

# font to draw text on output image
font = cv2.FONT_HERSHEY_SIMPLEX

src_img = cv2.imread(input_image_directory)
img = cv2.imread(input_image_directory)
detection_data = {}
counter = 0

# parse the detected object names and pixel locations
for i in json_data["objects"]["predictions"]:
	if i["object_title"] in detection_data:
		detection_data[i["object_title"] +"_" + str(counter)] = i["coordinates"]
		x1 = str(i["coordinates"]).split(",")[0]
		x2 = str(i["coordinates"]).split(",")[1]
		y1 = str(i["coordinates"]).split(",")[2]
		y2 = str(i["coordinates"]).split(",")[3]
		cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
		cv2.putText(img, i["object_title"], (int(x1),int(y1)-10), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
		counter = counter + 1

		write_csv (str(i["object_title"]), x1, x2, y1, y2, "object_detection")

		cropped_image = crop_custom(src_img, int(x1), int(y1), int(x2), int(y2))
		cv2.imwrite("./detected_objects/" + input_image.split('.')[0] + "_" + str(i["object_title"]) + ".png", cropped_image)

	else:
		detection_data[i["object_title"]] = i["coordinates"]
		x1 = str(i["coordinates"]).split(",")[0]
		x2 = str(i["coordinates"]).split(",")[1]
		y1 = str(i["coordinates"]).split(",")[2]
		y2 = str(i["coordinates"]).split(",")[3]
		cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
		cv2.putText(img, i["object_title"], (int(x1),int(y1)-10), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

		write_csv (str(i["object_title"]), x1, x2, y1, y2, "object_detection")

		cropped_image = crop_custom(src_img, int(x1), int(y1), int(x2), int(y2))
		cv2.imwrite("./detected_objects/" + input_image.split('.')[0] + "_" + str(i["object_title"]) + ".png", cropped_image)

# reset the dictionary and the counter
detection_data = {}
counter = 0

# parse the detected texts and pixel locations
for i in json_data["texts"]["predictions"]:
	try:
		if i["text_value"] in detection_data and i["coordinates"] != None:
			detection_data[i["text_value"] +"_" + str(counter)] = i["coordinates"]
			x1 = str(i["coordinates"]).split(",")[0]
			x2 = str(i["coordinates"]).split(",")[1]
			y1 = str(i["coordinates"]).split(",")[2]
			y2 = str(i["coordinates"]).split(",")[3]
			cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 2)
			cv2.putText(img, i["text_value"], (int(x1),int(y1)-10), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
			counter = counter + 1

			write_csv (str(i["text_value"]), x1, x2, y1, y2, "text_detection")

			cropped_image = crop_custom(src_img, int(x1), int(y1), int(x2), int(y2))
			cv2.imwrite("./detected_texts/" + input_image.split('.')[0] + "_" + str(i["text_value"]) + ".png", cropped_image)

		else:
			if i["coordinates"] != None:
				detection_data[i["text_value"]] = i["coordinates"]
				x1 = str(i["coordinates"]).split(",")[0]
				x2 = str(i["coordinates"]).split(",")[1]
				y1 = str(i["coordinates"]).split(",")[2]
				y2 = str(i["coordinates"]).split(",")[3]
				cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 2)
				cv2.putText(img, i["text_value"], (int(x1),int(y1)-10), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

				write_csv (str(i["text_value"]), x1, x2, y1, y2, "text_detection")
			
				cropped_image = crop_custom(src_img, int(x1), int(y1), int(x2), int(y2))
				cv2.imwrite("./detected_texts/" + input_image.split('.')[0] + "_" + str(i["text_value"]) + ".png", cropped_image)

	except:
		print("ok")

# reset the dictionary and the counter
detection_data = {}
counter = 0

# parse the detected objects and total counts of them
for i in json_data["objects"]["summary"]:
	try:
		if i["object_title"] in detection_data and i["count"] != None:
			detection_data[i["object_title"] +"_" + str(counter)] = i["count"]
			counter = counter + 1
		else:
			if i["count"] != None:
				detection_data[i["object_title"]] = i["count"]
			print(i["count"])
	except:
		print("ok")

# draw texts on output image and save it as a new image
cv2.putText(img, str(detection_data), (20,35), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.imwrite("./output/" + input_image.split('.')[0]+"_output.png",img)

print("All the processes are done. The output image was save.")
