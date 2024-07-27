{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cae9ccfc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from audio_processing import load_audio, apply_filter, spectral_subtraction\n",
    "from utils import plot_spectrogram\n",
    "\n",
    "def main():\n",
    "    # Load noisy audio\n",
    "    noisy_audio_path = 'NoisySignal/Station/sp01_station_sn5.wav'\n",
    "    noisy_s, noisy_f = load_audio(noisy_audio_path)\n",
    "\n",
    "    # Apply low-pass filter\n",
    "    filtered_s_low = apply_filter(noisy_s, noisy_f, cutoff_freq=1000, filter_type='lowpass')\n",
    "    plot_spectrogram(filtered_s_low, noisy_f, title='Low-Pass Filtered Spectrogram')\n",
    "\n",
    "    # Apply high-pass filter\n",
    "    filtered_s_high = apply_filter(noisy_s, noisy_f, cutoff_freq=200, filter_type='highpass')\n",
    "    plot_spectrogram(filtered_s_high, noisy_f, title='High-Pass Filtered Spectrogram')\n",
    "\n",
    "    # Apply band-pass filter\n",
    "    filtered_s_band = apply_filter(noisy_s, noisy_f, cutoff_freq=[200, 1000], filter_type='bandpass')\n",
    "    plot_spectrogram(filtered_s_band, noisy_f, title='Band-Pass Filtered Spectrogram')\n",
    "\n",
    "    # Perform spectral subtraction\n",
    "    noise_audio_path = 'Noise/Station/Station_1.wav'\n",
    "    enhanced_s = spectral_subtraction(noisy_audio_path, noisy_audio_path, noisy_f)\n",
    "    plot_spectrogram(enhanced_s, noisy_f, title='Spectrally Subtracted Spectrogram')\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
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
