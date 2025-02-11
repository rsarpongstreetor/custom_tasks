from setuptools import setup, find_packages
import os
import shutil

def copy_task_configs():
    """Copies task configurations and environment files to BenchMARL."""
    # Define source and destination paths
    source_paths = [
        os.path.join(os.path.dirname(__file__), 'conf', 'task', 'customenv', 'task_1.yaml'),
        os.path.join(os.path.dirname(__file__), 'conf', 'task', 'customenv', 'task_2.yaml'),
        os.path.join(os.path.dirname(__file__), 'environments', 'customenv', 'common.py'),
        os.path.join(os.path.dirname(__file__), 'environments', 'customenv', 'task_1.py'),
        os.path.join(os.path.dirname(__file__), 'environments', 'customenv', 'task_2.py'),
    ]
    destination_paths = [
        os.path.join('BenchMARL', 'benchmarl', 'conf', 'task', 'customenv', 'task_1.yaml'),
        os.path.join('BenchMARL', 'benchmarl', 'conf', 'task', 'customenv', 'task_2.yaml'),
        os.path.join('BenchMARL', 'benchmarl', 'environments', 'customenv', 'common.py'),
        os.path.join('BenchMARL', 'benchmarl', 'environments', 'customenv', 'task_1.py'),
        os.path.join('BenchMARL', 'benchmarl', 'environments', 'customenv', 'task_2.py'),
    ]

    # Create destination directories if they don't exist
    os.makedirs(os.path.dirname(destination_paths[0]), exist_ok=True)  # For YAML files
    os.makedirs(os.path.dirname(destination_paths[2]), exist_ok=True)  # For Python files

    # Copy the files
    for source_path, destination_path in zip(source_paths, destination_paths):
        shutil.copy2(source_path, destination_path)

# Call the function to copy the files before installation
copy_task_configs()

setup(
    name='custom_tasks',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['benchmarl', 'torchrl', 'tensordict', 'torch_geometric', 'pyyaml' ],
)
