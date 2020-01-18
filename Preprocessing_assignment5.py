#!/usr/bin/env python

import grass.script as gscript


def main():
    '''
    gscript.run_command('g.region', flags='p')
    #import data
    gscript.run_command('v.in.ogr', input=r"C:\Users\carst\fossgis_gawlas\fossgis19_1\project_windkraft\Final_Project_Group5\Daten\NeckarOdenwaldKreis.geojson", output='NOK', flags='t', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\carst\fossgis_gawlas\fossgis19_1\project_windkraft\Final_Project_Group5\Daten\RheinNeckarKreis.geojson", output = 'RNK', flags='t', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\carst\fossgis_gawlas\fossgis19_1\project_windkraft\Final_Project_Group5\Daten\Streets.geojson", output='Streets', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\carst\fossgis_gawlas\fossgis19_1\project_windkraft\Final_Project_Group5\Daten\Settlements.geojson", output='Settlements', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\carst\fossgis_gawlas\fossgis19_1\project_windkraft\Final_Project_Group5\Daten\Industrie_Gewerbegebiete.geojson", output='Industrial_Commercial', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\carst\fossgis_gawlas\fossgis19_1\project_windkraft\Final_Project_Group5\Daten\Aussiedlerhoefe.geojson", output='farmyards', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\carst\fossgis_gawlas\fossgis19_1\project_windkraft\Final_Project_Group5\Daten\Railways.geojson", output='Railways', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\carst\fossgis_gawlas\fossgis19_1\project_windkraft\Final_Project_Group5\Daten\aeroways.geojson", output='Airports', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\carst\fossgis_gawlas\fossgis19_1\project_windkraft\Final_Project_Group5\Daten\power.geojson", output='Powerlines', overwrite=True)
    #merge districts
    gscript.run_command('v.patch', input=['RNK', 'NOK'], output='Region', overwrite=True)
    #set region
    gscript.run_command('g.region', vector='Region')
    gscript.run_command('g.region', flags='p')
    # import raster with extent=region
    gscript.run_command('r.import', input=r"C:\Users\carst\fossgis_gawlas\fossgis19_1\project_windkraft\Final_Project_Group5\Daten\srtm_germany_dsm.tif", extent='region', output='DEM', overwrite=True)
    #clip areas
    gscript.run_command('v.clip', input='Streets', output='Streets_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Settlements', output='Settlements_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Industrial_Commercial', output='Industrial_Commercial_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Farmyards', output='Farmyards_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Railways', output='Railways_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Airports', output='Airports_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Powerlines', output='Powerlines_region', clip='Region', overwrite=True)
    #the command r.clip needs an addon, which will be installed automatically
    '''
    gscript.run_command('r.in.gdal', input='NETCDF:"C:/Users/Ulrike/Desktop/Studium_Heidelberg/1_Semester/FOSSGIS/Projekt/Final_Project_Group5/Daten/Winddaten/fu_ff_mean_year_201902280000_l100.nc":FF', output='Future_winddata')


if __name__ == '__main__':
    main()
