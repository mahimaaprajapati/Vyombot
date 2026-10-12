from setuptools import setup
import os
from glob import glob

package_name = 'lunabot_perception'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'models'), glob('models/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sneha',
    maintainer_email='sneha@example.com',
    description='YOLO perception module for Lunabot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'yolo_node = lunabot_perception.yolo_node:main',
        ],
    },
)
