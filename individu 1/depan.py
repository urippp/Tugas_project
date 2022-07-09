{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fd69a827-ba19-4a90-8dc9-b866a7ca0fc9",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#https://towardsdatascience.com/face-detection-in-just-5-lines-of-code-5cc6087cb1a9\n",
    "import PIL.Image\n",
    "import PIL.ImageDraw\n",
    "import face_recognition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3fbea099-cca6-4b26-b315-6103fe76f766",
   "metadata": {},
   "outputs": [],
   "source": [
    "given_image = face_recognition.load_image_file('depan.jpeg')\n",
    "#given_image = face_recognition.load_image_file('kelas ML.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e37c2cc2-4d27-4a96-8b56-e716d0c7a4ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We found 1 face(s) in this image.\n"
     ]
    }
   ],
   "source": [
    "face_locations = face_recognition.face_locations(given_image)\n",
    "number_of_faces = len(face_locations)\n",
    "print(\"We found {} face(s) in this image.\".format(number_of_faces))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c84caed0-8614-4ff2-9bbf-6d61682d9878",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image = PIL.Image.fromarray(given_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "760514e5-b4d9-4d38-abe7-09d391435580",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A face is detected at pixel location Top: 726, Left: 911, Bottom: 1281, Right: 356\n"
     ]
    }
   ],
   "source": [
    "for face_location in face_locations:\n",
    "    top, left, bottom, right = face_location\n",
    "    print(\"A face is detected at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}\".format(top, left, bottom, right))\n",
    "    draw = PIL.ImageDraw.Draw(pil_image)\n",
    "    draw.rectangle([left, top, right, bottom], outline=\"red\", width=10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6ddb02e2-9a49-46ac-992c-f90901d2e931",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd4db332-ff24-45c9-827b-33b05d252df2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96f74859-891a-46a8-bc8d-fbfe60f8ce6f",
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
