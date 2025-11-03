import helper.printing_functions
from helper.printing_functions import print_models as pm
from helper.printing_functions import show_completed_models as scm
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
pm(unprinted_designs, completed_models)
scm(completed_models)