class Customer:
    def __init__(self, id, arrival_time, service_time) -> None:
        self.id = id
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.departure_time = None

    def serve(self, elapsed_time: float, verbose=True) -> None:
        if self.arrival_time <= elapsed_time:
            # se chegou antes, teve que esperar na fila
            queue_time = elapsed_time - self.arrival_time
            server_idle_time = 0
        else:
            # se chegou depois, o servidor ficou um tempo ocioso
            queue_time = 0
            server_idle_time = abs(elapsed_time - self.arrival_time)

        if verbose:
            print(
                f"Elapsed time: {round(elapsed_time, 2)}\n"
                f"-> Customer {self.id}: arrived at {round(self.arrival_time, 2)} s.\n"
                f"-> Customer {self.id}: waited on the queue {round(queue_time, 2)} s.\n"
                f"-> Customer {self.id}: the server was idle for {round(server_idle_time, 2)} s.\n"
                f"-> Customer {self.id}: served for {round(self.service_time, 2)} s.\n"
            )

        self.departure_time = self.arrival_time + queue_time + self.service_time

    def get_time_spent_in_system(self) -> float:
        if self.departure_time is not None:
            return self.departure_time - self.arrival_time
        else:
            raise Exception("Customer didn't finish their service.")

    def __str__(self) -> str:
        return f"{round(self.arrival_time, 2)} | {round(self.service_time, 2)} | {round(self.departure_time or -1, 2)}"
