
# unit 1 project 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- global styling configuration ---
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

def create_metabolism_diagram():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    ax.set_xlim(0,10)
    ax.set_ylim(0,6)
    ax.axis('off')

    # food box
    ax.add_patch(
        patches.FancyBboxPatch(
            (0.6, 2.2),
            2.2,
            1.6,
            boxstyle="round,pad=0.2",
            fc="#FFD1DC",
            ec = "D32F2F",
            lw = 2,
        )
    )
    ax.text(
        1.7,
        3.2,
        "Dietary Protein\n(e.g., meat, eggs, beans)",
        ha="center",
        va="center",
        fontweight="bold",
    )
    ax.text(
        
    )