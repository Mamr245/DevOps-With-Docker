while True:
    try:
        year = int(input('Input vehicle registration year (2007 and onwards):  '))
        if year < 2007:
            print('Input a year bigger or equal than 2007')
        else:
            break;
    except:
        print('Input a year bigger or equal than 2007')

while True:
    try:
        disp = int(input('Engine displacement(cm3): '))
        if disp <= 0:
            print('Input a value bigger than 0')
        else:
            break;
    except:
        print('Input a value bigger than 0')

while True:
    print('')
    print('Petrol - 1')
    print('Diesel - 2')
    try:
        fuel_type = int(input('Fuel type: '))
        if fuel_type in [1,2]:
            break
        else:
            print('Please type "1" (Petrol) or "2" (Diesel)')
    except:
        print('Please type "1" (Petrol) or "2" (Diesel)')

while True:
    print('')
    print('NEDC Norm - 1')
    print('WLTP Norm - 2')
    try:
        norm = int(input('Select CO2 emission norm: '))
        if norm in [1,2]:
            if norm == 1:
                try:
                    vCO2_NEDC = int(input("Input vehicle's C02 emissions (g/km): "))
                    if vCO2_NEDC < 0:
                        print('Input a value bigger than 0')
                    else:
                        vCO2_WLTP = 0
                        break
                except:
                    print('Input a value bigger than 0')
            else:
                try:
                    vCO2_WLTP = int(input("Input vehicle's C02 emissions (g/km): "))
                    if vCO2_WLTP < 0:
                        print('Input a value bigger than 0')
                    else:
                        vCO2_NEDC = 0
                        break
                except:
                    print('Input a value bigger than 0')
        else:
            print('Please type "1" (NEDC Norm) or "2" (WLTP Norm)')
    except:
        print('Please type "1" (NEDC Norm) or "2" (WLTP Norm)')


print('')
if disp > 2500:
    tax_disp = 403.23
    print('Displacement Interval:                       More than 2500                      %.2f €' % tax_disp)
elif disp > 1750:
    tax_disp  = 117.82
    print('Displacement Interval:                       1750 up to 2500                     %.2f €' % tax_disp)
elif disp > 1250:
    tax_disp  = 58.97
    print('Displacement Interval:                       1250 up to 1750                     %.2f €' % tax_disp)
else:
    tax_disp  = 29.39
    print('Displacement Interval:                       Up to 1250                          %.2f €' % tax_disp)


if norm == 1 and vCO2_NEDC > 250:
    tax_CO2 = 336.07
    print('CO2 Interval (NEDC):                         More than 250                       %.2f €' % tax_CO2)
elif norm == 1 and vCO2_NEDC > 180:
    tax_CO2 = 196.18
    print('CO2 Interval (NEDC):                         180 up to 250                       %.2f €' % tax_CO2)
elif norm == 1 and vCO2_NEDC > 120:
    tax_CO2 = 90.33
    print('CO2 Interval (NEDC):                         120 up to 180                       %.2f €' % tax_CO2)
elif norm == 1 and vCO2_NEDC <= 120:
    tax_CO2 = 60.28
    print('CO2 Interval (NEDC):                         Up to 120                           %.2f €' % tax_CO2)
else:
    pass

if norm == 2 and vCO2_WLTP > 260:
    tax_CO2 = 336.07
    print('CO2 Interval  (WLTP):                        More than 260                       %.2f €' % tax_CO2)
elif norm == 2 and  vCO2_WLTP > 205:
    tax_CO2 = 196.18
    print('CO2 Interval (WLTP):                         206 up to 260                       %.2f €' % tax_CO2)
elif norm == 2 and vCO2_WLTP > 140:
    tax_CO2 = 90.33
    print('CO2 Interval (WLTP):                         140 up to 205                       %.2f €' % tax_CO2)
elif norm == 2 and vCO2_WLTP <= 140:
    tax_CO2 = 60.28
    print('CO2 Interval (WLTP):                         Up to 140                           %.2f €' % tax_CO2)
else:
    pass

if year >= 2017 and vCO2_NEDC > 250:
    extra_tax_co2 = 58.97
    print('Additional C02 emission tax (NEDC):           More than 250                      %.2f €' % extra_tax_co2)
elif year >= 2017 and vCO2_NEDC > 180:
    extra_tax_co2 = 29.39
    print('Additional C02 emission tax (NEDC):           180 up to 250                      %.2f €' % extra_tax_co2)
else:
    extra_tax_co2 = 0

if year >= 2017 and vCO2_WLTP > 260:
    extra_tax_co2 = 58.97
    print('Additional C02 emission tax (WLTP):          More than 260                       %.2f €' % extra_tax_co2)
elif year >= 2017 and vCO2_WLTP > 205:
    extra_tax_co2 = 29.39
    print('Additional C02 emission tax (WLTP):          205 up to 260                       %.2f €' % extra_tax_co2)
else:
    pass

if year == 2007:
    coef = 1
    print('Acquisition Coeficient:                      Year 2007                           %.2f' % coef)
elif year == 2008:
    coef = 1.05
    print('Acquisition Coeficient:                      Year 2008                           %.2f' % coef)
elif year == 2009:
    coef = 1.1
    print('Acquisition Coeficient:                      Year 2009                           %.2f' % coef)
else:
    coef = 1.15
    print('Acquisition Coeficient:                      Year 2010 onwards                   %.2f' % coef)

if fuel_type == 2 and disp > 2500:
    extra_tax_diesel = 68.85
    print('Additional fuel type tax (Diesel):           More than 2500cm3                   %.2f €' % extra_tax_diesel)
elif fuel_type == 2 and disp > 1750:
    extra_tax_diesel = 20.12
    print('Additional fuel type tax (Diesel):           1750 up to 2500cm3                  %.2f €' % extra_tax_diesel)
elif fuel_type == 2 and disp > 1250:
    extra_tax_diesel = 10.07
    print('Additional fuel type tax (Diesel):           1250 up to 1750cm3                  %.2f €' % extra_tax_diesel)
elif fuel_type == 2 and disp <= 1250:
    extra_tax_diesel = 5.02
    print('Additional fuel type tax (Diesel):           Up to 1250cm3                       %.2f €' % extra_tax_diesel)
else:
    extra_tax_diesel = 0

if fuel_type == 1:
    iuc = (tax_disp + tax_CO2 + extra_tax_co2)*coef
else:
    iuc = (tax_disp + tax_CO2 + extra_tax_co2)*coef + extra_tax_diesel
    
print('')
print('Total tax value: %.2f €' % iuc)


























