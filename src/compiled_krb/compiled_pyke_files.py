# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', 'knowledge_base/', 'disease.kfb'):
           [1464351306.6300614, 'disease.fbc'],
         ('', 'knowledge_base/', 'diagnose.krb'):
           [1464351306.6420116, 'diagnose_fc.py'],
        },
        compiler_version)

