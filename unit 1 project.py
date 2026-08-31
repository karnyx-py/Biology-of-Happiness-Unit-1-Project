
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

    # food protein box
    ax.add_patch(patches.FancyBboxPatch((0.5, 3.5), 2.2, 1.5, boxstyle="round,pad=0.1", fc="#FFD1DC", ec="#D32F2F", lw=2))
    ax.text(1.6, 4.2, "Food Protein", ha="center", va="center", fontsize=12, fontweight="bold", color="#D32F2F")
    ax.annotate("", xy=(1.6, 3.5), xytext=(0.5, 0.5), color="#D32F2F", lw=2, arrowstyle='->')
