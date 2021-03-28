from flask import Flask, make_response, render_template
from io import BytesIO

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from keras.datasets import mnist, cifar10
import numpy as np

#(x_train, y_train), (x_test, y_test) = mnist.load_data()


app = Flask(__name__)


@app.route("/plot/<int:idx>")

def plot_graph(idx):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    fig = plt.figure(figsize=(3, 3))


    #img=x_train[idx]
    img=x_train[0]
    plt.subplot(1, 1, 1)
    plt.imshow(img)

    plt.show()


    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)

    img_data = png_output.getvalue()

    response = make_response(img_data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(img_data)
    return response


if __name__ == "__main__":
    #app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
    app.run(host="0.0.0.0", port=5000, threaded=True)

