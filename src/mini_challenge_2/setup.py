from setuptools import find_packages, setup

package_name = 'mini_challenge_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/mini2_launch.py']),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rllaguno',
    maintainer_email='rodrigollagunoc@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'Controller = mini_challenge_2.Controller:main',
            'PointGenerator = mini_challenge_2.PointGenerator:main',
            'Odometry = mini_challenge_2.Odometry:main'
        ],
    },
)
