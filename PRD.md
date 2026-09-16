# Product Requirements Document (PRD)

## 1. Product Name
**Smart CPU Scheduler & Visualizer**

## 2. Product Overview
Smart CPU Scheduler & Visualizer is a Python-based Operating Systems project that simulates CPU scheduling algorithms through an interactive Tkinter GUI. It provides Gantt chart visualization and performance metrics for scheduling simulations.

## 3. Objective
The objective is to provide an interactive way to understand and compare CPU scheduling behavior by entering processes, selecting a scheduling algorithm, running the simulation, and viewing execution and performance results.

## 4. Core Features
1. Interactive GUI using Tkinter.
2. CPU scheduling algorithm simulation.
3. Gantt chart visualization.
4. Performance metric calculation.
5. Input validation and error handling.
6. Process table for entered processes.

## 5. Supported Algorithms
- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Priority Scheduling
- Round Robin (RR) with configurable Time Quantum

## 6. Functional Requirements

### Process Input
The application shall allow the user to enter:
- Process ID
- Arrival Time
- Burst Time
- Priority

The application validates required values and prevents duplicate process IDs.

### Algorithm Selection
The user shall be able to select:
- FCFS
- SJF
- Priority
- Round Robin

Round Robin shall accept a configurable Time Quantum.

### Simulation
The application shall execute the selected scheduling algorithm and generate scheduling results.

### Performance Analysis
The application shall calculate:
- Average Waiting Time
- Average Turnaround Time
- Average Response Time

### Visualization
The application shall display a Gantt chart representing process execution over time.

## 7. Error Handling
The application should handle invalid process input, duplicate process IDs, invalid arrival/burst values, missing priority values for Priority Scheduling, and invalid/missing Round Robin time quantum.

## 8. Technology Requirements
- Python
- Tkinter
- Matplotlib

## 9. Success Criteria
The project is complete when users can enter valid processes, select a scheduling algorithm, run the simulation, view the calculated metrics, and see the corresponding Gantt chart.

## 10. Future Improvements
- Dark Mode UI
- Export results to CSV/PDF
- Additional scheduling algorithms
- Embedded Gantt chart inside the GUI
