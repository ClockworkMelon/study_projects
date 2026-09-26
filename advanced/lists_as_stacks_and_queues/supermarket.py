customer = input()
queue = []
while customer != "End":
    queue.append(customer)

    if customer == "Paid":
        for customer in range(len(queue) - 1):
            print(queue[customer])

        queue = []

    customer = input()

print(f'{len(queue)} people remaining.')
