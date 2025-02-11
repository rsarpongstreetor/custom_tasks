from setuptools import setup, find_packages
import os
import shutil

def copy_task_configs(base_dir):
    """Copies task configurations and environment files to BenchMARL."""
    # Define source and destination paths using base_dir
    source_paths = [
        os.path.join(base_dir, 'conf', 'task', 'customenv', 'task_1.yaml'),
        os.path.join(base_dir, 'conf', 'task', 'customenv', 'task_2.yaml'),
        os.path.join(base_dir, 'environments', 'customenv', 'common.py'),
        os.path.join(base_dir, 'environments', 'customenv', 'task_1.py'),
        os.path.join(base_dir, 'environments', 'customenv', 'task_2.py'),
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
        if os.path.exists(source_path):  # Check if source file exists
            shutil.copy2(source_path, destination_path)
        else:
            print(f"Warning: Source file not found: {source_path}")

# Call the function after installation using package_data
setup(
    name='custom_tasks',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # ... your package dependencies ...
    ],
    package_data={'custom_tasks': ['conf/task/customenv/*.yaml', 'environments/customenv/*.py']}, # Include data files
    # Use data_files to copy data files during installation
    data_files=[
        ('BenchMARL/benchmarl/conf/task/customenv', ['custom_tasks/conf/task/customenv/task_1.yaml', 'custom_tasks/conf/task/customenv/task_2.yaml']),
        ('BenchMARL/benchmarl/environments/customenv', ['custom_tasks/environments/customenv/common.py', 'custom_tasks/environments/customenv/task_1.py', 'custom_tasks/environments/customenv/task_2.py']),
    ],
)
