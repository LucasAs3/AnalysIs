import matplotlib.pyplot as plt
import os


def create_metrics_chart(analysis: dict) -> str:
    labels = [
    "Document Quality",
    "Confidence",
    "Risk"
    ]

    values = [
        analysis["document_quality"],
        analysis["confidence_score"],
        analysis["risk"]
    ]

    os.makedirs("output", exist_ok=True)

    plt.figure(figsize=(8,3.5), dpi=250)

    bars = plt.barh(
    labels,
    values,
    color="#4F46E5",
    height=0.5
)  

    for bar in bars:
        width = bar.get_width()

        plt.text(
            width + 1,
            bar.get_y() + bar.get_height()/2,
            f"{int(width)}",
            fontsize=11,
            fontweight="bold",
            va="center"
        )

    plt.gca().invert_yaxis()
    ax = plt.gca()
    ax.spines["top"].set_visible(False)

    ax.spines["right"].set_visible(False)

    ax.spines["left"].set_visible(False)

    ax.spines["bottom"].set_visible(False)

    plt.xlim(0,110)

    plt.title("AI Analysis Metrics",
    fontsize=18,
    fontweight="bold")

    plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)

    

    output = "output/dashboard_metrics.png"
    plt.tight_layout()
    plt.savefig(output)

    plt.close()

    return output
