# 🏞️ Intel Image Classification with CNN

Bu proje, **Convolutional Neural Network (CNN)** kullanılarak görüntülerin **6 farklı çevresel sınıfa** ayrılmasını amaçlayan bir derin öğrenme uygulamasıdır. Proje kapsamında modelin eğitilmesi, değerlendirilmesi ve web tabanlı bir arayüz üzerinden sunulması uçtan uca gerçekleştirilmiştir.

Model, **Intel Image Classification** veri seti ile eğitilmiş ve **Gradio** arayüzü kullanılarak **Hugging Face Spaces** üzerinde erişilebilir hale getirilmiştir.

---

## 📌 Proje Konusu ve Seçilme Gerekçesi

Görüntü sınıflandırma problemi; uydu görüntülerinin analizi, çevresel izleme, şehir planlama ve otonom sistemler gibi birçok alanda yaygın olarak kullanılmaktadır. Bu nedenle proje konusu, **gerçek hayat uygulamalarına doğrudan karşılığı olan** bir problem üzerinden seçilmiştir.

Literatürde görüntü sınıflandırma problemleri için en yaygın ve başarılı yaklaşım **Convolutional Neural Network (CNN)** modelleridir. CNN’ler, görüntülerdeki uzamsal özellikleri otomatik olarak öğrenebildiği için geleneksel makine öğrenmesi yöntemlerine kıyasla daha yüksek performans sağlamaktadır.

---

## 📂 Veri Setinin Belirlenmesi

Bu projede **Intel Image Classification Dataset** kullanılmıştır. Veri seti, akademik çalışmalarda sıklıkla tercih edilen, etiketli ve dengeli bir veri setidir.

### Veri Seti Özellikleri:

* Toplam **6 sınıf** içermektedir
* Eğitim ve test verileri ayrı klasörler halinde düzenlenmiştir
* Görüntüler RGB formatındadır

### Sınıflar:

* Buildings
* Forest
* Glacier
* Mountain
* Sea
* Street

Bu yapı sayesinde modelin hem öğrenme süreci hem de genelleme başarısı ölçülebilmiştir.

---

## 🧠 Kullanılan Yöntem ve Algoritma

Projede **Convolutional Neural Network (CNN)** tabanlı bir mimari kullanılmıştır.

### Yöntem Seçim Gerekçesi:

* Geleneksel yöntemler (SVM, KNN vb.) manuel özellik çıkarımı gerektirir
* CNN modelleri, özellikleri otomatik olarak öğrenir
* Literatürde görüntü sınıflandırmada CNN’lerin daha yüksek doğruluk sağladığı gösterilmiştir

Model mimarisi şu katmanlardan oluşmaktadır:

* Convolution Katmanları
* Max Pooling Katmanları
* Flatten Katmanı
* Fully Connected (Dense) Katmanlar

Bu yapı, performans ve hesaplama maliyeti açısından dengeli bir yaklaşım sunmaktadır.

---

## ⚙️ Model Eğitimi ve Değerlendirilmesi

* Görüntüler **150x150** boyutuna yeniden ölçeklendirilmiştir
* Piksel değerleri **normalize edilmiştir (1/255)**
* Kayıp fonksiyonu: **Categorical Cross-Entropy**
* Optimizasyon algoritması: **Adam**

Model, eğitim süreci sonunda `.h5` formatında kaydedilmiştir. Eğitim ve doğrulama doğrulukları izlenerek modelin öğrenme başarısı değerlendirilmiştir.

---

## 🗂️ Proje Dosya Yapısı

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

## 🌐 Web Arayüzü ve Deploy Süreci

Model, **Gradio** kullanılarak web tabanlı bir arayüze dönüştürülmüştür. Bu arayüz sayesinde kullanıcılar herhangi bir kurulum yapmadan görüntü yükleyerek modelin tahminini alabilmektedir.

Uygulama **Hugging Face Spaces** üzerinde deploy edilmiştir.

🔗 **Canlı Demo:**
[https://huggingface.co/spaces/baharkayhan/intel-image-cnn](https://huggingface.co/spaces/baharkayhan/intel-image-cnn)

---

## 🧪 Kullanılan Teknolojiler

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib
* Gradio
* Hugging Face Spaces

---

## ▶️ Çalıştırma Adımları

### Model Eğitimi:

```bash
python model.py
```

### Gradio Arayüzü:

```bash
python app.py
```

---

## 📄 Proje Dokümantasyonu

Bu proje kapsamında tüm kodlar, model dosyası ve açıklamalar GitHub üzerinde düzenli bir şekilde paylaşılmıştır. Proje, derin öğrenme modelinin eğitilmesi ve deploy edilmesi süreçlerini uçtan uca göstermektedir.
