from setuptools import setup

setup(

	name='greeting',
	version='0.3',
	url='https://github.com/purvesh-linux11/test',
	author='purvesh-linux11',
	author_email='purvesh.linux11@protonmail.com',
	entry_points={
		'console_scripts':[
			'greeting=greeting:main'
		]
	},
	description='sample test snap'
)
