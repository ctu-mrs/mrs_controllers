#!/usr/bin/python

def replace( filename ):
    with open(filename, 'r') as file :
        filedata = file.read()
        
        filedata = filedata.replace('ldl_solve(', 'ldl_solve' + new_suffix_functions + '(')
        filedata = filedata.replace('ldl_factor(', 'ldl_factor' + new_suffix_functions + '(')
        filedata = filedata.replace('check_factorization(', 'check_factorization' + new_suffix_functions + '(')
        filedata = filedata.replace('matrix_multiply(', 'matrix_multiply' + new_suffix_functions + '(')
        filedata = filedata.replace('check_residual(', 'check_residual' + new_suffix_functions + '(')
        filedata = filedata.replace('fill_KKT(', 'fill_KKT' + new_suffix_functions + '(')
        filedata = filedata.replace('multbymA(', 'multbymA' + new_suffix_functions + '(')
        filedata = filedata.replace('multbymAT(', 'multbymAT' + new_suffix_functions + '(')
        filedata = filedata.replace('multbymG(', 'multbymG' + new_suffix_functions + '(')
        filedata = filedata.replace('multbymGT(', 'multbymGT' + new_suffix_functions + '(')
        filedata = filedata.replace('multbyP(', 'multbyP' + new_suffix_functions + '(')
        filedata = filedata.replace('fillq(', 'fillq' + new_suffix_functions + '(')
        filedata = filedata.replace('fillh(', 'fillh' + new_suffix_functions + '(')
        filedata = filedata.replace('fillb(', 'fillb' + new_suffix_functions + '(')
        filedata = filedata.replace('pre_ops(', 'pre_ops' + new_suffix_functions + '(')
        filedata = filedata.replace('eval_gap(', 'eval_gap' + new_suffix_functions + '(')
        filedata = filedata.replace('set_defaults(', 'set_defaults' + new_suffix_functions + '(')
        filedata = filedata.replace('setup_pointers(', 'setup_pointers' + new_suffix_functions + '(')
        filedata = filedata.replace('setup_indexed_params(', 'setup_indexed_params' + new_suffix_functions + '(')
        filedata = filedata.replace('setup_indexed_optvars(', 'setup_indexed_optvars' + new_suffix_functions + '(')
        filedata = filedata.replace('setup_indexing(', 'setup_indexing' + new_suffix_functions + '(')
        filedata = filedata.replace('set_start(', 'set_start' + new_suffix_functions + '(')
        filedata = filedata.replace('eval_objv(', 'eval_objv' + new_suffix_functions + '(')
        filedata = filedata.replace('fillrhs_aff(', 'fillrhs_aff' + new_suffix_functions + '(')
        filedata = filedata.replace('fillrhs_cc(', 'fillrhs_cc' + new_suffix_functions + '(')
        filedata = filedata.replace('refine(', 'refine' + new_suffix_functions + '(')
        filedata = filedata.replace('calc_ineq_resid_squared(', 'calc_ineq_resid_squared' + new_suffix_functions + '(')
        filedata = filedata.replace('calc_eq_resid_squared(', 'calc_eq_resid_squared' + new_suffix_functions + '(')
        filedata = filedata.replace('better_start(', 'better_start' + new_suffix_functions + '(')
        filedata = filedata.replace('fillrhs_start(', 'fillrhs_start' + new_suffix_functions + '(')
        filedata = filedata.replace('solve(', 'solve' + new_suffix_functions + '(')
        filedata = filedata.replace('main(', 'main' + new_suffix_functions + '(')
        filedata = filedata.replace('load_default_data(', 'load_default_data' + new_suffix_functions + '(')
        filedata = filedata.replace('tic(', 'tic' + new_suffix_functions + '(')
        filedata = filedata.replace('toc(', 'toc' + new_suffix_functions + '(')
        filedata = filedata.replace('tocq(', 'tocq' + new_suffix_functions + '(')
        filedata = filedata.replace('printmatrix(', 'printmatrixd' + new_suffix_functions + '(')
        filedata = filedata.replace('unif(', 'unif' + new_suffix_functions + '(')
        filedata = filedata.replace('ran1(', 'ran1d' + new_suffix_functions + '(')
        filedata = filedata.replace('randn_internal(', 'randn_internal' + new_suffix_functions + '(')
        filedata = filedata.replace('randn(', 'randn' + new_suffix_functions + '(')
        filedata = filedata.replace('reset_rand(', 'reset_rand' + new_suffix_functions + '(')
        
        filedata = filedata.replace('Params', 'Params' + new_suffix_variables)
        filedata = filedata.replace('params', 'params' + new_suffix_variables)
        filedata = filedata.replace('Vars', 'Vars' + new_suffix_variables)
        filedata = filedata.replace('vars', 'vars' + new_suffix_variables)
        filedata = filedata.replace('Settings', 'Settings' + new_suffix_variables)
        filedata = filedata.replace('settings', 'settings' + new_suffix_variables)
        filedata = filedata.replace('Workspace', 'Workspace' + new_suffix_variables)
        filedata = filedata.replace('work', 'work' + new_suffix_variables)


    with open(filename, 'w') as file :
        file.write(filedata)

new_suffix_variables = 'Controller'
new_suffix_functions = '_controller'
replace("solver.h")
replace("solver.c")
replace("csolve.c")
replace("ldl.c")
replace("matrix_support.c")
replace("util.c")
