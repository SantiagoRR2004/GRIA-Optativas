import numpy as np
from scipy.stats import gaussian_kde, norm
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
    plt.savefig(
        os.path.join(imagesDirectory, "distributions.png"), dpi=300, bbox_inches="tight"
    )
    plt.close()


def createNormalDistributionPlot(df: pd.DataFrame) -> None:
    """
    Create a normal distribution plot based on the averages and standard deviations.

    Args:
        - df (pd.DataFrame): DataFrame containing grades for different subjects.

    Returns:
        - None.
    """
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    imagesDirectory = os.path.join(currentDirectory, "images")
    os.makedirs(imagesDirectory, exist_ok=True)

    x = np.linspace(-100, 100, 10000)
    leftBound = x[-1]
    rightBound = x[0]
    plt.figure(figsize=(16, 9))

    for subject in df.columns:
        mean = df[subject].mean()
        stdDev = df[subject].std()

        y = norm.pdf(x, loc=mean, scale=stdDev)

        # Add a mask
        mask = y >= 0.001

        plt.plot(x[mask], y[mask], label=subject)

        # Calculate the right and left bounds
        leftBound = min(leftBound, x[mask][0])
        rightBound = max(rightBound, x[mask][-1])

    plt.ylim(bottom=0)
    plt.xlim(leftBound, rightBound)
    plt.legend()
    plt.xlabel("Nota")
    plt.ylabel("Densidad de probabilidad")
    plt.savefig(
        os.path.join(imagesDirectory, "normalDistributions.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()
