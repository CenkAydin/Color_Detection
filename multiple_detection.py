import numpy as np
import cv2

webcam = cv2.VideoCapture(0)

while(1):
	
	_, imageFrame = webcam.read()
	imageFrame = cv2.flip(imageFrame, 1)

	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)


	red_lower = np.array([161, 155, 84], np.uint8)
	red_upper = np.array([179, 255, 255], np.uint8)
	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)


	green_lower = np.array([25, 52, 72], np.uint8)
	green_upper = np.array([102,255,255], np.uint8)
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)


	blue_lower = np.array([110,50,50], np.uint8)
	blue_upper = np.array([130,255,255], np.uint8)
	blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
	

	kernal = np.ones((5, 5), "uint8")
	

	red_mask = cv2.dilate(red_mask, kernal)
	res_red = cv2.bitwise_and(imageFrame, imageFrame,
							mask = red_mask)
	
	green_mask = cv2.dilate(green_mask, kernal)
	res_green = cv2.bitwise_and(imageFrame, imageFrame,
								mask = green_mask)
	

	blue_mask = cv2.dilate(blue_mask, kernal)
	res_blue = cv2.bitwise_and(imageFrame, imageFrame,
							mask = blue_mask)

	
	contours, hierarchy = cv2.findContours(red_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 3000):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(0, 0, 255), 2)
			cisim_yatay = x + (w // 2)
			cisim_dikey = y + (h // 2)
			if y < 10 and x <= 360:
				imageFrame = cv2.putText(imageFrame, f"KIRMIZI-yatay={cisim_yatay} dikey={cisim_dikey}", (x, y + h + 20),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                        (0, 0, 255), 2)
			elif y < 10 and x > 360:
				imageFrame = cv2.putText(imageFrame, f"KIRMIZI-yatay={cisim_yatay} dikey={cisim_dikey}", (350, y + h + 20),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.75, (0, 0, 255), 2)
			elif y > 10 and x <= 360:
				imageFrame = cv2.putText(imageFrame, f"KIRMIZI-yatay={cisim_yatay} dikey={cisim_dikey}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                        (0, 0, 255), 2)
			elif y > 10 and x > 360:
				imageFrame = cv2.putText(imageFrame, f"KIRMIZI-yatay={cisim_yatay} dikey={cisim_dikey}", (350, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                        (0, 0, 255), 2)
			
			#cv2.putText(imageFrame, "Red", (x, y),
			#			cv2.FONT_HERSHEY_SIMPLEX, 1.0,
			#			(0, 0, 255),2)	

	
	contours, hierarchy = cv2.findContours(green_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 3000):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(0, 255, 0), 2)
			cisim_yatay = x + (w // 2)
			cisim_dikey = y + (h // 2)
			if y < 10 and x <= 360:
				imageFrame = cv2.putText(imageFrame, f"YESIL-yatay={cisim_yatay} dikey={cisim_dikey}", (x, y + h + 20),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                        (0, 0, 255), 2)
			elif y < 10 and x > 360:
				imageFrame = cv2.putText(imageFrame, f"YESIL-yatay={cisim_yatay} dikey={cisim_dikey}", (350, y + h + 20),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.75, (0, 0, 255), 2)
			elif y > 10 and x <= 360:
				imageFrame = cv2.putText(imageFrame, f"YESIL-yatay={cisim_yatay} dikey={cisim_dikey}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                        (0, 0, 255), 2)
			elif y > 10 and x > 360:
				imageFrame = cv2.putText(imageFrame, f"YESIL-yatay={cisim_yatay} dikey={cisim_dikey}", (350, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                        (0, 0, 255), 2)
			#cv2.putText(imageFrame, "Green", (x, y),
			#			cv2.FONT_HERSHEY_SIMPLEX,
			#			1.0, (0, 255, 0),2)

	
	contours, hierarchy = cv2.findContours(blue_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 3000):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(255, 0, 0), 2)
			cisim_yatay = x + (w // 2)
			cisim_dikey = y + (h // 2)
			if y < 10 and x <= 360:
				imageFrame = cv2.putText(imageFrame, f"MAVI-yatay={cisim_yatay} dikey={cisim_dikey}", (x, y + h + 20),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                        (0, 0, 255), 2)
			elif y < 10 and x > 360:
				imageFrame = cv2.putText(imageFrame, f"MAVI-yatay={cisim_yatay} dikey={cisim_dikey}", (350, y + h + 20),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.75, (0, 0, 255), 2)
			elif y > 10 and x <= 360:
				imageFrame = cv2.putText(imageFrame, f"MAVI-yatay={cisim_yatay} dikey={cisim_dikey}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                        (0, 0, 255), 2)
			elif y > 10 and x > 360:
				imageFrame = cv2.putText(imageFrame, f"MAVI-yatay={cisim_yatay} dikey={cisim_dikey}", (350, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                        (0, 0, 255), 2)
			#cv2.putText(imageFrame, "Blue", (x, y),
			#			cv2.FONT_HERSHEY_SIMPLEX,
			#			1.0, (255, 0, 0),2)
			
	
	cv2.imshow("COKLU RENK TANIMA UYGULAMASI", imageFrame)
	if cv2.waitKey(1) == ord("q"):
		webcam.release()
		cv2.destroyAllWindows()
		break
