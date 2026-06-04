class FCFSScheduler:
    def __init__(self, processes):
        """
        processes format:
        [
            {"pid": "P1", "arrival": 0, "burst": 5},
            {"pid": "P2", "arrival": 1, "burst": 3}
        ]
        """
        self.processes = sorted(processes, key=lambda x: x["arrival"])

    def run(self):
        current_time = 0
        completed_processes = []

        for process in self.processes:
            pid = process["pid"]
            arrival = process["arrival"]
            burst = process["burst"]

            # CPU idle case
            if current_time < arrival:
                current_time = arrival

            start_time = current_time
            completion_time = start_time + burst
            turnaround_time = completion_time - arrival
            waiting_time = turnaround_time - burst
            response_time = start_time - arrival

            completed_processes.append({
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

        return completed_processes