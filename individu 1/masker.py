{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f7ee8037-c930-4cd6-bc82-a29ae17b19f2",
   "metadata": {},
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
   "id": "b5e56545-5184-4183-8160-0569633a8d9b",
   "metadata": {},
   "outputs": [],
   "source": [
    "given_image = face_recognition.load_image_file('masker.jpeg')\n",
    "#given_image = face_recognition.load_image_file('kelas ML.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7c66a233-926d-4d32-842b-29767e586850",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We found 0 face(s) in this image.\n"
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
   "id": "31d03d0b-6a57-4ff8-86b7-6354ca043ae4",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image = PIL.Image.fromarray(given_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f0ace652-fb26-4546-9f5f-f8a0ae7017da",
   "metadata": {},
   "outputs": [],
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
   "id": "db8d2f91-ee31-4993-8db3-2064ee34987f",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "502d1d91-7124-4ff0-9b03-ebdd0a186ddc",
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
