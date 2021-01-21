import requests
import json
import cv2
import csv
             
url = 'https://api.chooch.ai/predict/image?apikey=8b534527-eb6b-4293-b653-de6eee231882'

input_image = "in.jpeg"
files = {'image': open(input_image, 'rb')}

response = requests.post(url, files=files)
                              
#print(response.content)

json_data = json.loads(response.text)

print(json_data)

#print(json_data["objects"]["predictions"]) 


with open('object_detection.csv', 'w') as f:
	writer = csv.writer(f)                          
	csv_line = "object, x1, x2, y1, y2"
	writer.writerows([csv_line.split(',')])


with open('text_detection.csv', 'w') as f:
	writer = csv.writer(f)                          
	csv_line = "text, x1, x2, y1, y2"
	writer.writerows([csv_line.split(',')])

'''detection_data = {}
counter = 0
for i in json_data["objects"]["predictions"]:
	if i["object_title"] in detection_data:
		detection_data[i["object_title"] +"_" + str(counter)] = i["coordinates"]
		counter = counter + 1
	else:
		detection_data[i["object_title"]] = i["coordinates"]
		print(i["coordinates"])

print("===")
print(detection_data)'''


'''
detection_data = {}
counter = 0
for i in json_data["predictions"]:
	try:
		if i["class_title"] in detection_data and i["coordinates"] != None:
			detection_data[i["class_title"] +"_" + str(counter)] = i["coordinates"]
			counter = counter + 1
		else:
			if i["coordinates"] != None:
				detection_data[i["class_title"]] = i["coordinates"]
			print(i["coordinates"])
	except:
		print("ok")
print("===")
print(detection_data)'''

'''
detection_data = {}
counter = 0
for i in json_data["texts"]["predictions"]:
	try:
		if i["text_value"] in detection_data and i["coordinates"] != None:
			detection_data[i["text_value"] +"_" + str(counter)] = i["coordinates"]
			counter = counter + 1
		else:
			if i["coordinates"] != None:
				detection_data[i["text_value"]] = i["coordinates"]
			print(i["coordinates"])
	except:
		print("ok")
print("===")
print(detection_data)'''


img = cv2.imread(input_image)
detection_data = {}
counter = 0
font = cv2.FONT_HERSHEY_SIMPLEX
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

		with open('object_detection.csv', 'a') as f:
			writer = csv.writer(f)                          
			csv_line = str(i["object_title"]) + "," + x1 + "," + x2 + "," + y1 + "," + y2
			writer.writerows([csv_line.split(',')])

	else:
		detection_data[i["object_title"]] = i["coordinates"]
		x1 = str(i["coordinates"]).split(",")[0]
		x2 = str(i["coordinates"]).split(",")[1]
		y1 = str(i["coordinates"]).split(",")[2]
		y2 = str(i["coordinates"]).split(",")[3]
		cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
		cv2.putText(img, i["object_title"], (int(x1),int(y1)-10), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

		with open('object_detection.csv', 'a') as f:
			writer = csv.writer(f)                          
			csv_line = str(i["object_title"]) + "," + x1 + "," + x2 + "," + y1 + "," + y2
			writer.writerows([csv_line.split(',')])


print("===")
#print(detection_data)

'''detection_data = {}
counter = 0
for i in json_data["predictions"]:
	try:
		if i["class_title"] in detection_data and i["coordinates"] != None:
			detection_data[i["class_title"] +"_" + str(counter)] = i["coordinates"]
			x1 = str(i["coordinates"]).split(",")[0]
			x2 = str(i["coordinates"]).split(",")[1]
			y1 = str(i["coordinates"]).split(",")[2]
			y2 = str(i["coordinates"]).split(",")[3]
			cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255,0,0), 2)
			cv2.putText(img, i["class_title"], (int(x1),int(y1)-10), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
			counter = counter + 1
		else:
			if i["coordinates"] != None:
				detection_data[i["class_title"]] = i["coordinates"]
				x1 = str(i["coordinates"]).split(",")[0]
				x2 = str(i["coordinates"]).split(",")[1]
				y1 = str(i["coordinates"]).split(",")[2]
				y2 = str(i["coordinates"]).split(",")[3]
				cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255,0,0), 2)
				cv2.putText(img, i["class_title"], (int(x1),int(y1)-10), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
			#print(i["coordinates"])
	except:
		print("ok")
print("===")'''
#print(detection_data)


detection_data = {}
counter = 0
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

			with open('text_detection.csv', 'a') as f:
				writer = csv.writer(f)                          
				csv_line = str(i["text_value"]) + "," + x1 + "," + x2 + "," + y1 + "," + y2
				writer.writerows([csv_line.split(',')])

		else:
			if i["coordinates"] != None:
				detection_data[i["text_value"]] = i["coordinates"]
				x1 = str(i["coordinates"]).split(",")[0]
				x2 = str(i["coordinates"]).split(",")[1]
				y1 = str(i["coordinates"]).split(",")[2]
				y2 = str(i["coordinates"]).split(",")[3]
				cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 2)
				cv2.putText(img, i["text_value"], (int(x1),int(y1)-10), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

				with open('text_detection.csv', 'a') as f:
					writer = csv.writer(f)                          
					csv_line = str(i["text_value"]) + "," + x1 + "," + x2 + "," + y1 + "," + y2
					writer.writerows([csv_line.split(',')])
			#print(i["coordinates"])
	except:
		print("ok")
print("===")
#print(detection_data)













detection_data = {}
counter = 0
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
print("===")
print(detection_data)
cv2.putText(img, str(detection_data), (20,35), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
cv2.imwrite(input_image.split('.')[0]+"_output.png",img)
