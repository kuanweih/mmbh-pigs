
PATH_RUN = '/home/dir/'

BOXSIZE = 15.    # Mpc/h

HUBBLE = 0.697
TOMSUN = 1e10 / HUBBLE

""" mass funcstions """
N_BIN = 30
HALO_MIN = 1e8
HALO_MAX = 1e13
BH_MIN = 1e3
BH_MAX = 1e9
STAR_MIN = 1e5
STAR_MAX = 1e12

""" t1 calculations"""
NMESHS = [5, 15]    # BOXSIZE / scales
EPSILON = 1e-40    # deal with ki==0.


def create_dir(dir_name):
    """ create directory name according to the run """
    import os
    import errno
    if not os.path.exists(os.path.dirname(dir_name)):
        try:
            os.makedirs(os.path.dirname(dir_name))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
