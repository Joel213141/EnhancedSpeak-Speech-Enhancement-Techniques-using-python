{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7112acc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import librosa.display\n",
    "\n",
    "def plot_spectrogram(signal, sample_rate, title='Spectrogram'):\n",
    "    plt.figure(figsize=(15, 5))\n",
    "    D = librosa.amplitude_to_db(np.abs(librosa.stft(signal)), ref=np.max)\n",
    "    librosa.display.specshow(D, sr=sample_rate, x_axis='time', y_axis='log')\n",
    "    plt.colorbar(format='%+2.0f dB')\n",
    "    plt.title(title)\n",
    "    plt.show()\n"
   ]
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
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
