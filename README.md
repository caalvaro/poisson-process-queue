# poisson-process-queue
Implementation of M/M/1 queue with poisson arrivals and exponentially ditributed service time. Based on the exercise 8.27 of Probability and Computing (2nd edition), by Michael Mitzenmacher and Eli Upfal.

# Execution
    python main.py

# Output
    Lambda: 0.5
    Exponentially distributed service time.
    -> Average amount of time spent in the system per customer who completed service: 2.01 s.
    -> Customers served: 500240
    -> Total time elapsed: 9997.97 s.

    Lambda: 0.8
    Exponentially distributed service time.
    -> Average amount of time spent in the system per customer who completed service: 5.06 s.
    -> Customers served: 799845
    -> Total time elapsed: 9995.58 s.

    Lambda: 0.9
    Exponentially distributed service time.
    -> Average amount of time spent in the system per customer who completed service: 10.06 s.
    -> Customers served: 898286
    -> Total time elapsed: 10001.58 s.

    Lambda: 0.99
    Exponentially distributed service time.
    -> Average amount of time spent in the system per customer who completed service: 55.79 s.
    -> Customers served: 982668
    -> Total time elapsed: 10219.5 s.

    Lambda: 0.5
    Fixed service time.
    -> Average amount of time spent in the system per customer who completed service: 1.5 s.
    -> Customers served: 500500
    -> Total time elapsed: 10001.81 s.

    Lambda: 0.8
    Fixed service time.
    -> Average amount of time spent in the system per customer who completed service: 3.01 s.
    -> Customers served: 800031
    -> Total time elapsed: 10000.03 s.

    Lambda: 0.9
    Fixed service time.
    -> Average amount of time spent in the system per customer who completed service: 5.41 s.
    -> Customers served: 898797
    -> Total time elapsed: 10006.0 s.

    Lambda: 0.99
    Fixed service time.
    -> Average amount of time spent in the system per customer who completed service: 34.67 s.
    -> Customers served: 985057
    -> Total time elapsed: 10045.04 s.
