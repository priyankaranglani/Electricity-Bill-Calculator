'''
Electricity bill
-----------------------------
For RGP (Residential):
0–50 units → ₹3.20 per unit
51–200 units → ₹3.90 per unit
Above 200 units → ₹4.90 per unit
'''
#taking user input.
units = int(input("enter total  units consumed:"))


if(units<=50):
  bill = (units*3.20)
elif(units<=200):
  bill = ((50*3.20)+(units-50)*3.90)
else:
  bill = ((50*3.20)+(150*3.90)+(units-200)*4.90)

#Additional charges.
fpppa_charges = units*0.391
fixed_charges = 50
energy_charges = bill
total_energy_charge = fpppa_charges+fixed_charges +energy_charges
previous_dues = 131.84

govt_duty = (total_energy_charge*15)/100

print("fpppa_charges:",fpppa_charges)
print("fixed_charges:",fixed_charges)
print("energy_charges:",energy_charges)
print("total_energy_charges:",total_energy_charge)
print("govt_duty:",govt_duty)
print("total Bill is:",round(bill+total_energy_charge+govt_duty-previous_dues,2))