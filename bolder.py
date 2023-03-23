car_parts = ['brake','Sustainability','Winter','Vacuum-Boster','RE','Piston','Start','Neg-Side-Circuit-Signs','MC','No-Charge-Issue','Hub','Faulty_Sensor','MasterCylinder','Boosters','Vacuum-Booster','Alt','Alternator', 'Spark Plugs', 'Battery', 'Brakes', 'Clutch', 'Master Cylinder', 'Hydro-Booster', 'Calipers', 'Wheel Hub', 'Turbo', 'Vacuum Booster', 'ALT', 'Starter', 'Neg-Side Circuit', 'Phenolic Piston']

with open('input.txt', 'r') as f:
    lines = f.readlines()

bolded_lines = []
for line in lines:
    bolded_line = line
    for part in car_parts:
        bolded_line = bolded_line.replace(part, '\\b ' + part + '\\b0 ')
    bolded_lines.append(bolded_line)

with open('output5ab.rtf', 'w') as f:
    f.write('{\\rtf1\\ansi\n')
    for line in bolded_lines:
        f.write(line.strip() + '\\line\n')
    f.write('}')


