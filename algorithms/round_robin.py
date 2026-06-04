from collections import deque


class RoundRobinScheduler:
    def __init__(self, processes, time_quantum):
        self.processes = sorted(processes, key=lambda x: x["arrival"])
        self.time_quantum = time_quantum

    def run(self):
        processes = self.processes.copy()

        current_time = 0
        completed = []
        ready_queue = deque()

        execution_log = []

        # Remaining burst time
        remaining_time = {
            p["pid"]: p["burst"]
            for p in processes
        }

        first_response = {}

        while processes or ready_queue:

            # Add arrived processes
            while processes and processes[0]["arrival"] <= current_time:
                ready_queue.append(processes.pop(0))

            # CPU idle case
            if not ready_queue:
                current_time += 1
                continue

            process = ready_queue.popleft()

            pid = process["pid"]
            arrival = process["arrival"]

            # First response tracking
            if pid not in first_response:
                first_response[pid] = current_time

            execution_time = min(
                self.time_quantum,
                remaining_time[pid]
            )

            start_time = current_time
            current_time += execution_time
            remaining_time[pid] -= execution_time

            execution_log.append({
                "pid": pid,
                "start": start_time,
                "burst": execution_time
            })

            # Add newly arrived processes
            while processes and processes[0]["arrival"] <= current_time:
                ready_queue.append(processes.pop(0))

            # Process completed
            if remaining_time[pid] == 0:

                completion_time = current_time
                original_burst = process["burst"]

                turnaround_time = (
                    completion_time - arrival
                )

                waiting_time = (
                    turnaround_time
                    - original_burst
                )

                response_time = (
                    first_response[pid]
                    - arrival
                )

                completed.append({
                    "pid": pid,
                    "arrival": arrival,
                    "burst": original_burst,
                    "completion": completion_time,
                    "turnaround": turnaround_time,
                    "waiting": waiting_time,
                    "response": response_time
                })

            else:
                ready_queue.append(process)

        return completed, execution_log