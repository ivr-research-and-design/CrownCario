# Data Info

Good Overview to data format: https://docs.neurosity.co/docs/api/brainwaves

### Neurosity Crown's Format Options: raw, rawUnfiltered, psd, powerByBand
The simplest format option is the raw format. When the headset is running, the EEG receptors will output 16 samples every fraction of a second (62.5 ms) for each receptor. These 16 samples are called Epochs. For simplicity, we should simplify the data prior to storing it because we do not need to store that precise of data.

11_4_2022_Davis-Baseline.txt is a file storing 30 second Baseline data (user stays calm and undistracted).