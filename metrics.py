def calculate_average_metrics(results):
    n = len(results)

    avg_waiting = sum(p["waiting"] for p in results) / n
    avg_turnaround = sum(p["turnaround"] for p in results) / n
    avg_response = sum(p["response"] for p in results) / n

    return {
        "Average Waiting Time": round(avg_waiting, 2),
        "Average Turnaround Time": round(avg_turnaround, 2),
        "Average Response Time": round(avg_response, 2)
    }
