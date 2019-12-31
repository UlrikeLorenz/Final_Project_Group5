#!/usr/bin/env python

import grass.script as gscript


def main():
    gscript.run_command('g.region', flags='p')
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium_Heidelberg\1_Semester\FOSSGIS\Assignment5\Roads_BONUS.geojson", output='Roads', overwrite=True)
    gscript.run_command('v.in.ogr', input=r"C:\Users\Ulrike\Desktop\Studium_Heidelberg\1_Semester\FOSSGIS\Assignment5\Stops_BONUS.geojson", output='Stops', overwrite=True)
    gscript.run_command('v.net', input='Roads', points='Stops', output='roads_stops_net', op='connect', threshold=500, overwrite=True)
    gscript.run_command('v.category', input='roads_stops_net', op='report')
    gscript.run_command('v.net.salesman', input='roads_stops_net', center_cats=[1,2,3,4,5,6], output='salesman_distance', overwrite=True)
if __name__ == '__main__':
    main()
