from flask import Blueprint
from core import db 
from core.apis import decorators 
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentGradeSchema
principal_assignment_resources = Blueprint('principal_assignment_resources', __name__) 


@principal_assignment_resources.route('/', methods=['GET'], strict_slashes=False) 
@decorators.authenticate_principal
def list_assignments(p): 
    """List all submitted or graded assignments""" 
    principal_assignments = Assignment.get_assignments_by_principal() 
    principal_assignments_dump = AssignmentSchema().dump(principal_assignments, many=True)
    return APIResponse.respond(data=principal_assignments_dump) 
