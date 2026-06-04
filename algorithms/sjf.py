class SJFScheduler:
    def __init__(self, processes):
        self.processes = processes

    def run(self):
        processes = self.processes.copy()

        current_time = 0
        completed = []
        ready_queue = []

        while processes or ready_queue:

            # Add arrived processes
            for process in processes[:]:
                if process["arrival"] <= current_time:
                    ready_queue.append(process)
                    processes.remove(process)

            # If CPU idle
            if not ready_queue:
                current_time += 1
                continue

            # Pick shortest burst process
            ready_queue.sort(key=lambda x: x["burst"])
            process = ready_queue.pop(0)

            pid = process["pid"]
            arrival = process["arrival"]
            burst = process["burst"]

            start_time = current_time
            completion_time = start_time + burst

            turnaround_time = completion_time - arrival
            waiting_time = turnaround_time - burst
            response_time = start_time - arrival

            completed.append({
                "pid": pid,
                "arrival": arrival,
                "burst": burst,
                "start": start_time,
                "completion": completion_time,
                "turnaround": turnaround_time,
                "waiting": waiting_time,
                "response": response_time
            })

            current_time = completion_time

        return completed