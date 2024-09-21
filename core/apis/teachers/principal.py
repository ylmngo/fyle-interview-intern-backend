from flask import Blueprint 
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from core.apis.teachers.schema import TeacherSchema


principal_teacher_resources = Blueprint('principal_teacher_resources', __name__) 

@principal_teacher_resources.route('/', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal 
def list_teachers(p): 
    """List all teachers"""
    principal_teachers = Teacher.list_teachers() 
    principal_teachers_dump = TeacherSchema().dump(principal_teachers, many=True) 
    return APIResponse.respond(data=principal_teachers_dump)
