# 🏞️ Intel Image Classification with CNN

Bu proje, **Convolutional Neural Network (CNN)** kullanarak görüntüleri 6 farklı sınıfa ayıran bir **derin öğrenme uygulamasıdır**. Model, **Intel Image Classification** veri seti ile eğitilmiş ve **Gradio arayüzü** kullanılarak **Hugging Face Spaces** üzerinde erişilebilir hale getirilmiştir.

---

## 📌 Proje Özeti

* 📂 Veri seti: Intel Image Classification Dataset
* 🧠 Model: Convolutional Neural Network (CNN)
* 🖼️ Girdi: Görüntü
* 🎯 Çıktı: Görüntünün ait olduğu sınıf ve olasılık skorları
* 🌐 Arayüz: Gradio
* ☁️ Deploy: Hugging Face Spaces

---

## 🗂️ Sınıflar

Model aşağıdaki **6 sınıf** için tahmin yapmaktadır:

* Buildings
* Forest
* Glacier
* Mountain
* Sea
* Street

---

## 📁 Proje Dosya Yapısı

```text
intel_image_cnn/
├── model.py                # CNN modelinin eğitildiği dosya
├── app.py                  # Gradio arayüzü
├── intel_image_model.h5    # Eğitilmiş model dosyası
├── seg_train/              # Eğitim verileri
├── seg_test/               # Test verileri
└── README.md               # Proje açıklama dosyası
```

---

## ⚙️ Model Eğitimi

Model, TensorFlow kullanılarak eğitilmiştir.

Model eğitimi sonrası `.h5` formatında kaydedilmiştir.

---

## 🧪 Kullanılan Teknolojiler

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib
* Gradio
* Hugging Face Spaces

---

## 🚀 Hugging Face Demo

Uygulama, Gradio arayüzü ile Hugging Face Spaces üzerinde deploy edilmiştir.

🔗 **Canlı Demo:**

https://huggingface.co/spaces/baharkayhan/intel-image-cnn

---

### Model Eğitimi:

```bash
python model.py
```

### Gradio Arayüzü:

```bash
python app.py
```

---

## Açıklama

Bu projede, CNN tabanlı bir görüntü sınıflandırma modeli lokal ortamda eğitilmiş, model çıktıları `.h5` formatında kaydedilmiş ve Gradio arayüzü kullanılarak Hugging Face Spaces üzerinde yayınlanmıştır. Proje, derin öğrenme ve model deploy süreçlerini uçtan uca göstermektedir.

---
