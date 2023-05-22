from setuptools import setup, find_packages


setup(name='apitest',
      version='1.0',
      description="Practice API testing",
      author='Dmitry Ustimenko',
      author_email='fitlifeua@gmail.com',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest==7.3.1",
          "pytest-html==3.2.0",
          "requests==2.30.0",
          "requests-oauthlib==1.3.1",
          "PyMySQL==1.0.3",
          "WooCommerce==3.0.0)",
      ]
      )