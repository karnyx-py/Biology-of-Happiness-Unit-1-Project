# unit 1 project
import matplotlib.patches as patches
import matplotlib.pyplot as plt

# global styling
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'


def create_combined_diagrams():
  fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 9), dpi=100)

  # --- panel 1: metabolism ---
  ax1.set_xlim(0, 11)
  ax1.set_ylim(0, 4.5)
  ax1.axis('off')
  title1 = ax1.set_title(
      'Metabolism: How Reactions Turn Meals into You',
      fontweight='bold',
      pad=10,
  )

  # food box
  ax1.add_patch(
      patches.FancyBboxPatch(
          (0.6, 1.1),
          2.5,
          2.2,
          boxstyle='round,pad=0.1',
          fc='#FFD1DC',
          ec='#D32F2F',
          lw=1.8,
      )
  )
  m_t1 = ax1.text(
      1.85,
      2.5,
      'Dietary Protein',
      ha='center',
      va='center',
      fontweight='bold',
      color='#B71C1C',
  )
  m_t2 = ax1.text(
      1.85,
      2.0,
      '(e.g., Meat, Beans)',
      ha='center',
      va='center',
      color='#333333',
  )
  m_t3 = ax1.text(
      1.85,
      1.5,
      '[Complex Polymer]',
      ha='center',
      va='center',
      style='italic',
      color='#555555',
  )

  # catabolism arrow and text
  ax1.annotate(
      '',
      xy=(4.2, 2.2),
      xytext=(3.2, 2.2),
      arrowprops=dict(
          facecolor='#D32F2F', edgecolor='#D32F2F', width=2, headwidth=6
      ),
  )
  m_t4 = ax1.text(
      3.7,
      2.55,
      'Catabolism\n(Digestion)',
      ha='center',
      va='bottom',
      fontweight='bold',
      color='#D32F2F',
  )
  m_t5 = ax1.text(
      3.7,
      1.85,
      'Releases Energy\nBreaks Bonds',
      ha='center',
      va='top',
      color='#444444',
  )

  # amino acids box
  ax1.add_patch(
      patches.FancyBboxPatch(
          (4.3, 1.1),
          2.5,
          2.2,
          boxstyle='round,pad=0.1',
          fc='#FFF9C4',
          ec='#FBC02D',
          lw=1.8,
      )
  )
  m_t6 = ax1.text(
      5.55,
      2.4,
      'Free Amino Acids',
      ha='center',
      va='center',
      fontweight='bold',
      color='#F57F17',
  )
  m_t7 = ax1.text(
      5.55,
      1.8,
      '[Monomer Blocks]',
      ha='center',
      va='center',
      style='italic',
      color='#555555',
  )

  # anabolism arrow and text
  ax1.annotate(
      '',
      xy=(7.9, 2.2),
      xytext=(6.9, 2.2),
      arrowprops=dict(
          facecolor='#388E3C', edgecolor='#388E3C', width=2, headwidth=6
      ),
  )
  m_t8 = ax1.text(
      7.4,
      2.55,
      'Anabolism\n(Biosynthesis)',
      ha='center',
      va='bottom',
      fontweight='bold',
      color='#2E7D32',
  )
  m_t9 = ax1.text(
      7.4,
      1.85,
      'Uses ATP Energy\nBuilds Bonds',
      ha='center',
      va='top',
      color='#444444',
  )

  # human body structures box
  ax1.add_patch(
      patches.FancyBboxPatch(
          (8.0, 1.1),
          2.5,
          2.2,
          boxstyle='round,pad=0.1',
          fc='#C8E6C9',
          ec='#388E3C',
          lw=1.8,
      )
  )
  m_t10 = ax1.text(
      9.25,
      2.5,
      'Body Structures',
      ha='center',
      va='center',
      fontweight='bold',
      color='#1B5E20',
  )
  m_t11 = ax1.text(
      9.25,
      2.0,
      'Muscle, Skin & Hair',
      ha='center',
      va='center',
      color='#333333',
  )
  m_t12 = ax1.text(
      9.25,
      1.5,
      '[Human Polymers]',
      ha='center',
      va='center',
      style='italic',
      color='#555555',
  )

  # --- panel 2: membrane transport ---
  ax2.set_xlim(0, 11)
  ax2.set_ylim(0, 4.5)
  ax2.axis('off')
  title2 = ax2.set_title(
      'Selective Permeability of the Cell Membrane', fontweight='bold', pad=10
  )

  # membrane bilayer representation
  ax2.add_patch(
      patches.Rectangle(
          (0.5, 1.75),
          10.0,
          1.0,
          fc='#FFF3E0',
          ec='#FF9800',
          lw=1.8,
          linestyle='--',
      )
  )
  c_t1 = ax2.text(
      0.7,
      2.25,
      'Phospholipid Bilayer\n(Hydrophobic Core)',
      ha='left',
      va='center',
      fontweight='bold',
      color='#E65100',
  )

  # region labels
  c_t2 = ax2.text(
      5.5,
      4.1,
      'Extracellular Fluid (Outside Cell)',
      ha='center',
      va='center',
      fontweight='bold',
  )
  c_t3 = ax2.text(
      5.5,
      0.4,
      'Cytoplasm (Inside Cell)',
      ha='center',
      va='center',
      fontweight='bold',
  )

  # simple diffusion
  ax2.annotate(
      '',
      xy=(3.6, 0.9),
      xytext=(3.6, 3.6),
      arrowprops=dict(
          facecolor='#1E88E5', edgecolor='#1E88E5', width=2, headwidth=6
      ),
  )
  c_t4 = ax2.text(
      3.6,
      3.7,
      'Small Non-Polar\n(O2, CO2, Lipids)',
      ha='center',
      va='bottom',
      fontweight='bold',
      color='#1565C0',
  )
  c_t5 = ax2.text(
      3.6,
      0.7,
      'Simple Diffusion\n(Direct Crossing)',
      ha='center',
      va='top',
      color='#444444',
  )

  # protein channel
  ax2.add_patch(
      patches.FancyBboxPatch(
          (7.0, 1.45),
          1.3,
          1.6,
          boxstyle='round,pad=0.08',
          fc='#B0BEC5',
          ec='#37474F',
          lw=1.8,
      )
  )
  c_t6 = ax2.text(
      7.65,
      2.25,
      'Protein\nChannel',
      ha='center',
      va='center',
      color='#263238',
      fontweight='bold',
  )

  # facilitated transport
  ax2.annotate(
      '',
      xy=(7.65, 0.9),
      xytext=(7.65, 3.6),
      arrowprops=dict(
          facecolor='#D81B60', edgecolor='#D81B60', width=2, headwidth=6
      ),
  )
  c_t7 = ax2.text(
      7.65,
      3.7,
      'Large / Polar / Ions\n(Glucose, Na+)',
      ha='center',
      va='bottom',
      fontweight='bold',
      color='#AD1457',
  )
  c_t8 = ax2.text(
      7.65,
      0.7,
      'Facilitated Transport\n(Requires Channel)',
      ha='center',
      va='top',
      color='#444444',
  )

  # element groups for adaptive scaling
  titles = [title1, title2]
  headers = [m_t1, m_t6, m_t10, c_t2, c_t3]
  subs = [
      m_t2,
      m_t3,
      m_t4,
      m_t5,
      m_t7,
      m_t8,
      m_t9,
      m_t11,
      m_t12,
      c_t1,
      c_t4,
      c_t5,
      c_t6,
      c_t7,
      c_t8,
  ]

  # dynamic resize handler
  def on_resize(event):
    scale = fig.get_size_inches()[0] / 11.0
    for t in titles:
      t.set_fontsize(max(8.0, 11.0 * scale))
    for h in headers:
      h.set_fontsize(max(6.5, 9.5 * scale))
    for s in subs:
      s.set_fontsize(max(5.5, 7.5 * scale))
    fig.canvas.draw_idle()

  # connect resize listener
  fig.canvas.mpl_connect('resize_event', on_resize)
  on_resize(None)

  # layout padding and save files
  plt.tight_layout(pad=2.0)
  plt.savefig('biology_unit1_diagrams.png', dpi=300, bbox_inches='tight')
  plt.savefig('biology_unit1_diagrams.pdf', bbox_inches='tight')
  plt.show()


create_combined_diagrams()