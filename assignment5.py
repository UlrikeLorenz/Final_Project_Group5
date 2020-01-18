#!/usr/bin/env python

import grass.script as gscript


def main():
    gscript.run_command('g.region', flags='p')

    '''
    #import data

    gscript.run_command('v.proj', location='finalProject', mapset='assignment5', input='Streets_region', overwrite=True)

    gscript.run_command('v.proj', location='finalProject', mapset='assignment5', input='Settlements_region', overwrite=True)

    gscript.run_command('v.proj', location='finalProject', mapset='assignment5', input='Region', overwrite=True)
    
    gscript.run_command('v.proj', location='finalProject', mapset='assignment5', input='Airports_region', overwrite=True)
    
    gscript.run_command('v.proj', location='finalProject', mapset='assignment5', input='Farmyards_region', overwrite=True)

    gscript.run_command('v.proj', location='finalProject', mapset='assignment5', input='Industrial_Commercial_region', overwrite=True)

    gscript.run_command('v.proj', location='finalProject', mapset='assignment5', input='Landuse_region', overwrite=True)

    gscript.run_command('v.proj', location='finalProject', mapset='assignment5', input='Powerlines_region', overwrite=True)

    gscript.run_command('v.proj', location='finalProject', mapset='assignment5', input='Railways_region', overwrite=True)
    
    gscript.run_command('g.region', vector='Region')
    
    #buffer areas

    gscript.run_command('v.buffer', input='Streets_region', distance=100, output='Streets_buffer', overwrite=True)

    gscript.run_command('v.buffer', input='Settlements_region', distance=700, output='Settlements_buffer_old', overwrite=True)

    gscript.run_command('v.buffer', input='Settlements_region', distance=1000, output='Settlements_buffer_new', overwrite=True)
    
    gscript.run_command('v.buffer', input='Farmyards_region', distance=500, output='Farmyards_buffer', overwrite=True)

    gscript.run_command('v.buffer', input='Industrial_Commercial_region', distance=300, output='Industrial_Commercial_buffer', overwrite=True)

    gscript.run_command('v.buffer', input='Airports_region', distance=1500, output='Airports_buffer', overwrite=True)

    gscript.run_command('v.buffer', input='Powerlines_region', distance=150, output='Powerlines_buffer', overwrite=True)

    gscript.run_command('v.buffer', input='Railways_region', distance=50, output='Railways_buffer', overwrite=True)

    #create layer with available areas

    gscript.run_command('v.patch', input=['Streets_buffer', 'Settlements_buffer_old', 'Airports_buffer', 'Farmyards_buffer', 'Industrial_Commercial_region', 'Powerlines_buffer'], output='Areas_old', overwrite=True)

    gscript.run_command('v.patch', input=['Streets_buffer', 'Settlements_buffer_new', 'Airports_buffer', 'Farmyards_buffer', 'Industrial_Commercial_region', 'Powerlines_buffer'], output='Areas_new', overwrite=True)

    
    #calculate slope
    
    gscript.run_command('r.proj', location='finalProject', mapset='assignment5', input='DEM_region', output='DEM_region', overwrite=True)
    
    gscript.run_command('r.slope.aspect', elevation='DEM_region', slope='slope', aspect='aspect', pcurvature='pcurve', tcurvature='tcurve', overwrite=True)
    '''
    #compare areas with the two distances to settlements

    
    #compare with winddata
    gscript.run_command('r.in.gdal', input='NETCDF:"C:/Users/Ulrike/Desktop/Studium_Heidelberg/1_Semester/FOSSGIS/Projekt/Final_Project_Group5/Daten/Winddaten/fu_ff_mean_year_201902280000_l100.nc":FF', output='Future_winddata')



if __name__ == '__main__':
    main()



'''
#!/usr/bin/env python

import grass.script as gscript


def main():
    gscript.run_command('g.region', flags='p')

    #import data

    gscript.run_command('v.proj', location='finalProject', mapset='assignment5_UTM', input='Streets_region', overwrite=True)

    gscript.run_command('v.proj', location='finalProject', mapset='assignment5_UTM', input='Settlements_region', overwrite=True)

    gscript.run_command('v.proj', location='finalProject', mapset='assignment5_UTM', input='Region', overwrite=True)

    #buffer areas

    gscript.run_command('v.buffer', input='Streets_region', distance=100, output='Streets_buffer', overwrite=True)

    gscript.run_command('v.buffer', input='Settlements', value=700, output='Settlements_buffer_old', overwrite=True)

    gscript.run_command('v.buffer', input='Settlements', value=1000, output='Settlements_buffer_new', overwrite=True)

    #create layer with available areas

    gscript.run_command('v.patch', input=['Streets_buffer', 'Settlements_buffer_old'], output='Areas_old', overwrite=True)

    gscript.run_command('v.patch', input=['Streets_buffer', 'Settlements_buffer_new'], output='Areas_new', overwrite=True)

    #calculate slope

    #gscript.run_command('r.slope', input='DEM', output='slope', overwrite=True)

    #compare areas with the two distances to settlements




if __name__ == '__main__':
    main()

'''