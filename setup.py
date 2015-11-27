from setuptools import setup, Distribution, find_packages

class BinaryDistribution(Distribution):
	def is_pure(self):
		return False

setup(	name='epydemic', version='0.0',
		description='Mathematical Biology Package',
		url='#',
		author='Yoongu Hwang',
		author_email='yoongu.hwang@gmail.com',
		license='MIT',
		packages=find_packages(),
		install_requires=[
		'pyqtgraph',
		],
		include_package_data=True,
		distclass=BinaryDistribution,
		zip_safe=False)