# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 14:18:40 2025
@author: gecw
"""

import numpy as np
import matplotlib.pyplot as plt

def local_regression(x0, X, Y, tau):
    x0 = np.r_[1, x0]  # Add intercept to x0
    X_design = np.c_[np.ones(len(X)), X]  # Add intercept to X

    # Compute weights using Gaussian kernel
    distances = X - x0[1]
    weights = np.exp(- (distances ** 2) / (2 * tau ** 2))
    W = np.diag(weights)

    # Weighted least squares solution
    theta = np.linalg.pinv(X_design.T @ W @ X_design) @ X_design.T @ W @ Y
    return x0 @ theta

def draw_all(taus):
    fig, axs = plt.subplots(1, len(taus), figsize=(18, 4))
    
    for i, tau in enumerate(taus):
        prediction = [local_regression(x0, X, Y, tau) for x0 in domain]
        axs[i].plot(X, Y, 'o', color='black', markersize=2, label='Data')
        axs[i].plot(domain, prediction, color='red', label=f'Tau = {tau}')
        axs[i].set_title(f"Tau = {tau}")
        axs[i].set_xlabel("X")
        axs[i].set_ylabel("Y")
        axs[i].grid(True)

    plt.tight_layout()
    plt.suptitle("Locally Weighted Regression (varying Tau)", fontsize=14, y=1.05)
    plt.show()

# Sample dataset
X = np.linspace(-3, 3, num=1000)
domain = X
Y = np.log(np.abs(X ** 2 - 1) + 0.5)

# Tau values to visualize
taus = [10, 1, 0.1, 0.01, 0.001]

# Draw all subplots
draw_all(taus)
