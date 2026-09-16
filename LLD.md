# Low-Level Design (LLD)

## 1. Project Structure

```text
smart-cpu-scheduler/
├── algorithms/
│   ├── fcfs.py
│   ├── sjf.py
│   ├── priority.py
│   └── round_robin.py
├── gantt_chart.py
├── metrics.py
├── main.py
├── requirements.txt
├── README.md
├── HLD.md
├── LLD.md
└── PRD.md
```

## 2. GUI Module — `main.py`

The main application defines the `CPUSchedulerGUI` class.

The GUI:
- Creates the application window.
- Provides process input fields.
- Provides algorithm selection.
- Handles Round Robin Time Quantum.
- Displays processes in a table.
- Runs simulations.
- Displays calculated metrics.
- Opens the Gantt chart.

The application window is titled **Smart CPU Scheduler**.

## 3. Process Data Model

Processes are represented as Python dictionaries containing:

```python
{
    "pid": process_id,
    "arrival": arrival_time,
    "burst": burst_time
}
```

For Priority Scheduling, a priority value is added:

```python
process["priority"] = priority
```

## 4. Input Validation

The GUI validates:
- Process ID is not empty.
- Process IDs are not duplicated.
- Arrival time is non-negative.
- Burst time is greater than zero.
- Priority cannot be negative.
- Priority Scheduling requires priority values.
- Round Robin requires a valid positive Time Quantum.

Invalid input results in an error message rather than running the simulation.

## 5. Scheduling Modules

The project separates scheduling logic into four modules:

### `algorithms/fcfs.py`
Implements First Come First Serve scheduling.

### `algorithms/sjf.py`
Implements Shortest Job First scheduling.

### `algorithms/priority.py`
Implements Priority Scheduling using assigned priority values.

### `algorithms/round_robin.py`
Implements Round Robin scheduling using a configurable Time Quantum.

The GUI invokes the appropriate scheduler and receives scheduling results.

## 6. Metrics Module — `metrics.py`

The function:

```python
calculate_average_metrics(results)
```

calculates:

```text
Average Waiting Time
Average Turnaround Time
Average Response Time
```

The averages are calculated from the corresponding values in the scheduling results and rounded to two decimal places.

## 7. Gantt Chart Module — `gantt_chart.py`

The function:

```python
plot_gantt_chart(results)
```

creates a Matplotlib horizontal bar chart.

For each execution entry, the chart uses:
- Process ID
- Start time
- Burst duration

The x-axis represents time, and process IDs are displayed inside the execution bars.

## 8. Simulation Control Flow

```text
Start Application
      ↓
Enter Processes
      ↓
Validate Input
      ↓
Select Algorithm
      ↓
Run Simulation
      ↓
Execute Selected Scheduler
      ↓
Receive Results
      ↓
Calculate Average Metrics
      ↓
Update GUI
      ↓
Generate Gantt Chart
```

## 9. Round Robin Flow

For Round Robin:
1. User selects Round Robin.
2. Time Quantum input becomes available.
3. User enters a positive quantum.
4. The Round Robin scheduler executes.
5. Scheduling results and execution log are returned.
6. Metrics are calculated from the scheduling results.
7. The execution log is used for the Gantt chart.

## 10. Execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## 11. Performance Outputs

The application displays:
- Average Waiting Time
- Average Turnaround Time
- Average Response Time

The metrics module computes these values from the scheduler results.

## 12. Future Technical Extensions
- Add more CPU scheduling algorithms.
- Add result export to CSV/PDF.
- Embed the Gantt chart directly inside the Tkinter interface.
- Add Dark Mode UI.
