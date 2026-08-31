
# unit 1 project
import matplotlib.patches as patches
import matplotlib.pyplot as plt

# global styling
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'


def create_metabolism_diagram():
  fig, ax = plt.subplots(figsize=(14, 5.5), dpi=300)
  ax.set_xlim(0, 14)
  ax.set_ylim(0, 6)
  ax.axis('off')

  # food box
  ax.add_patch(
      patches.FancyBboxPatch(
          (0.6, 1.8),
          3.0,
          2.4,
          boxstyle='round,pad=0.15',
          fc='#FFD1DC',
          ec='#D32F2F',
          lw=2.5,
      )
  )
  ax.text(
      2.1,
      3.4,
      'Dietary Protein',
      ha='center',
      va='center',
      fontsize=11,
      fontweight='bold',
      color='#B71C1C',
  )
  ax.text(
      2.1,
      2.9,
      '(e.g., Meat, Eggs, Beans)',
      ha='center',
      va='center',
      fontsize=8.5,
      color='#333333',
  )
  ax.text(
      2.1,
      2.3,
      '[Complex Polymer]',
      ha='center',
      va='center',
      fontsize=8,
      style='italic',
      color='#555555',
  )

  # catabolism arrow and labels
  ax.annotate(
      '',
      xy=(5.2, 3.0),
      xytext=(3.8, 3.0),
      arrowprops=dict(
          facecolor='#D32F2F', edgecolor='#D32F2F', width=3, headwidth=9
      ),
  )
  ax.text(
      4.5,
      3.4,
      'Catabolism\n(Digestion)',
      ha='center',
      va='bottom',
      fontweight='bold',
      color='#D32F2F',
      fontsize=9,
  )
  ax.text(
      4.5,
      2.5,
      'Releases Energy\nBreaks Bonds',
      ha='center',
      va='top',
      fontsize=7.5,
      color='#444444',
  )

  # amino acids box
  ax.add_patch(
      patches.FancyBboxPatch(
          (5.4, 1.8),
          3.0,
          2.4,
          boxstyle='round,pad=0.15',
          fc='#FFF9C4',
          ec='#FBC02D',
          lw=2.5,
      )
  )
  ax.text(
      6.9,
      3.3,
      'Free Amino Acids',
      ha='center',
      va='center',
      fontsize=11,
      fontweight='bold',
      color='#F57F17',
  )
  ax.text(
      6.9,
      2.5,
      '[Monomer Building Blocks]',
      ha='center',
      va='center',
      fontsize=8,
      style='italic',
      color='#555555',
  )

  # anabolism arrow and labels
  ax.annotate(
      '',
      xy=(10.0, 3.0),
      xytext=(8.6, 3.0),
      arrowprops=dict(
          facecolor='#388E3C', edgecolor='#388E3C', width=3, headwidth=9
      ),
  )
  ax.text(
      9.3,
      3.4,
      'Anabolism\n(Biosynthesis)',
      ha='center',
      va='bottom',
      fontweight='bold',
      color='#2E7D32',
      fontsize=9,
  )
  ax.text(
      9.3,
      2.5,
      'Requires Energy (ATP)\nForms Peptide Bonds',
      ha='center',
      va='top',
      fontsize=7.5,
      color='#444444',
  )

  # body structure box
  ax.add_patch(
      patches.FancyBboxPatch(
          (10.2, 1.8),
          3.2,
          2.4,
          boxstyle='round,pad=0.15',
          fc='#C8E6C9',
          ec='#388E3C',
          lw=2.5,
      )
  )
  ax.text(
      11.8,
      3.4,
      'Human Body Structures',
      ha='center',
      va='center',
      fontsize=11,
      fontweight='bold',
      color='#1B5E20',
  )
  ax.text(
      11.8,
      2.8,
      'Muscle (Actin / Myosin)\nSkin & Hair (Keratin)',
      ha='center',
      va='center',
      fontsize=8.5,
      color='#333333',
  )
  ax.text(
      11.8,
      2.1,
      '[New Cellular Polymers]',
      ha='center',
      va='center',
      fontsize=8,
      style='italic',
      color='#555555',
  )

  plt.title(
      'Metabolism: How Catabolic and Anabolic Reactions Turn Meals into You',
      fontsize=12,
      fontweight='bold',
      pad=16,
  )
  plt.tight_layout()
  plt.savefig('metabolism_diagram.png', bbox_inches='tight')
  plt.show()


def create_membrane_diagram():
  fig, ax = plt.subplots(figsize=(14, 5.5), dpi=300)
  ax.set_xlim(0, 14)
  ax.set_ylim(0, 6)
  ax.axis('off')

  # membrane bilayer
  ax.add_patch(
      patches.Rectangle(
          (0.5, 2.4),
          13.0,
          1.2,
          fc='#FFF3E0',
          ec='#FF9800',
          lw=2,
          linestyle='--',
      )
  )
  ax.text(
      0.8,
      3.0,
      'Phospholipid Bilayer\n(Hydrophobic Interior)',
      ha='left',
      va='center',
      fontsize=8.5,
      fontweight='bold',
      color='#E65100',
  )

  # region labels
  ax.text(
      7.0,
      5.5,
      'Extracellular Fluid (Outside Cell)',
      ha='center',
      va='center',
      fontsize=11,
      fontweight='bold',
  )
  ax.text(
      7.0,
      0.5,
      'Cytoplasm (Inside Cell)',
      ha='center',
      va='center',
      fontsize=11,
      fontweight='bold',
  )

  # simple diffusion
  ax.annotate(
      '',
      xy=(4.5, 1.2),
      xytext=(4.5, 4.8),
      arrowprops=dict(
          facecolor='#1E88E5', edgecolor='#1E88E5', width=2.5, headwidth=8
      ),
  )
  ax.text(
      4.5,
      5.0,
      'Small Non-Polar Molecules\n(O2, CO2, Lipids)',
      ha='center',
      va='bottom',
      fontweight='bold',
      color='#1565C0',
      fontsize=8.5,
  )
  ax.text(
      4.5,
      1.0,
      'Simple Diffusion\n(Directly crosses bilayer)',
      ha='center',
      va='top',
      fontsize=8,
  )

  # protein channel
  ax.add_patch(
      patches.FancyBboxPatch(
          (8.8, 2.0),
          1.6,
          2.0,
          boxstyle='round,pad=0.1',
          fc='#B0BEC5',
          ec='#37474F',
          lw=2,
      )
  )
  ax.text(
      9.6,
      3.0,
      'Protein\nChannel',
      ha='center',
      va='center',
      color='#263238',
      fontweight='bold',
      fontsize=8.5,
  )

  # facilitated transport
  ax.annotate(
      '',
      xy=(9.6, 1.2),
      xytext=(9.6, 4.8),
      arrowprops=dict(
          facecolor='#D81B60', edgecolor='#D81B60', width=2.5, headwidth=8
      ),
  )
  ax.text(
      9.6,
      5.0,
      'Large / Polar / Ions\n(Glucose, Na+)',
      ha='center',
      va='bottom',
      fontweight='bold',
      color='#AD1457',
      fontsize=8.5,
  )
  ax.text(
      9.6,
      1.0,
      'Facilitated Transport\n(Requires channel)',
      ha='center',
      va='top',
      fontsize=8,
  )

  plt.title(
      'Selective Permeability of the Cell Membrane',
      fontsize=12,
      fontweight='bold',
      pad=16,
  )
  plt.tight_layout()
  plt.savefig('membrane_diagram.png', bbox_inches='tight')
  plt.show()


create_metabolism_diagram()
create_membrane_diagram()