# Author: Jorge Rodriguez
# Date: April 25, 2017
# Employee and ProductionWorker Class, assignment

from chapter11 import employee

# Get employee information
name = input("Enter Production Worker employee's name: ")
emp_number = input("Employee's number: ")
shift = int(input("Shift number (day=1 or night=2): "))
pay_rate = input("Hourly pay rate: $")

# Determine the shift
if shift == 1:
    shift = "Day shift"
else:
    shift = "Night shift"

# Create an instance of Production Worker
production_worker = employee.ProductionWorker(name, emp_number, shift, pay_rate)

print("Name of production worker employee:", name)
print(f"Number of employee : #{emp_number}")
print("Shift:", shift)
print(f"Pay rate: ${pay_rate}")
