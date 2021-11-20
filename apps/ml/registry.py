from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgorithm
from apps.endpoints.models import MLAlgorithmStatus


class MLReg:
    """
    ML registry class is used to connect the machine learning algorithm with the server code.
    The registry keeps simple dict object with a mapping of algorithm id to algorithm object.
    """

    def __init__(self):
        self.endpoints = {}

    def add_algo(self, endpoint_name, algo_object, algo_name,
                 algo_status, algo_version, owner, algo_description, algo_code):
        # get endpoint
        endpoint, _ = Endpoint.objects.get_or_create(name=endpoint_name, owner=owner)

        # initialize algorithm
        database_object, algo_created = MLAlgorithm.objects.get_or_create(
            name=algo_name,
            description=algo_description,
            code=algo_code,
            version=algo_version,
            parent_endpoint=endpoint

        )
        if algo_created:
            status = MLAlgorithmStatus(status=algo_status,
                                       created_by=owner,
                                       parent_mlalgorithm=database_object,
                                       active=True)
            status.save()
        self.endpoints[database_object.id] = algo_object
