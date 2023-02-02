#weight of package
weight = 41.5

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20.00
else:
  cost_ground = weight * 4.75 + 20.00

#cost ground shipping
print("Ground Shipping $", cost_ground)

#premium ground fee
premium_ground = 125.00

print("Ground Shipping Premium $", premium_ground)

#total ground shipping cost
print("Total Ground Shipping Fee $", cost_ground + premium_ground)

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

#drone shipping cost
print("Drone Shipping Fee $", cost_drone)
