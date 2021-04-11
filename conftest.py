import json
from os.path import join
import pytest
from kubernetes import client, config
import allure
from definitions import container_list_location, kubeconfig_file


@pytest.fixture(scope="function", autouse=True)
def get_kube_env(label_selector):
    yield
    containers_list = {}
    config.load_kube_config(config_file=kubeconfig_file)

    v1 = client.CoreV1Api()
    # print("Listing pods with their IPs and containers:")

    if label_selector is None:
        ret = v1.list_pod_for_all_namespaces(watch=False)

        for i in ret.items:
            # print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
            pod = v1.read_namespaced_pod(namespace=i.metadata.namespace, name=i.metadata.name)

            for container in pod.spec.containers:
                # print(container.image)
                containers_list[i.metadata.namespace + ":" + i.metadata.name] = container.image
    else:
        for label in label_selector:
            ret = v1.list_pod_for_all_namespaces(watch=False, **label)

            for i in ret.items:
                # print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
                pod = v1.read_namespaced_pod(namespace=i.metadata.namespace, name=i.metadata.name)

                for container in pod.spec.containers:
                    # print(container.image)
                    containers_list[i.metadata.namespace + ":" + i.metadata.name] = container.image



    container_list_file = join(container_list_location, "container_list.json")

    with open(file=container_list_file, mode="w", encoding="utf-8") as file:
        json.dump(containers_list, file)

    allure.attach.file(source=container_list_file, name="container_list.json",
                       attachment_type=allure.attachment_type.JSON)
