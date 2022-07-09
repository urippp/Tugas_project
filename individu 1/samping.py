{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e69ef313-269b-4d07-8eb4-abbd2e9b211f",
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
   "id": "faa1d727-37b3-45b2-8cc3-68421119077a",
   "metadata": {},
   "outputs": [],
   "source": [
    "given_image = face_recognition.load_image_file('samping.jpeg')\n",
    "#given_image = face_recognition.load_image_file('kelas ML.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "91f83299-084e-4385-9a24-868a79c6baa1",
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
   "id": "eada025d-292f-4e10-933e-00d79f05c4bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image = PIL.Image.fromarray(given_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "df864094-f428-47ad-92d2-728ccd63ee44",
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
   "id": "35241950-9ade-4bff-a1d4-f444084a5601",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58039efb-6266-485b-b6fd-c11b8da3eb8b",
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
