from pytest_testrail.plugin import pytestrail


def case(*ids):
    return pytestrail.case(*ids)
