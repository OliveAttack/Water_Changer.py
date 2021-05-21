#this is a water energy calculator
mass = 23
# input mass here
starting_temperature = -10
ending_temperature = 109
temperature_difference = ending_temperature - starting_temperature
phase_fusion = mass * 333.5
phase_vapor = mass * 2256
#temperatures are in celsius

#heating ice
if starting_temperature < 0:
    if ending_temperature < 0:
        ending_energy = 2.09 * mass * temperature_difference
    elif ending_temperature <= 100:
        ending_energy = (2.09 * mass * abs(starting_temperature)) + (phase_fusion) + (mass * 4.18 * ending_temperature)
    else:
        ending_energy = (2.09 * mass * abs(starting_temperature)) + (phase_fusion) + (mass * 418) + phase_vapor + (mass * 2.01 * (ending_temperature - 100))

#heating water
elif starting_temperature < 100:
    if ending_temperature < 0:
        ending_energy = ((2.09 * mass * abs(ending_temperature)) + (phase_fusion) + (mass * 4.18 * starting_temperature)) * -1
    elif ending_temperature < 100:
        ending_energy = mass * temperature_difference * 4.18
    else:
        ending_energy = (mass * 4.18 * (100 - starting_temperature)) + phase_vapor + (mass * 2.01 * (ending_temperature - 100))

#dealing with steam
elif starting_temperature > 100:
    if ending_temperature < 0:
        ending_energy = ((2.09 * mass * abs(ending_temperature)) + (phase_fusion) + (mass * 418) + phase_vapor + (mass * 2.01 * (starting_temperature - 100))) * -1
    elif ending_temperature < 100:
        ending_energy = ((mass * 4.18 * (100 - ending_temperature)) + phase_vapor + (mass * 2.01 * (starting_temperature - 100))) * -1
    else:
        ending_energy = mass * 2.01 * temperature_difference
        
print(ending_energy)
