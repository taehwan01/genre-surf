import sys
import librosa


def getAudioFile(filename):
    return librosa.load(filename)


def getFeatures(y, sr):
    audioFeatures = dict()

    # Extract chromagram
    chroma = librosa.feature.chroma_stft(y = y, sr = sr)
    audioFeatures['chroma_stft_mean'] = chroma.mean()
    audioFeatures['chroma_stft_var'] = chroma.var()

    # Extract RMS
    rms = librosa.feature.rms(y = y)
    audioFeatures['rms_mean'] = rms.mean()
    audioFeatures['rms_var'] = rms.var()

    # Extract spectral centroid
    spec_cent = librosa.feature.spectral_centroid(y = y, sr = sr)
    audioFeatures['spectral_centroid_mean'] = spec_cent.mean()
    audioFeatures['spectral_centroid_var'] = spec_cent.var()

    # Extract spectral bandwidth
    spec_bw = librosa.feature.spectral_bandwidth(y = y, sr = sr)
    audioFeatures['spectral_bandwidth_mean'] = spec_bw.mean()
    audioFeatures['spectral_bandwidth_var'] = spec_bw.var()

    # Extract spectral rolloff
    spec_rolloff = librosa.feature.spectral_rolloff(y = y, sr = sr)
    audioFeatures['rolloff_mean'] = spec_rolloff.mean()
    audioFeatures['rolloff_var'] = spec_rolloff.var()

    # Extract zero crossing rate
    zeroCrossingRate = librosa.feature.zero_crossing_rate(y)
    audioFeatures['zero_crossing_rate_mean'] = zeroCrossingRate.mean()
    audioFeatures['zero_crossing_rate_var'] = zeroCrossingRate.var()

    # Extract harmonic and percussive features
    harmony, perceptr = librosa.effects.hpss(y, margin = 3.0)
    audioFeatures['harmony_mean'] = harmony.mean()
    audioFeatures['harmony_var'] = harmony.var()
    audioFeatures['perceptr_mean'] = perceptr.mean()
    audioFeatures['perceptr_var'] = perceptr.var()

    # Extract tempo
    tempo,_ = librosa.beat.beat_track(y = y, sr = sr)
    audioFeatures['tempo'] = tempo

    # Extract MFCCs
    mfcc = librosa.feature.mfcc(y = y, sr = sr)
    for i in range(0, len(mfcc)):
        mfcc_mean = 'mfcc' + str(i + 1) + '_mean'
        mfcc_var = 'mfcc' + str(i + 1) + '_var'
        audioFeatures[mfcc_mean] = mfcc[i].mean()
        audioFeatures[mfcc_var] = mfcc[i].var()

    return audioFeatures

def main(inputFile):
    y, sr = getAudioFile(inputFile)
    audioFeatures = getFeatures(y, sr)
    print(audioFeatures, end = '')


if __name__ == '__main__':
    main(sys.argv[1])
    sys.stdout.flush()