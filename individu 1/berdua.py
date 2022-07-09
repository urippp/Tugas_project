{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cae61de7-e67d-4f55-9b40-6950bfd24803",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 2 no of faces in this image\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#importing the required libraries\n",
    "import cv2\n",
    "import face_recognition\n",
    "\n",
    "#loading the image to detect\n",
    "original_image = cv2.imread('dua orang.jpg')\n",
    "\n",
    "#load the sample images and get the 128 face embeddings from them\n",
    "modi_image = face_recognition.load_image_file('11.jpg')\n",
    "modi_face_encodings = face_recognition.face_encodings(modi_image)[0]\n",
    "\n",
    "trump_image = face_recognition.load_image_file('22.jpg')\n",
    "trump_face_encodings = face_recognition.face_encodings(trump_image)[0]\n",
    "\n",
    "#save the encodings and the corresponding labels in seperate arrays in the same order\n",
    "known_face_encodings = [modi_face_encodings, trump_face_encodings]\n",
    "known_face_names = [\"pitri\", \"urip\"]\n",
    "\n",
    "#load the unknown image to recognize faces in it\n",
    "image_to_recognize = face_recognition.load_image_file('dua orang.jpg')\n",
    "\n",
    "#detect all faces in the image\n",
    "#arguments are image,no_of_times_to_upsample, model\n",
    "all_face_locations = face_recognition.face_locations(image_to_recognize,model='hog')\n",
    "#detect face encodings for all the faces detected\n",
    "all_face_encodings = face_recognition.face_encodings(image_to_recognize,all_face_locations)\n",
    "\n",
    "#print the number of faces detected\n",
    "print('There are {} no of faces in this image'.format(len(all_face_locations)))\n",
    "\n",
    "#looping through the face locations and the face embeddings\n",
    "for current_face_location,current_face_encoding in zip(all_face_locations,all_face_encodings):\n",
    "    #splitting the tuple to get the four position values of current face\n",
    "    top_pos,right_pos,bottom_pos,left_pos = current_face_location\n",
    "    \n",
    "    \n",
    "    #find all the matches and get the list of matches\n",
    "    all_matches = face_recognition.compare_faces(known_face_encodings, current_face_encoding)\n",
    "   \n",
    "    #string to hold the label\n",
    "    name_of_person = 'Unknown face'\n",
    "    \n",
    "    #check if the all_matches have at least one item\n",
    "    #if yes, get the index number of face that is located in the first index of all_matches\n",
    "    #get the name corresponding to the index number and save it in name_of_person\n",
    "    if True in all_matches:\n",
    "        first_match_index = all_matches.index(True)\n",
    "        name_of_person = known_face_names[first_match_index]\n",
    "    \n",
    "    #draw rectangle around the face    \n",
    "    cv2.rectangle(original_image,(left_pos,top_pos),(right_pos,bottom_pos),(255,0,0),2)\n",
    "    \n",
    "    #display the name as text in the image\n",
    "    font = cv2.FONT_HERSHEY_DUPLEX\n",
    "    cv2.putText(original_image, name_of_person, (left_pos,bottom_pos), font, 0.5, (255,255,255),1)\n",
    "    \n",
    "    #display the image\n",
    "    cv2.imshow(\"Faces Identified\",original_image)\n",
    "cv2.waitKey(0); cv2.destroyAllWindows(); cv2.waitKey(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43bed2d6-f08d-4000-bb7d-4da5e6b38422",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
