import numpy as np
from scipy.stats import gaussian_kde
from scipy.integrate import simpson
import matplotlib.pyplot as plt
import pandas as pd
import os


def createProbabilityDistributionPlot(df: pd.DataFrame) -> None:
    """
    Create a probability distribution plot for each column in the DataFrame.
    Each column should contain numerical data representing grades.

    Args:
        - df (pd.DataFrame): DataFrame containing grades for different subjects.

    Returns:
        - None.
    """
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    imagesDirectory = os.path.join(currentDirectory, "images")
    os.makedirs(imagesDirectory, exist_ok=True)

    x = np.linspace(0, 10, 1000)
    plt.figure(figsize=(16, 9))

    for col in df.columns:
        data = df[col].dropna().values

        # Compute KDE
        kde = gaussian_kde(data)

        pdf = kde(x)

        # Zero outside [0, 10]
        pdf[(x < 0) | (x > 10)] = 0

        # Renormalize so the integral over [0, 10] equals 1
        area = simpson(pdf, x)
        pdf /= area

        plt.plot(x, pdf, label=col)

    plt.ylim(bottom=0)
    plt.xlim(0, 10)
    plt.legend()
    plt.xlabel("Nota")
    plt.ylabel("Densidad de probabilidad")
    plt.savefig(os.path.join(imagesDirectory, "distributions.png"), dpi=300)
    plt.close()
