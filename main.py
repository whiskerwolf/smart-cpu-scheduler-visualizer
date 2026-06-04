import tkinter as tk
from tkinter import ttk, messagebox

from algorithms.fcfs import FCFSScheduler
from algorithms.sjf import SJFScheduler
from algorithms.priority import PriorityScheduler
from algorithms.round_robin import RoundRobinScheduler

from metrics import calculate_average_metrics
from gantt_chart import plot_gantt_chart


class CPUSchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart CPU Scheduler")
        self.root.geometry("1000x700")

        self.processes = []

        self.create_widgets()

    def create_widgets(self):

        # ---------------- TITLE ----------------
        title = tk.Label(
            self.root,
            text="Smart CPU Scheduler & Visualizer",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        # ---------------- INPUT FRAME ----------------
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # Process ID
        tk.Label(
            input_frame,
            text="Process ID"
        ).grid(row=0, column=0)

        self.pid_entry = tk.Entry(input_frame)
        self.pid_entry.grid(
            row=1,
            column=0,
            padx=5
        )

        # Arrival Time
        tk.Label(
            input_frame,
            text="Arrival Time"
        ).grid(row=0, column=1)

        self.arrival_entry = tk.Entry(input_frame)
        self.arrival_entry.grid(
            row=1,
            column=1,
            padx=5
        )

        # Burst Time
        tk.Label(
            input_frame,
            text="Burst Time"
        ).grid(row=0, column=2)

        self.burst_entry = tk.Entry(input_frame)
        self.burst_entry.grid(
            row=1,
            column=2,
            padx=5
        )

        # Priority
        tk.Label(
            input_frame,
            text="Priority"
        ).grid(row=0, column=3)

        self.priority_entry = tk.Entry(input_frame)
        self.priority_entry.grid(
            row=1,
            column=3,
            padx=5
        )

        # ---------------- ALGORITHM ----------------
        tk.Label(
            self.root,
            text="Select Algorithm"
        ).pack()

        self.algorithm_var = tk.StringVar()

        self.algorithm_dropdown = ttk.Combobox(
            self.root,
            textvariable=self.algorithm_var,
            values=[
                "FCFS",
                "SJF",
                "Priority",
                "Round Robin"
            ],
            state="readonly",
            width=20
        )

        self.algorithm_dropdown.pack(pady=5)
        self.algorithm_dropdown.current(0)

        self.algorithm_dropdown.bind(
            "<<ComboboxSelected>>",
            self.toggle_quantum
        )

        # ---------------- TIME QUANTUM ----------------
        tk.Label(
            self.root,
            text="Time Quantum (Round Robin Only)"
        ).pack()

        self.quantum_entry = tk.Entry(
            self.root,
            width=15
        )
        self.quantum_entry.pack()

        # Disable initially
        self.quantum_entry.config(
            state="disabled"
        )

        # ---------------- BUTTONS ----------------
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        add_button = tk.Button(
            button_frame,
            text="Add Process",
            command=self.add_process,
            width=15
        )
        add_button.grid(
            row=0,
            column=0,
            padx=5
        )

        run_button = tk.Button(
            button_frame,
            text="Run Simulation",
            command=self.run_simulation,
            width=15
        )
        run_button.grid(
            row=0,
            column=1,
            padx=5
        )

        clear_input_button = tk.Button(
            button_frame,
            text="Clear Inputs",
            command=self.clear_inputs,
            width=15
        )
        clear_input_button.grid(
            row=0,
            column=2,
            padx=5
        )

        clear_all_button = tk.Button(
            button_frame,
            text="Clear All",
            command=self.clear_all,
            width=15
        )
        clear_all_button.grid(
            row=0,
            column=3,
            padx=5
        )

        # ---------------- TABLE ----------------
        columns = (
            "PID",
            "Arrival",
            "Burst",
            "Priority"
        )

        self.process_table = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings",
            height=10
        )

        for col in columns:
            self.process_table.heading(
                col,
                text=col
            )

            self.process_table.column(
                col,
                width=150,
                anchor="center"
            )

        self.process_table.pack(
            pady=10
        )

        # ---------------- METRICS ----------------
        metrics_frame = tk.Frame(self.root)
        metrics_frame.pack(pady=10)

        self.metrics_label = tk.Label(
            metrics_frame,
            text="Simulation Metrics Will Appear Here",
            font=("Arial", 12),
            justify="left"
        )

        self.metrics_label.pack()

    # ---------------- TOGGLE QUANTUM ----------------
    def toggle_quantum(self, event=None):

        algorithm = self.algorithm_var.get()

        if algorithm == "Round Robin":
            self.quantum_entry.config(
                state="normal"
            )
        else:
            self.quantum_entry.delete(
                0,
                tk.END
            )
            self.quantum_entry.config(
                state="disabled"
            )

    # ---------------- ADD PROCESS ----------------
    def add_process(self):

        try:
            pid = self.pid_entry.get().strip()

            if not pid:
                messagebox.showerror(
                    "Error",
                    "Process ID cannot be empty."
                )
                return

            # Duplicate PID check
            for p in self.processes:
                if p["pid"] == pid:
                    messagebox.showerror(
                        "Error",
                        "Duplicate Process ID."
                    )
                    return

            arrival = int(
                self.arrival_entry.get()
            )

            burst = int(
                self.burst_entry.get()
            )

            if arrival < 0 or burst <= 0:
                messagebox.showerror(
                    "Error",
                    "Arrival/Burst time must be valid."
                )
                return

            process = {
                "pid": pid,
                "arrival": arrival,
                "burst": burst
            }

            priority = (
                self.priority_entry.get()
                .strip()
            )

            if priority:

                priority = int(priority)

                if priority < 0:
                    messagebox.showerror(
                        "Error",
                        "Priority cannot be negative."
                    )
                    return

                process["priority"] = priority

            self.processes.append(process)

            self.process_table.insert(
                "",
                tk.END,
                values=(
                    process["pid"],
                    process["arrival"],
                    process["burst"],
                    process.get(
                        "priority",
                        "-"
                    )
                )
            )

            self.clear_inputs()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter valid numbers."
            )

    # ---------------- CLEAR INPUTS ----------------
    def clear_inputs(self):

        self.pid_entry.delete(0, tk.END)
        self.arrival_entry.delete(0, tk.END)
        self.burst_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    # ---------------- CLEAR ALL ----------------
    def clear_all(self):

        self.processes.clear()

        for item in self.process_table.get_children():
            self.process_table.delete(item)

        self.metrics_label.config(
            text="Simulation Metrics Will Appear Here"
        )

    # ---------------- RUN SIMULATION ----------------
    def run_simulation(self):

        if not self.processes:
            messagebox.showwarning(
                "Warning",
                "Please add processes first."
            )
            return

        algorithm = self.algorithm_var.get()

        try:

            # FCFS
            if algorithm == "FCFS":

                scheduler = FCFSScheduler(
                    self.processes
                )

                results = scheduler.run()

                chart_data = results

            # SJF
            elif algorithm == "SJF":

                scheduler = SJFScheduler(
                    self.processes
                )

                results = scheduler.run()

                chart_data = results

            # Priority
            elif algorithm == "Priority":

                for process in self.processes:
                    if "priority" not in process:
                        messagebox.showerror(
                            "Error",
                            "Priority value missing."
                        )
                        return

                scheduler = PriorityScheduler(
                    self.processes
                )

                results = scheduler.run()

                chart_data = results

            # Round Robin
            elif algorithm == "Round Robin":

                if not self.quantum_entry.get():
                    messagebox.showerror(
                        "Error",
                        "Please enter Time Quantum."
                    )
                    return

                quantum = int(
                    self.quantum_entry.get()
                )

                if quantum <= 0:
                    messagebox.showerror(
                        "Error",
                        "Quantum must be greater than 0."
                    )
                    return

                scheduler = RoundRobinScheduler(
                    self.processes,
                    quantum
                )

                results, execution_log = (
                    scheduler.run()
                )

                chart_data = execution_log

            # ---------------- METRICS ----------------
            metrics = calculate_average_metrics(
                results
            )

            result_text = (
                f"Average Waiting Time: "
                f"{metrics['Average Waiting Time']}\n\n"
                f"Average Turnaround Time: "
                f"{metrics['Average Turnaround Time']}\n\n"
                f"Average Response Time: "
                f"{metrics['Average Response Time']}"
            )

            self.metrics_label.config(
                text=result_text
            )

            # Refresh GUI FIRST
            self.root.update()

            # THEN open gantt chart
            plot_gantt_chart(chart_data)

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )


root = tk.Tk()
app = CPUSchedulerGUI(root)
root.mainloop()