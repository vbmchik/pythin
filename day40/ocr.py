import keras_ocr
import matplotlib.pyplot as plt
ocr_keras = keras_ocr.pipeline.Pipeline()
ocr_img_keras = [ keras_ocr.tools.read(img_ocr) for img_ocr in ['1.jpg','2.jpg',]]
ocr_pred = ocr_keras.recognize (ocr_img_keras)
fig, axs = plt.subplots(nrows=len(ocr_img_keras), figsize=(10, 20))
for ax, image, predictions in zip(axs, ocr_img_keras, ocr_pred):
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)		
    ocr_img = ocr_pred[1]
for text, box in ocr_img:
    print(text)