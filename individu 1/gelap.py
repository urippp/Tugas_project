{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b5458eda-208c-4bd3-8027-277ee92ac8ab",
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
   "id": "abc6993c-75a1-42f9-bbf3-692546d6c5ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "given_image = face_recognition.load_image_file('gelap.jpeg')\n",
    "#given_image = face_recognition.load_image_file('kelas ML.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "093b3d4f-1058-45a9-be12-58d794539175",
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
   "id": "0d72dc26-3243-420f-9b2a-476a36a90cc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image = PIL.Image.fromarray(given_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2c348575-03a2-436f-8810-3dbd0c24d048",
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
   "id": "bff79586-4b8e-4509-a6fe-b0a24e9ac5fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c77cf85-92ed-4eb8-a328-3588f29ec8ae",
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
