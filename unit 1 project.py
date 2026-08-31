
# unit 1 project 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- global styling configuration ---
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

# --- metabolism and protein cycle diagram ---
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
        1.7,
        2.5,
        "[Complex Polymer]",
        ha="center",
        va="center",
        fontsize=8,
        style="italic",
    )

    # catabolism arrow and labels
    ax.annotate(
        "",
        xy=(4.4, 3.0),
        xytext=(3.0, 3.0),
        arrowprops=dict(
            facecolor="D32F2F", edgecolor="D32F2F", width=3, headwith=10
        ),
    )
    ax.text(
        3.7,
        3.4,
      "Catabolism\n(Digestion / Hydrolysis)",
      ha="center",
      va="bottom",
      fontweight="bold",
      color="#D32F2F",
      fontsize=9,
  )
    ax.text(
      3.7,
      2.5,
      "Releases Energy\nBreaks Bonds",
      ha="center",
      va="top",
      fontsize=8,
  )

    # amino acid pool
    ax.add_patch(
        patches.FancyBboxPatch(
            (4.6, 2.2),
            2.4,
            1.6,
            boxstyle="round,pad=0.2",
            fc="#FFF9C4",
            ec = "FBC02D",
            lw = 2,
        )
    )
    ax.text(
        5.8,
        3.2,
        "Free Amino Acids",
        ha="center",
        va="center",
        fontweight="bold",
    )
    ax.text(
        5.8,
        2.5,
        "[Individual Monomers]",
        ha="center",
        va="center",
        fontsize=8,
        style="italic",
    )

    # anabolosim arrow and labels
    ax.annotate(
        "",
        xy=(8.6, 3.0),
        xytext=(7.0, 3.0),
        arrowprops=dict(
            facecolor="#388E3C", edgecolor="#388E3C", width=3, headwidth=10
        ),
    )
    ax.text(
        7.9,
        3.4,
        "Anabolism\n(Protein Synthesis)",
        ha="center",
        va="bottom",
        fontweight="bold",
        color="#388E3C",
        fontsize=9,
    )
    ax.text(
        7.9,
        2.5,
        "Uses Energy (ATP)\nBuilds bonds",
        ha="center",
        va="top",
        fontsize=8,
    )

    # body structure box
    ax.add_patch(
        patches.FancyBboxPatch(
            (8.8, 2.2),
            2.6,
            1.6,
            boxstyle="round,pad=0.2",
            fc="#C8E6C9",
            ec="#388E3C",
            lw=2,   
        )
    )
    ax.text(
        10.1,
        3.2,
        "Human Body Structures",
        ha="center",
        va="center",
        fontweight="bold",
    )
    ax.text(
        10.1,
        2.5,
        "Muscle (Actin/Myosin)\nSkin & Hair (Keratin)",
        ha="center",
        va="center",
        fontsize=8,
    )

    plt.title(
        "Metabolism: How Catabolic and Anabolic Reactions Turn Meals into You",
        fontsize=13,
        fontweight="bold",
        pad=15,
    )
    plt.tight_layout()
    plt.savefig("metabolism_diagram.png")
    plt.show()


# --- PANEL 2: membrane transport ---
def create_membrane_diagram():
    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")

    # membrane bilayer representation
    ax.add_patch(
        patches.Rectangle(
            (0.5, 2.4), 11, 1.2, fc="#FFF3E0", ec="#FF9800", lw=2, linestyle="--"
        )
    )
    ax.text(
        0.8,
        3.0,
        "Phospholipid Bilayer\n(Hydrophobic Interior)",
        ha="left",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#E65100",
    )

    # region labels
    ax.text(
        6.0,
        5.5,
        "Extracellular Fluid (Outside Cell)",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
    )
    ax.text(
        6.0,
        0.5,
        "Cytoplasm (Inside Cell)",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
    )

    # path A: simple diffusion (small non-polar)
    ax.annotate(
        "",
        xy=(3.5, 1.2),
        xytext=(3.5, 4.8),
        arrowprops=dict(
            facecolor="#1E88E5", edgecolor="#1E88E5", width=2, headwidth=8
        ),
    )
    ax.text(
        3.5,
        5.0,
        "Small Non-Polar Molecules\n(O2, CO2, Lipids)",
        ha="center",
        va="bottom",
        fontweight="bold",
        color="#1565C0",
        fontsize=9,
    )
    ax.text(
        3.5,
        1.0,
        "Simple Diffusion\n(Directly crosses bilayer)",
        ha="center",
        va="top",
        fontsize=8,
    )

    # transport protein channel
    ax.add_patch(
        patches.FancyBboxPatch(
            (7.5, 2.0),
            1.4,
            2.0,
            boxstyle="round,pad=0.1",
            fc="#B0BEC5",
            ec="#37474F",
            lw=2,
        )
    )
    ax.text(
        8.2,
        3.0,
        "Protein\nChannel",
        ha="center",
        va="center",
        color="#263238",
        fontweight="bold",
        fontsize=8,
    )

    # path B: facilitated diffusion (large / polar / charged)
    ax.annotate(
        "",
        xy=(8.2, 1.2),
        xytext=(8.2, 4.8),
        arrowprops=dict(
            facecolor="#D81B60", edgecolor="#D81B60", width=2, headwidth=8
        ),
    )
    ax.text(
        8.2,
        5.0,
        "Large / Polar / Charged\n(Glucose, Na+, Amino Acids)",
        ha="center",
        va="bottom",
        fontweight="bold",
        color="#AD1457",
        fontsize=9,
    )
    ax.text(
        8.2,
        1.0,
        "Facilitated Transport\n(Requires transport protein)",
        ha="center",
        va="top",
        fontsize=8,
    )

    plt.title(
        "Selective Permeability of the Cell Membrane",
        fontsize=13,
        fontweight="bold",
        pad=15,
    )
    plt.tight_layout()
    plt.savefig("membrane_diagram.png")
    plt.show()


if __name__ == "__main__":
    create_metabolism_diagram()
    create_membrane_diagram()
