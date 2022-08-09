import numpy as np

def kl(e0, e1):
    var0, var1 = get_variance(e0), get_variance(e1)
    kl0 = 0.5 * (var0 / var1 - 1 + np.log(var1) - np.log(var0))
    kl1 = 0.5 * (var1 / var0 - 1 + np.log(var0) - np.log(var1))
    return np.maximum(kl0, kl1).sum()

def asymmetric_kl(e0, e1):
    var0, var1 = get_variance(e0), get_variance(e1)
    kl0 = 0.5 * (var0 / var1 - 1 + np.log(var1) - np.log(var0))
    kl1 = 0.5 * (var1 / var0 - 1 + np.log(var0) - np.log(var1))
    return kl0.sum()

def jsd(e0, e1):
    var0, var1 = get_variance(e0), get_variance(e1)
    var = 0.5 * (var0 + var1)
    kl0 = 0.5 * (var0 / var - 1 + np.log(var) - np.log(var0))
    kl1 = 0.5 * (var1 / var - 1 + np.log(var) - np.log(var1))
    return (0.5 * (kl0 + kl1)).mean()

def cosine(e0, e1):
    h1, h2 = get_scaled_hessian(e0, e1)
    return distance.cosine(h1, h2)

def normalized_cosine(e0, e1):
    h1, h2 = get_variances(e0, e1, normalized=True)
    return distance.cosine(h1, h2)

def correlation(e0, e1):
    v1, v2 = get_variances(e0, e1, normalized=False)
    return distance.correlation(v1, v2)

def entropy(e0, e1):
    h1, h2 = get_scaled_hessian(e0, e1)
    return np.log(2) - binary_entropy(h1).mean()
