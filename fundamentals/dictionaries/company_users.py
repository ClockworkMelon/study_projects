company_register = {}
while True:
    company_employee_id = input().split(" -> ")

    if company_employee_id[0] == 'End':
        break

    company_name = company_employee_id[0]
    employee_id = company_employee_id[1]

    if company_name not in company_register:
        company_register[company_name] = []

    for company in company_register:
        if employee_id not in company_register[company_name]:
            company_register[company_name].append(employee_id)

for company in company_register:
    print(f'{company}')
    for employee_id in company_register[company]:
        print(f'-- {employee_id}')