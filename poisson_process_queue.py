from random import random
from math import log
from customer import Customer


class PoissonProcessQueue:
    def __init__(
        self,
        id: int,
        arrival_rate: float,
        max_time: float,
        service_rate: float,
        fixed_service_time: bool,
        verbose=True,
    ) -> None:
        elapsed_time = 0
        poisson_process = []

        # gera o tempo de chegada de cada cliente
        while elapsed_time < max_time:
            poisson_process.append(elapsed_time)

            interarrival_time = self.generate_exponencial(arrival_rate)
            elapsed_time += interarrival_time

        self.id = id
        self.arrivals = poisson_process

        self.customers = []

        # para cada cliente, gera o tempo de serviço
        for id, arrival_time in enumerate(self.arrivals):
            if not fixed_service_time:
                service_time = self.generate_exponencial(service_rate)
            else:
                service_time = 1.0

            new_customer = Customer(id, arrival_time, service_time)

            self.customers.append(new_customer)

        if verbose:
            print(self)
            self.print_customers()

    def generate_exponencial(self, rate: float) -> float:
        u = random()
        return -log(1 - u) / rate

    def print_customers(self):
        print()
        for customer in self.customers:
            print(customer)
        print()

    def __str__(self) -> str:
        print(
            f"Poisson process {self.id}:\n",
            list(round(t, 2) for t in self.arrivals),
            "\n",
        )
