import pytest

label_selector = [
    {"label_selector": 'app=dl-manager-gw'},
    {"label_selector": 'app=storybook'},
    {"label_selector": 'app.kubernetes.io/instance=aircraft-repo-mock-gateway'}
]

@pytest.mark.parametrize("label_selector", [(label_selector)])
def test_0(label_selector, get_kube_env):
    assert False

@pytest.mark.parametrize("label_selector", [(label_selector)])
def test_1(label_selector, get_kube_env):
    assert True

no_suitable_label_selector = [
    {"label_selector": 'app=fooo'},
]
@pytest.mark.parametrize("label_selector", [(no_suitable_label_selector)])
def test_no_selector_suitable(label_selector, get_kube_env):
    assert True


label_selector_none = None
@pytest.mark.parametrize("label_selector", [(label_selector_none)])
def test_empty_selector(label_selector, get_kube_env):
    assert True
