from keras.models import load_model
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")
model = load_model("trained_model.h5")


@np.vectorize
def predict(time, charge_weight):
    prediction = model.predict(np.array([[time / 4000.0, charge_weight / 3.3]]))[0]
    velocity = prediction[0] * 399.99
    r = prediction[1] * 1431.04435815
    return velocity, r


@np.vectorize
def plot_points(charge_weight):
    time_axis = np.arange(0, 4000, 200)
    v, r = predict(time_axis, charge_weight / 1000)

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(880 / 72, 820 / 72))
    plt.suptitle(f"Velocity and Distance over time with a {charge_weight / 1000} kg charge", y=1.02, fontweight="bold")

    ax1.plot(time_axis, v)
    ax1.set_title("$v(t)$")
    ax1.set_ylim(0, 450)
    ax1.set_ylabel("Velocity (m/s)")

    ax2.plot(time_axis, r)
    ax2.set_title("$r(t)$")
    ax2.set_ylim(0, 1500)
    ax2.set_xlabel("Time (milliseconds)")
    ax2.set_ylabel("Distance (m)")

    plt.tight_layout(pad=1.5)
    plt.savefig(f"frames/{int(charge_weight / 10)}.png", bbox_inches = "tight")

plot_points(np.arange(0, 6000, 10))
