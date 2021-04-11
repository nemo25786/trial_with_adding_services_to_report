import pytest
from ccst_get_kb8_services_in_report import KubernetesSVCAttach
from definitions import kubeconfig_file, container_list_location
import logging

@pytest.fixture(scope="function", autouse=True)
def get_kube_env(label_selector, get_log=logging.getLogger(), kubeconfig_file=kubeconfig_file):
    yield
    try:
        kb8_attach = KubernetesSVCAttach(kubeconfig_file=kubeconfig_file)
        kb8_attach.attach_svc_to_report(label_selector=label_selector, container_list_location=container_list_location)
    except Exception as e:
        get_log.warning("error in adding list of images to report")



