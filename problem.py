from typing import List

"""
Problem Statement

There are 5-20 deliveries that need to be
made from a central pickup point.
You have between 2 and 5 cars to do the deliveries.
Drivers pick up at a central point and then return to that point 
at the end of their route to pick up more deliveries.
"""

"""
P0 Task

Given a list of addresses, 
return a List[int] set of indices that
minimizes the total route travel time for a single car.

Print out the total travel time.

Inputs:
  delivery_addresses: List of addresses to deliver to
                      1 < len(delivery_addresses) < 7

  hq_address: All routes must start and end at hq_address

Returns:
  route: list of indices into delivery_addresses
  len(route) == len(delivery_addresses)
"""


def optimize_route(delivery_addresses: List[str], hq_address: str) -> List[int]:
    # Make this better!
    return [i for i in range(len(delivery_addresses))]


"""
P1 Task

Given a list of addresses,
return List[List[int]] set of cars
(groups of addresses) such that each car
makes deliveries such that each car makes less than
max_deliveries_per_car deliveries and such that
the routes are easy to complete (i.e. one car should deliver
to all the addresses in a neighborhood).

Inputs:
   delivery_addresses: List of addresses to deliver to
                       1 < len(delivery_addresses) < 20

Returns:
   cars: A list of cars. Each car is a List[int].
         car[i] is an index into the delivery_addresses input.
   Constraints:
   all([len(car) < max_deliveries_per_car for car in cars])
   The groupings here should be easy for optimize_route to optimize!
"""


def assign_to_cars(delivery_addresses: List[str], num_cars: int, max_deliveries_per_car: int) -> List[List[int]]:
    # Make this better!
    cars = []
    car: List[int] = []
    for i, delivery in enumerate(delivery_addresses):
        if len(car) < max_deliveries_per_car:
            car.append(i)
        else:
            cars.append(car)
            car = [i]
    return cars


"""
Appendix / FAQ
Address Format: comma delimited string

addressline1, city, zipcode, USA

i.e.

2 N 6th St, Brooklyn, 11249, USA
"""
