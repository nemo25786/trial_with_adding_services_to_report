import os
from os.path import join

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
kubeconfig_folder = join(ROOT_DIR, "kubeconfig_file")
kubeconfig_folder = join(kubeconfig_folder, "config")
container_list_location = join(ROOT_DIR, "container_list_files")

