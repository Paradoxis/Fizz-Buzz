from distutils.core import setup
from pip.req import parse_requirements
from pip.download import PipSession


setup(
    name='fizz-buzz',
    version='1.0.0',
    url='https://github.com/Paradoxis/Fizz-Buzz',
    license='DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE',
    author='Paradoxis',
    author_email='luke@paradoxis.nl',
    description='Ace that job interview with minimal effort, good developers write clean code, master developers don\'t write any at all.',
    keywords=['FizzBuzz', 'Fizz', 'Buzz'],
    download_url='https://codeload.github.com/Paradoxis/Fizz-Buzz/tar.gz/master',
)
