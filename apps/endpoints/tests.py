from django.test import TestCase
import inspect
import apps.ml
import json

from apps.ml.bank_classifier import RandomForestClassifier
from apps.ml.extra_trees import ExtraTreesClassifier
from apps.ml.neural_classifier import NeuralClassifier
from apps.ml.registry import MLReg
from rest_framework.test import APIClient


class MLTest(TestCase):
    def test_rf_algo(self):
        input_data = {'age': 31, 'job': 'student', 'marital': 'married', 'education': 'university.degree',
                      'default': 'no', 'housing': 'yes', 'loan': 'no', 'contact': 'cellular', 'month': 'may',
                      'day_of_week': 'thu', 'duration': 90, 'campaign': 1, 'pdays': 999, 'previous': 0,
                      'poutcome': 'nonexistent', 'emp.var.rate': 1.4, 'cons.price.idx': 93.994, 'cons.conf.idx': -36.4,
                      'euribor3m': 4.857, 'nr.employed': 5228.1}
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('no', response['label'])

    def test_registry(self):
        registry = MLReg()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "bank_classifier"
        algorithm_object = RandomForestClassifier()
        algorithm_name = "random forest"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Rosen"
        algorithm_description = "Random Forest with simple pre- and post-processing"
        algorithm_code = inspect.getsource(RandomForestClassifier)
        # add to registry
        registry.add_algo(endpoint_name, algorithm_object, algorithm_name,
                          algorithm_status, algorithm_version, algorithm_owner,
                          algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)

    def test_predict_view(self):
        client = APIClient()
        input_data = {'age': 31, 'job': 'student', 'marital': 'married', 'education': 'university.degree',
                      'default': 'no', 'housing': 'yes', 'loan': 'no', 'contact': 'cellular', 'month': 'may',
                      'day_of_week': 'thu', 'duration': 90, 'campaign': 1, 'pdays': 999, 'previous': 0,
                      'poutcome': 'nonexistent', 'emp.var.rate': 1.4, 'cons.price.idx': 93.994, 'cons.conf.idx': -36.4,
                      'euribor3m': 4.857, 'nr.employed': 5228.1}
        print(json.dumps(input_data))
        classifier_url = "/api/v1/bank_classifier/predict/"
        response = client.post(classifier_url, input_data, format='json')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["label"], "no")
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)

    def test_et_algo(self):
        input_data = {'age': 31, 'job': 'student', 'marital': 'married', 'education': 'university.degree',
                      'default': 'no', 'housing': 'yes', 'loan': 'no', 'contact': 'cellular', 'month': 'may',
                      'day_of_week': 'thu', 'duration': 90, 'campaign': 1, 'pdays': 999, 'previous': 0,
                      'poutcome': 'nonexistent', 'emp.var.rate': 1.4, 'cons.price.idx': 93.994, 'cons.conf.idx': -36.4,
                      'euribor3m': 4.857, 'nr.employed': 5228.1}
        my_alg = ExtraTreesClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('no', response['label'])

    def nn_algo(self):
        input_data = {'age': 31, 'job': 'student', 'marital': 'married', 'education': 'university.degree',
                      'default': 'no', 'housing': 'yes', 'loan': 'no', 'contact': 'cellular', 'month': 'may',
                      'day_of_week': 'thu', 'duration': 90, 'campaign': 1, 'pdays': 999, 'previous': 0,
                      'poutcome': 'nonexistent', 'emp.var.rate': 1.4, 'cons.price.idx': 93.994, 'cons.conf.idx': -36.4,
                      'euribor3m': 4.857, 'nr.employed': 5228.1}
        my_alg = NeuralClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('no', response['label'])
