from locals import *

from collections import OrderedDict
import itertools

import sklearn.linear_model
import sklearn.svm
import sklearn.ensemble

# Code from http://rosettacode.org/wiki/Power_set#Python
def list_powerset2(lst):
    return reduce(lambda result, x: result + [subset + [x] for subset in result],
                  lst, [[]])
def powerset(s):
    return frozenset(map(frozenset, list_powerset2(list(s))))

def all_hyperparameters(odict):
    hyperparams = list(itertools.product(*odict.values()))
    for h in hyperparams:
        yield dict(zip(odict.keys(), h))

MODEL_HYPERPARAMETERS = {
    "SGDClassifier": OrderedDict({
        "loss": ['hinge', 'log', 'modified_huber'],
        "penalty": ['l2', 'l1', 'elasticnet'],
        "alpha": [0.001, 0.0001, 0.00001],
        "rho": [0.55, 0.85, 0.95],
#        "l1_ratio": [0.05, 0.15, 0.45],
        "fit_intercept": [True],
        "n_iter": [1, 5, 25],
        "shuffle": [True, False],
#        "epsilon": [
        "learning_rate": ["constant", "optimal", "invscaling"],
        "eta0": [0.001, 0.01, 0.1],
        "power_t": [0.1, 0.25, 0.5, 1.],
        "warm_start": [True, False],
    }),

    "SVC": OrderedDict({
        "C": [0.1, 1, 10, 100],
        "kernel": ["rbf", "sigmoid", "linear", "poly"],
        "degree": [1,2,3,4,5],
        "gamma": [1e-3, 1e-5, 0.],
        "probability": [False, True],
        "cache_size": [CACHESIZE],
        "shrinking": [False, True],
    }),

    "SVR": OrderedDict({
        "C": [0.1, 1, 10, 100],
        "epsilon": [0.001, 0.01, 0.1, 1.0],
        "kernel": ["rbf", "sigmoid", "linear", "poly"],
        "degree": [1,2,3,4,5],
        "gamma": [1e-3, 1e-5, 0.],
        "cache_size": [CACHESIZE],
        "shrinking": [False, True],
    }),

    "GradientBoostingRegressor": OrderedDict({
        'loss': ['ls', 'lad', 'huber', 'quantile'],
        'learn_rate': [1., 0.1, 0.01],
        'n_estimators': [10, 32, 100, 320],
        'max_depth': [1, 3, None],
        'min_samples_split': [1, 3],
        'min_samples_leaf': [1, 3],
        'subsample': [0.032, 0.1, 0.32, 1],
    }),

    "RandomForestClassifier": OrderedDict({
        'n_estimators': [10, 32, 100, 320],
        'criterion': ['gini', 'entropy'],
        'max_depth': [1, 3, None],
        'min_samples_split': [1, 3],
        'min_samples_leaf': [1, 3],
        'min_density': [0.032, 0.1, 0.32],
        'max_features': ["sqrt", "log2", None],
#        'bootstrap': [True, False],
        'bootstrap': [True],
        'oob_score': [True, False],
#        'verbose': [True],
    }),

    "RandomForestRegressor": OrderedDict({
        'n_estimators': [10, 32, 100, 320],
        'max_depth': [1, 3, None],
        'min_samples_split': [1, 3],
        'min_samples_leaf': [1, 3],
        'min_density': [0.032, 0.1, 0.32],
        'max_features': ["sqrt", "log2", None],
#        'bootstrap': [True, False],
        'bootstrap': [True],
        'oob_score': [True, False],
#        'verbose': [True],
    }),
}

MODEL_NAME_TO_CLASS = {
    "SGDClassifier": sklearn.linear_model.SGDClassifier,
    "SVC": sklearn.svm.SVC,
    "SVR": sklearn.svm.SVR,
    "GradientBoostingRegressor": sklearn.ensemble.GradientBoostingRegressor,
    "RandomForestClassifier": sklearn.ensemble.RandomForestClassifier,
    "RandomForestRegressor": sklearn.ensemble.RandomForestRegressor,
}
