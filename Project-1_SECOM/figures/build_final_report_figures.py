"""Reproduce the two figures used in documents/Final_Report.md."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent


def build_model_comparison() -> None:
    feature_counts = np.array([20, 30, 40, 70, 100])
    average_precision = np.array([0.1717, 0.1723, 0.1780, 0.1785, 0.2000])
    ap_std = np.array([0.0648, 0.0567, 0.0642, 0.0548, 0.0627])

    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.errorbar(
        feature_counts,
        average_precision,
        yerr=ap_std,
        fmt="o-",
        color="#1f5a85",
        ecolor="#8ca9bd",
        capsize=5,
        linewidth=2.2,
        markersize=7,
        label="Random Forest + ANOVA",
    )
    ax.axhline(
        0.1539,
        color="#c05a47",
        linestyle="--",
        linewidth=1.8,
        label="All-feature logistic reference (AP = 0.154)",
    )
    ax.axhline(
        0.0662,
        color="#777777",
        linestyle=":",
        linewidth=1.6,
        label="Failure prevalence (0.066)",
    )
    ax.set(
        title="Repeated-CV ranking performance by retained feature count",
        xlabel="ANOVA-selected features",
        ylabel="Average precision",
        xticks=feature_counts,
        ylim=(0, 0.30),
    )
    ax.grid(axis="y", alpha=0.22)
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "final_model_comparison.png", dpi=180)
    plt.close(fig)


def build_feature_stability() -> None:
    features = [
        "103", "59", "510", "129", "348", "64", "431", "21", "100", "125",
        "430", "316", "434", "436", "435", "351", "213", "95", "28", "114",
    ]
    frequencies = np.array(
        [
            [1.00, 1.00, 1.00, 1.00, 1.00],
            [1.00, 1.00, 1.00, 1.00, 1.00],
            [1.00, 1.00, 1.00, 1.00, 1.00],
            [1.00, 1.00, 1.00, 1.00, 0.92],
            [1.00, 1.00, 0.88, 0.84, 0.80],
            [1.00, 0.96, 0.96, 0.88, 0.72],
            [1.00, 0.84, 0.84, 0.80, 0.72],
            [1.00, 0.96, 0.80, 0.72, 0.68],
            [1.00, 1.00, 0.84, 0.80, 0.64],
            [1.00, 1.00, 0.92, 0.88, 0.60],
            [0.84, 0.80, 0.76, 0.72, 0.60],
            [1.00, 1.00, 0.88, 0.84, 0.56],
            [0.88, 0.80, 0.72, 0.68, 0.56],
            [0.84, 0.80, 0.68, 0.56, 0.52],
            [0.84, 0.80, 0.72, 0.64, 0.52],
            [0.80, 0.80, 0.76, 0.60, 0.48],
            [0.80, 0.80, 0.64, 0.52, 0.44],
            [1.00, 0.92, 0.56, 0.48, 0.44],
            [1.00, 0.96, 0.88, 0.76, 0.40],
            [0.88, 0.64, 0.64, 0.56, 0.40],
        ]
    )

    fig, ax = plt.subplots(figsize=(8.8, 9.2))
    image = ax.imshow(frequencies, cmap="Blues", vmin=0, vmax=1, aspect="auto")
    ax.set_xticks(range(5), ["Top 100", "Top 70", "Top 40", "Top 30", "Top 20"])
    ax.set_yticks(range(len(features)), features)
    ax.set_xlabel("Selection threshold")
    ax.set_ylabel("Anonymous feature ID")
    ax.set_title("Feature-selection frequency across 25 resamples")

    for row in range(frequencies.shape[0]):
        for column in range(frequencies.shape[1]):
            value = frequencies[row, column]
            ax.text(
                column,
                row,
                f"{value:.0%}",
                ha="center",
                va="center",
                fontsize=8,
                color="white" if value >= 0.72 else "#18384f",
            )

    colorbar = fig.colorbar(image, ax=ax, fraction=0.035, pad=0.03)
    colorbar.set_label("Selection frequency")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "final_feature_stability.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    build_model_comparison()
    build_feature_stability()
