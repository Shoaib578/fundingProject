from flask import Blueprint,jsonify,request,render_template,redirect,url_for,flash
from flask_login import login_user, current_user, logout_user, login_required
from application import db
from application.models.company import Company
from application.models.fund import Fund
from application.models.module import Module
from application.models.task import Task
from application.models.working_package import WorkingPackage
from datetime import datetime
main  = Blueprint('main', __name__)

@main.route('/')
@login_required
def Home():
    user_id = current_user.id
    funds = Fund.query.filter_by(user_id=user_id).all()
    return render_template('main/home.html',page_name="Home",funds=funds)



@main.route('/add_fund',methods=['GET','POST'])
def AddFund():
    if request.method == 'POST':
        user_id = current_user.id
        fund_name = request.form.get('fund_name')
        fund_description = request.form.get('fund_description')
        new_fund = Fund(fund_name=fund_name,user_id=user_id,fund_description=fund_description)
        db.session.add(new_fund)
        db.session.commit()
        flash("Fund added successfully")
        return redirect(url_for('main.AddFund'))
    
    return render_template('main/add_fund.html',page_name="Add Fund")


@main.route('/fund/modules/<int:fund_id>',methods=['GET', 'POST'])
def FundModules(fund_id):
    modules = Module.query.filter_by(fund_id=fund_id).all()

    if request.method == 'POST':
        module_name = request.form.get('module_name')
        new_module = Module(module_name=module_name, fund_id=fund_id)
        db.session.add(new_module)
        db.session.commit()
        flash("Module added successfully")
        return redirect(url_for('main.FundModules',fund_id=fund_id))
    return render_template('main/modules.html',page_name="Modules",modules=modules,fund_id=fund_id)



@main.route('/module/packages/<int:module_id>',methods=['GET', 'POST'])
def ModuleWorkingPackages(module_id):
    working_packages = WorkingPackage.query.filter_by(module_id=module_id).all()
    if request.method == 'POST':
        package_name = request.form.get('package_name')
       

        new_working_package = WorkingPackage(package_name=package_name, module_id=module_id)
        db.session.add(new_working_package)
        db.session.commit()
        flash("Working Package added successfully")
        return redirect(url_for('main.ModuleWorkingPackages',module_id=module_id))
    return render_template('main/working_packages.html',page_name="Working Packages",module_id=module_id,working_packages=working_packages)


@main.route('/working_packages/tasks/<int:package_id>',methods=['GET', 'POST'])
def WorkingPackageTasks(package_id):
    tasks = Task.query.filter_by(working_package_id=package_id).all()
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        task_description = request.form.get('task_description')
        task_due_date = request.form.get('task_due_date')
        new_task = Task(task_name=task_name, working_package_id=package_id,task_description=task_description,due_date=task_due_date)
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully")
        return redirect(url_for('main.WorkingPackageTasks',package_id=package_id))
    
    
    return render_template('main/tasks.html',page_name="Tasks",package_id=package_id,tasks=tasks)

@main.route('/logout')
def Logout():
    logout_user()
    return redirect(url_for('auth.Login'))