{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7143b0d3-3b16-4a0d-80bd-d683146eec21",
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
   "execution_count": 7,
   "id": "d01e520f-668e-4906-a40e-ef1d1159411c",
   "metadata": {},
   "outputs": [],
   "source": [
    "given_image = face_recognition.load_image_file('blur.jpeg')\n",
    "#given_image = face_recognition.load_image_file('kelas ML.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b4319a6a-5659-47e5-b7d3-e4682a93e049",
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
   "execution_count": 9,
   "id": "c8f990ce-00d9-4d0e-91a4-c059c84bb5c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image = PIL.Image.fromarray(given_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "69c8969a-0f04-455e-ad9c-32574764a119",
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
   "execution_count": 11,
   "id": "589a207b-5975-4739-8762-1e97be2faa52",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61ecb06b-adc1-4633-89cc-fd3831fb0ec0",
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
