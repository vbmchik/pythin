import keras_ocr
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# [ x**2 for x in [1, 2, 3] ]
images = [
    keras_ocr.tools.read(img) for img in [ "1.jpg", "2.jpg", "card1.png", ]
]
pipeline = keras_ocr.pipeline.Pipeline()
prediction_groups = pipeline.recognize(images)
#fig, axs = plt.subplots(nrows=len(images), figsize=(10, 20))
#for ax, image, predictions in zip(axs, images, prediction_groups):
#    keras_ocr.tools.drawAnnotations(image=image,
#                                    predictions=predictions,
#                                    ax=ax)
predicted_image = prediction_groups[0]
for result in prediction_groups:
    for text, box in result:
        print(text)
