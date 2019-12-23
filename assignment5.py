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
    #gscript.run_command(v.buffer, input='Settlements', value=, output='Settlements_buffer_old', overwrite=True)
    #gscript.run_command(v.buffer, input='Settlements', value=, output='Settlements_buffer_new', overwrite=True)
    #create layer with available areas
    #gscript.run_command(v.patch, input=, output='Areas_old', overwrite=True)
    #gscript.run_command(v.patch, input=, output='Areas_new', overwrite=True)
    #calculate slope
    #gscript.run_command('r.slope', input='DEM', output='slope', overwrite=True)

    #compare areas with the two distances to settlements


if __name__ == '__main__':
    main()
