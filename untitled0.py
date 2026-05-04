import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

def padding(img, pad_size):
    h, w, c = img.shape
    padded_img = np.zeros((h + 2 * pad_size, w + 2 * pad_size, c), dtype=img.dtype)
    padded_img[pad_size:h + pad_size, pad_size:w + pad_size] = img
    return padded_img

def median_filter(img, kernel_size=3):
    pad = kernel_size // 2
    h, w, c = img.shape
    padded = padding(img, pad)
    result = np.zeros_like(img)
    
    for i in range(h):
        for j in range(w):
            for k in range(c):
                region = padded[i:i+kernel_size, j:j+kernel_size, k]
                result[i, j, k] = np.median(region)
    return result

def histogram_equalization(img):
    result = np.zeros_like(img)
    for k in range(img.shape[2]):
        channel = img[:, :, k]
        hist, bins = np.histogram(channel.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_m = np.ma.masked_equal(cdf, 0)
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        cdf = np.ma.filled(cdf_m, 0).astype('uint8')
        result[:, :, k] = cdf[channel]
    return result

def sharpening_laplacian(img, strength=0.5):
    kernel = np.array([[0, -1, 0], 
                       [-1, 5, -1], 
                       [0, -1, 0]])
    pad = 1
    h, w, c = img.shape
    padded = padding(img, pad)
    result = np.zeros_like(img, dtype=np.float32)
    
    for i in range(h):
        for j in range(w):
            for k in range(c):
                region = padded[i:i+3, j:j+3, k]
                val = np.sum(region * kernel)
                result[i, j, k] = val
                
    return np.clip(result, 0, 255).astype(np.uint8)

def main():
    base_dir = 'C:/Users/salma/mini-project'
    input_path = os.path.join(base_dir, 'input/lena_noisy.png')
    output_dir = os.path.join(base_dir, 'output')
    output_path = os.path.join(output_dir, 'lena_restored.png')

    img = cv2.imread(input_path)
    if img is None:
        print("Citra tidak ditemukan")
        return

    denoised = median_filter(img, kernel_size=3)
    equalized = histogram_equalization(denoised)
    restored = sharpening_laplacian(equalized)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)       
    cv2.imwrite(output_path, restored)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title("Input Rusak")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Hasil Restorasi")
    plt.imshow(cv2.cvtColor(restored, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()