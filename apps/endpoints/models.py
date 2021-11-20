from django.db import models


# Create your models here.
class Endpoint(models.Model):
    '''
    The Endpoint class represents an API endpoint, it has the following attributess:
        name: The name of the API point used in the API URL
        owner: Owner of the API endpoint
        created_at: date point at which the API point is created
    '''

    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class MLAlgorithm(models.Model):
    '''
    The MLAlgorithm class represents the ML algo object
    It has the following attributes:
        name: name of the algorithm
        description: short description of how the algorithm works
        code: code of the algo
        version: version of the algorithm(similar to software versioning)
        owner: name of the owner
        created_at: date point of the creation of the ML algo
        parent_endpoint: Reference to the endpoint

    '''
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=5000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):
    '''
    The MLAlgorithmStatus represents the status of the MLAlgorithm which can change during the time
    Attribs:
        status: testing, staging, production, ab_testing
        active: boolean to indicate activity
        created_by: name of the creator
        created_at: date of creation
        parent_mlalgorithm: reference  to the corresponding ML algo

    '''
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="status")


class MLReq(models.Model):
    '''
    MLRequest will keep information about all requests to the ML Algorithms
    Attribs:
        input_data:the input data to the ML algorithm in JSON format
        full_response:the response of the ML algorithm
        response: response in JSON format
        feedback: the feedback about the response in JSON
        created_at: date point of creation
        parent_mlalgorithm: reference to the ML algo used in order to compute the response
    '''
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)


class ABTest(models.Model):
    '''
    The ABtest class keeps info about A/B tests
    Attribs:
        title: The title of the given test
        created_by: The name of the creator
        created_at: The date of test creation
        ended_at: The date of the test stop
        summary: test summary created at test stop
        parent_mlalgorithm_1: reference to the first corresponding mlalgo
        parent_mlalgorithm_2: reference to the second corresponding mlalgo
    The A/B test keeps information about which algorithm is tested, who and when created the test and when the test
    is stopped
    '''
    title = models.CharField(max_length=10000)
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    summary = models.CharField(max_length=10000, blank=True, null=True)
    parent_mlalgorithm_1 = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="parent_mlalgorithm_1")
    parent_mlalgorithm_2 = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="parent_mlalgorithm_2")
