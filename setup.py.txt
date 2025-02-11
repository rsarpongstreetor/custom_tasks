from setuptools import setup, find_packages

setup(
    name='custom_tasks',
    version='0.1.0',  # Update with your version
    packages=find_packages(include=['custom_tasks', 'custom_tasks.*']),  # Include subpackages
    install_requires=['benchmarl', 'torchrl', 'tensordict', 'torch_geometric', 'pyyaml'],  # Add other dependencies
    # Add entry points for custom tasks (optional)
    entry_points={
        'benchmarl.tasks': [
            'customenv/task_1 = custom_tasks.conf.task.customenv.task_1:task_1',
            # Add more entry points for other tasks
        ],
    },
)
