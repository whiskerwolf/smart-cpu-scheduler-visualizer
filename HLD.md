# High-Level Design (HLD)

## 1. System Overview
Smart CPU Scheduler & Visualizer follows a modular architecture:

**User Input → Tkinter GUI → Selected Scheduler → Scheduling Results → Metrics + Gantt Chart**

## 2. High-Level Architecture

```text
+-----------------------------+
|            User             |
| Process & Algorithm Inputs  |
+-------------+---------------+
              |
              v
+-----------------------------+
|       Tkinter GUI           |
|          main.py            |
+-------------+---------------+
              |
              v
+-----------------------------+
|     Scheduling Layer        |
|                             |
| FCFS | SJF | Priority | RR |
+-------------+---------------+
              |
              v
+-----------------------------+
|      Scheduling Results     |
+-------------+---------------+
          /                    v             v
+----------------+ +----------------------+
| Metrics Module | | Gantt Chart Module   |
|   metrics.py   | |   gantt_chart.py     |
+-------+--------+ +----------+-----------+
        |                    |
        v                    v
 Average Waiting,       Execution Timeline
 Turnaround, Response       Visualization
```

## 3. Main Components

### 3.1 GUI Layer
`main.py` implements the Tkinter application, process input form, algorithm selection, process table, controls, and results display.

### 3.2 Scheduling Layer
The project uses separate scheduler modules for:
- FCFS
- SJF
- Priority
- Round Robin

The GUI selects the appropriate scheduler based on the user's algorithm choice.

### 3.3 Metrics Layer
`metrics.py` calculates average waiting, turnaround, and response times from scheduling results.

### 3.4 Visualization Layer
`gantt_chart.py` uses Matplotlib to visualize process execution as a Gantt chart.

## 4. Data Flow
1. User enters process information.
2. GUI validates and stores process data.
3. User selects a scheduling algorithm.
4. The corresponding scheduler is executed.
5. Scheduling results are returned.
6. Average performance metrics are calculated.
7. The GUI displays the metrics.
8. Gantt chart data is passed to the visualization module.
9. Matplotlib displays the execution timeline.

## 5. Technology Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| GUI | Tkinter |
| Visualization | Matplotlib |
| Scheduling Logic | Python modules |
| Performance Analysis | Python |

## 6. Key Design Characteristics
- Modular scheduling algorithms.
- Separation of GUI, metrics, and visualization responsibilities.
- Interactive process input.
- Validation before simulation.
- Visual representation of scheduling execution.

## 7. Non-Functional Requirements
- Clear and responsive desktop GUI.
- Maintainable modular source structure.
- Validated user input.
- Reproducible scheduling simulations.
- Readable performance results.
