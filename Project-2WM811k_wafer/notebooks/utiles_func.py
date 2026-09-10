import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch
import matplotlib.pyplot as plt

def unwrap_failure_type(failure_type):
    if isinstance(failure_type, np.ndarray):
        failure_type = failure_type.tolist()
    if isinstance(failure_type, list):
        if len(failure_type) == 0:
            return None
        value = failure_type[0]
    if isinstance(value, list):
        if len(value) == 0:
            return None
        value = value[0]
    value = value.strip().strip("'").strip('"')
    return value


wafer_colors = ListedColormap([
    "#f2efe8",  # 0: background
    "#6294ba",  # 1: good die
    "#d76741"   # 2: failed die
])

wafer_norm = BoundaryNorm(
    [-0.5, 0.5, 1.5, 2.5],
    wafer_colors.N
)


def plot_example_maps(example_maps, wafer_maps):    
    fig, ax = plt.subplots(2, 2, figsize=(9, 9))

    for ax, (_, row) in zip(ax.flat, example_maps.iterrows()):
        wafer_map = row["waferMap"]
        ax.imshow(
            wafer_map,
            cmap=wafer_colors,
            norm=wafer_norm,
            interpolation="nearest",
            aspect="equal"
        )
        ax.set_title(
            f"Lot: {row['lotName'][3:]} | "
            f"Wafer: {row['waferIndex']} "
        )
        ax.axis("off")

    legend_items = [
        Patch(facecolor="#f2efe8", label="Background"),
        Patch(facecolor="#6f9fc4", label="Good die"),
        Patch(facecolor="#d97757", label="Failed die")
    ]

    ax.legend(
        handles=legend_items,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.03),
        ncol=3,
        frameon=False
    )

    # plt.tight_layout()
    plt.show()
    
def audit_wafer_map(wm):
    """
    Audits an individual wafer map array for shape, emptiness, and unexpected pixel values.
    Expected values:
        0: Background
        1: Good die (Pass)
        2: Failed die (Defect)
    """
    if not isinstance(wm, np.ndarray) or wm.ndim != 2:
        return {
            'is_corrupt_shape': True,
            'is_empty_shape': True,
            'total_pixels': 0,
            'die_count': 0,
            'fail_count': 0,
            'unexpected_values': True,
            'unique_values': ()
        }
    
    h, w = wm.shape
    if h == 0 or w == 0:
        return {
            'is_corrupt_shape': False,
            'is_empty_shape': True,
            'total_pixels': 0,
            'die_count': 0,
            'fail_count': 0,
            'unexpected_values': False,
            'unique_values': ()
        }

    # Extract unique values present in this map
    uniques = np.unique(wm)
    # Check if there are any values outside {0, 1, 2}
    unexpected = not set(uniques).issubset({0, 1, 2})
    
    # Die counts (dies on wafer = good (1) + fail (2))
    good_count = int(np.sum(wm == 1))
    fail_count = int(np.sum(wm == 2))
    die_count = good_count + fail_count

    return {
        'is_corrupt_shape': False,
        'is_empty_shape': False,
        'total_pixels': int(h * w),
        'die_count': die_count,
        'fail_count': fail_count,
        'unexpected_values': unexpected,
        'unique_values': tuple(uniques)
    }
