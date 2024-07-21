from flask import Blueprint 
from core import db 
from core.apis import decorators 
from core.apis.responses import APIResponse 
from core.models.teachers import Teacher 
from core.apis.teachers.schema import TeacherSchema

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__) 

@principal_teachers_resources.route('/', methods=['GET'], strict_slashes=False) 
@decorators.authenticate_principal 
def list_teachers(p): 
    principal_teachers = Teacher.get_teachers() 
    principal_teachers_dump = TeacherSchema().dump(principal_teachers, many=True)
    return APIResponse.respond(data=principal_teachers_dump)