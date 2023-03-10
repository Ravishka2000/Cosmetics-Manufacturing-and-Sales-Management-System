from django.http import HttpResponse
from django.shortcuts import redirect


def whmanageronly(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'WarehouseManager':
            return view_func(request, *args, **kwargs)
        if group == 'SupplierManager':
            return redirect('SM_dashboard-SM_dashboard')
        if group == 'SalesManager':
            return redirect('CS_dashboard')
        if group == 'EmployeeSupervisor':
            return redirect('es-dashboard')
        if group == 'customer':
            return redirect('')
        if group == 'Supplier':
            return redirect('S_dashboard-Supplier_dashboard')
        if group == 'BatchProductionManager':
            return redirect('bp_dashboard')
        if group == 'LaboratoryManager':
            return redirect('FL_dashboard')
        if group == 'DeliveryManager':
            return redirect('DM_dashboard')
        if group == 'EmployeeManager':
            return redirect('dashboard')
        if group == 'CostAnalysisManager':
            return redirect('CA_dashboard')
            
    return wrapper_func


def warehousemanager_employeesupervisor(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'WarehouseManager':
            return view_func(request, *args, **kwargs)
        if group == 'EmployeeSupervisor':
            return view_func(request, *args, **kwargs)
        if group == 'SalesManager':
            return redirect('CS_dashboard')
        if group == 'SupplierManager':
            return redirect('SM_dashboard-SM_dashboard')
        if group == 'customer':
            return redirect('')
        if group == 'Supplier':
            return redirect('S_dashboard-Supplier_dashboard')
        if group == 'BatchProductionManager':
            return redirect('bp_dashboard')
        if group == 'LaboratoryManager':
            return redirect('FL_dashboard')
        if group == 'DeliveryManager':
            return redirect('DM_dashboard')
        if group == 'EmployeeManager':
            return redirect('dashboard')
        if group == 'CostAnalysisManager':
            return redirect('CA_dashboard')

    return wrapper_func


def employeesupervisoronly(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'EmployeeSupervisor':
            return view_func(request, *args, **kwargs)
        if group == 'SupplierManager':
            return redirect('SM_dashboard-SM_dashboard')
        if group == 'Supplier':
            return redirect('S_dashboard-Supplier_dashboard')
        if group == 'LaboratoryManager':
            return redirect('FL_dashboard')
        if group == 'customer':
            return redirect('')
        if group == 'WarehouseManager':
            return redirect('wm-dashboard')
        if group == 'BatchProductionManager':
            return redirect('bp_dashboard')
        if group == 'SalesManager':
            return redirect('CS_dashboard')
        if group == 'DeliveryManager':
            return redirect('DM_dashboard')
        if group == 'EmployeeManager':
            return redirect('dashboard')
        if group == 'CostAnalysisManager':
            return redirect('CA_dashboard')

    return wrapper_func
