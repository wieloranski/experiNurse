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
         ('', 'knowledge_base/', 'diagnose.krb'):
           [1463918071.6104581, 'diagnose_fc.py'],
         ('', 'knowledge_base/', 'disease.kfb'):
           [1463918071.6138148, 'disease.fbc'],
        },
        compiler_version)

