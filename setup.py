from setuptools import setup, Distribution, find_packages

class BinaryDistribution(Distribution):
	def is_pure(self):
		return False

setup(	name='epydemic', version='0.1',
		description='Mathematical Biology Package',
		url='https://github.com/yoon-gu/epydemic/',
		author='Jacob Hwang',
		author_email='jacob@dnry.org',
		license='MIT',
		packages=find_packages(),
		install_requires=[
			'pyqtgraph',
			'numpy',
			'scipy',
		],
		include_package_data=True,
		distclass=BinaryDistribution,
		zip_safe=False)