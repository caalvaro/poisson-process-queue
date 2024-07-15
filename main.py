from poisson_process_queue import PoissonProcessQueue

arrival_rates = [0.5, 0.8, 0.9, 0.99]  # lambda
number_of_queues = 100  # n
max_time = 10_000  # t

fixed_service_time_options = [False, True]
service_time_mean = 1
service_rate = 1.0 / service_time_mean

VERBOSE = False  # se quiser imprimir detalhes da simulação para cada cliente


if __name__ == "__main__":
    for fixed_service_time in fixed_service_time_options:
        for arrival_rate in arrival_rates:
            time_in_system_partial_sum = 0
            customers_served = 0

            for queue_id in range(number_of_queues):
                # cria a fila com o tempo de chegada baseado no processo de poisson e gera os cliente com tempo de serviço distribuidos exponencialmente
                queue = PoissonProcessQueue(
                    queue_id,
                    arrival_rate,
                    max_time,
                    service_rate,
                    fixed_service_time,
                    VERBOSE,
                )

                elapsed_time = 0

                # atualiza o tempo de saída de cada cliente
                for customer in queue.customers:
                    customer.serve(elapsed_time, VERBOSE)
                    elapsed_time = customer.departure_time  # atualiza o tempo

                    if customer.departure_time <= max_time:
                        # contabiliza se o cliente foi servido a tempo
                        time_in_system_partial_sum += (
                            customer.get_time_spent_in_system()
                        )
                        customers_served += 1

            avg_time_spent = time_in_system_partial_sum / customers_served

            print(
                f"Lambda: {arrival_rate}\n"
                f"{'Fixed service time.' if fixed_service_time else 'Exponentially distributed service time.'}\n"
                f"-> Average amount of time spent in the system per customer who completed service: {round(avg_time_spent, 2)} s.\n"
                f"-> Customers served: {round(customers_served, 2)}\n"
                f"-> Total time elapsed: {round(elapsed_time, 2)} s.\n"
            )
