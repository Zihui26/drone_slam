from setuptools import find_packages, setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ws2',
    maintainer_email='glenn.ni@digiplacelab.com',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'setposition = py_pubsub.setposition:main',
            'pysetposition = py_pubsub.pymavlink_setposition:main',
            'realsense = py_pubsub.color_depth:main' 
        ],
    },
)
