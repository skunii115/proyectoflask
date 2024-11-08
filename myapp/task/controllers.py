from flask import Blueprint

taskRoute = Blueprint('task', __name__, url_prefix='/task')

#Creacion de rutas en el modulo rutas
@taskRoute.route('/')
def index():
    return 'Index'

@taskRoute.route('/<int:id>')#devuelve un registro especificos
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    return 'delete ' +str(id)

@taskRoute.route('/create', methods=('GET','POST'))
def create():
    return 'Create '

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])
def update(id:int):
    return 'update '+str(id)