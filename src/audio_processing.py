{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9467588d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import librosa\n",
    "from pydub import AudioSegment\n",
    "from scipy.signal import butter, sosfilt\n",
    "\n",
    "def load_audio(audio_path):\n",
    "    audio = AudioSegment.from_wav(audio_path)\n",
    "    samples = np.array(audio.get_array_of_samples())\n",
    "    frame_rate = audio.frame_rate\n",
    "    return samples, frame_rate\n",
    "\n",
    "def apply_filter(signal, frame_rate, cutoff_freq, filter_type='lowpass', order=10):\n",
    "    nyq = 0.5 * frame_rate\n",
    "    normal_cutoff = cutoff_freq / nyq if isinstance(cutoff_freq, int) else [f / nyq for f in cutoff_freq]\n",
    "    sos = butter(order, normal_cutoff, btype=filter_type, analog=False, output='sos')\n",
    "    filtered_signal = sosfilt(sos, signal)\n",
    "    return filtered_signal\n",
    "\n",
    "def spectral_subtraction(noisy_audio_path, noise_audio_path, frame_rate):\n",
    "    noisy_s, _ = load_audio(noisy_audio_path)\n",
    "    noise_s, _ = load_audio(noise_audio_path)\n",
    "    # Implementation of spectral subtraction would go here\n",
    "    # Placeholder for actual spectral subtraction logic\n",
    "    return noisy_s  # Returning original for placeholder\n"
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
