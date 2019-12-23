#!/usr/bin/env python

import grass.script as gscript


def main():
    gscript.run_command('g.region', flags='p')
    #import data
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium Heidelberg\1. Semester\FOSSGIS\Projekt\Final_Project_Group5\Daten\NeckarOdenwaldKreis.geojson", output='NOK', flags='t', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium Heidelberg\1. Semester\FOSSGIS\Projekt\Final_Project_Group5\Daten\RheinNeckarKreis.geojson", output = 'RNK', flags='t', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium Heidelberg\1. Semester\FOSSGIS\Projekt\Final_Project_Group5\Daten\Streets.geojson", output='Streets', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium Heidelberg\1. Semester\FOSSGIS\Projekt\Final_Project_Group5\Daten\Settlements.geojson", output='Settlements', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium Heidelberg\1. Semester\FOSSGIS\Projekt\Final_Project_Group5\Daten\Industrie_Gewerbegebiete.geojson", output='Industial/Commercial', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium Heidelberg\1. Semester\FOSSGIS\Projekt\Final_Project_Group5\Daten\Aussiedlerhöfe.geojson", output='farmyards', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium Heidelberg\1. Semester\FOSSGIS\Projekt\Final_Project_Group5\Daten\Railways.geojson", output='Railways', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium Heidelberg\1. Semester\FOSSGIS\Projekt\Final_Project_Group5\Daten\aeroways.geojson", output='Airports', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium Heidelberg\1. Semester\FOSSGIS\Projekt\Final_Project_Group5\Daten\power.geojson", output='Powerlines', overwrite=True)
    #merge districts
    gscript.run_command('v.patch', input=['RNK', 'NOK'], output='Region', overwrite=True)
    #clip areas
    gscript.run_command('v.clip', input='Streets', output='Streets_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Settlements', output='Settlements_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Industrial/Commercial', output='Industrial/Commercial_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Farmyards', output='Farmyards_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Railways', output='Railways_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Airports', output='Airports_region', clip='Region', overwrite=True)
    gscript.run_command('v.clip', input='Powerlines', output='Powerlines_region', clip='Region', overwrite=True)


if __name__ == '__main__':
    main()
