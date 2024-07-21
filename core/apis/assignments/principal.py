from flask import Blueprint 
from core import db 
from core.apis import decorators 
from core.apis.responses import APIResponse 
from core.models.assignments import Assignment 

from .schema import AssignmentSchema, AssignmentGradeSchema 
principal_assignments_resources = Blueprint('principal_assignment_resources', __name__) 

@principal_assignments_resources.route('/', methods=['GET'], strict_slashes=False)  
@decorators.authenticate_principal 
def list_assignmetns(p): 
    principal_assignments = Assignment.get_assignments() 
    principal_assignments_dump = AssignmentSchema().dump(principal_assignments, many=True) 
    return APIResponse.respond(data=principal_assignments_dump) 