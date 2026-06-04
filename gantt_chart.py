import matplotlib.pyplot as plt


PROCESS_COLORS = {
    "P1": "#4E79A7",
    "P2": "#F28E2B",
    "P3": "#59A14F",
    "P4": "#E15759",
    "P5": "#76B7B2",
    "P6": "#EDC948"
}


def plot_gantt_chart(results):
    fig, ax = plt.subplots(figsize=(12, 3))

    timeline = []

    for process in results:
        start = process["start"]
        burst = process["burst"]
        pid = process["pid"]

        color = PROCESS_COLORS.get(pid, "gray")

        ax.barh(
            y=0,
            width=burst,
            left=start,
            height=0.5,
            color=color
        )

        ax.text(
            start + burst / 2,
            0,
            pid,
            ha='center',
            va='center',
            fontsize=11,
            fontweight='bold'
        )

        timeline.append(start)

    # Add last completion point
    last_end = (
        results[-1]["start"]
        + results[-1]["burst"]
    )

    timeline.append(last_end)

    ax.set_xticks(sorted(set(timeline)))
    ax.set_xlabel("Time")
    ax.set_title("CPU Scheduling Gantt Chart")
    ax.set_yticks([])

    ax.grid(axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()