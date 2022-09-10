from setuptools import setup

package_name = 'helloworld_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ydh',
    maintainer_email='ydh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'helloworld_publisher = helloworld_pkg.helloworld_publisher:main',
        'helloworld_subscriber = helloworld_pkg.helloworld_subscriber:main',
        ],
    },
)
