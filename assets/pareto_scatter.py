#!/usr/bin/env python3
"""Figure 1 redesign: quantitative Pareto scatter (SyntaxGym vs parses scored at
inference). Data from Table 2 (tab:results_delta-dup1). Single-column ACL size."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- palette (validated) ----
BLUE   = "#4059AD"   # Type A: joint syntactic LMs, beam marginalization
ORANGE = "#B45F06"   # ours (paper tagcolor)
CYAN   = "#0891B2"   # Type C: parser-free at inference
GRAY   = "#6B7280"   # baseline, semantic neutral
INK    = "#1F2937"
MUTED  = "#6B7280"
SURF   = "#FFFFFF"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 8,
    "axes.edgecolor": "#9CA3AF",
    "axes.linewidth": 0.7,
    "text.color": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
})

# x positions: categorical-log (0, 1, break, 300)
X0, X1, X300 = 0.0, 1.0, 2.45

pts = [
    # (x, SG, label, color, dx, dy, ha)
    (X0,   73.09, "Transformer-XL\n(no syntactic supervision)", GRAY, 0.09, 0.0, "left"),
    (X0,   77.10, "TPT",                          CYAN,  0.09,  0.0,  "left"),
    (X0,   80.00, "TreeReg",                      CYAN,  0.09, -0.55, "left"),
    (X300, 80.20, "PLM",                          BLUE, -0.09, -0.3,  "right"),
    (X300 - 0.13, 82.30, "Pushdown\nLM",          BLUE,  0.0,  -0.95, "center"),
    (X300 + 0.05, 82.50, "TG",                    BLUE,  0.0,   0.75, "center"),
]

fig, ax = plt.subplots(figsize=(3.25, 2.8), dpi=300)
fig.patch.set_facecolor(SURF)
ax.set_facecolor(SURF)

# recessive horizontal grid
ax.grid(axis="y", color="#E5E7EB", linewidth=0.6, zorder=0)
ax.set_axisbelow(True)

# Pareto frontier: TreeReg -> SiPE -> TG (dashed, under points)
fx = [X0, X1, X300 + 0.05]
fy = [80.00, 80.60, 82.50]
ax.plot(fx, fy, ls=(0, (4, 3)), lw=1.1, color="#9CA3AF", zorder=1)

# points
for x, y, lab, col, dx, dy, ha in pts:
    ax.scatter([x], [y], s=42, color=col, edgecolor="white", linewidth=1.0, zorder=3)
    ax.annotate(lab, xy=(x, y), xytext=(x + dx, y + dy), fontsize=7,
                color=INK, ha=ha, va="center", zorder=4, linespacing=0.95)

# ours: star, bigger, bold label
ax.scatter([X1], [80.60], s=200, marker="*", color=ORANGE,
           edgecolor="white", linewidth=1.0, zorder=5)
ax.annotate("SiPE (ours)", xy=(X1, 80.60), xytext=(X1 + 0.14, 80.15),
            fontsize=8, fontweight="bold", color=ORANGE, ha="left", zorder=5)

# axes
ax.set_xlim(-0.28, 2.72)
ax.set_ylim(71.8, 83.9)
ax.set_xticks([X0, X1, X300])
ax.set_xticklabels(["0", "1", "$\\approx$300"])
ax.set_ylabel("SyntaxGym score", fontsize=8)
ax.set_xlabel("Inference cost (parse trees evaluated per sentence)", fontsize=8)

# group sublabels under the tick labels
for x, txt, col in [(X0, "parser-free", CYAN), (X1, "single parse", ORANGE),
                    (X300, "beam marginalization", BLUE)]:
    ax.annotate(txt, xy=(x, 0), xycoords=("data", "axes fraction"),
                xytext=(0, -21), textcoords="offset points",
                fontsize=6.6, color=col, ha="center", fontweight="bold")
ax.xaxis.labelpad = 22

# axis-break glyph between x=1 and x=300
for bx in (1.72,):
    ax.annotate("//", xy=(bx, 0), xycoords=("data", "axes fraction"),
                xytext=(0, -6.5), textcoords="offset points",
                fontsize=7.5, color="#9CA3AF", ha="center")

for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.tick_params(length=2.5, width=0.7, labelsize=7.5)

fig.tight_layout(pad=0.4)
out = "/mnt/efs/harisriaz/HexaPE_EMNLP_2026/latex/figures/pareto_scatter"
fig.savefig(out + ".pdf")
fig.savefig(out + ".png")
print("saved", out + ".{pdf,png}")
