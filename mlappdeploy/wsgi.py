"""
WSGI config for mlappdeploy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mlappdeploy.settings')

application = get_wsgi_application()
# ML registry
import inspect
from apps.ml.registry import MLReg
from apps.ml.bank_classifier import RandomForestClassifier
from apps.ml.extra_trees import ExtraTreesClassifier
from apps.ml.neural_classifier import NeuralClassifier
try:
    #Create ML registry
    registry=MLReg()
    #RF classifier
    rf=RandomForestClassifier()
    #Add to ML registry

    registry.add_algo(endpoint_name="bank_classifier",
                      algo_object=rf,
                      algo_name="random forest",
                      algo_status="production",
                      algo_version="0.0.1",
                      owner="Rosen",
                      algo_description="Random Forest with pre and post-processing",
                      algo_code=inspect.getsource(RandomForestClassifier)

                      )
    #ExtraTreesClassifier
    et = ExtraTreesClassifier()
    # add to ML registry
    registry.add_algo(endpoint_name="extra_trees",
                      algo_object=et,
                      algo_name="extra forest",
                      algo_status="production",
                      algo_version="0.0.1",
                      owner="Rosen",
                      algo_description="Extra trees classifier with pre and post-processing",
                      algo_code=inspect.getsource(ExtraTreesClassifier))
    # Nnet Classifier
    nn = NeuralClassifier()
    registry.add_algo(endpoint_name="neural_classifier",
                      algo_object=nn,
                      algo_name="neural net",
                      algo_status="production",
                      algo_version="0.0.1",
                      owner="Rosen",
                      algo_description="Neural network sequential model",
                      algo_code=inspect.getsource(NeuralClassifier))
except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
