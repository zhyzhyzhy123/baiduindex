from setuptools import setup, find_packages

setup(
    name = 'baiduindex',
    version = '0.0.1',
    keywords='spider baidu toutiao',
    description = 'A spider on baidu',
    license = 'MIT License',
    url = 'https://github.com/zhyzhyzhy123/baiduindex',
    author = 'Hongyi Zhu',
    author_email = '472739561@qq.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['datetime', 'json', 'requests'],
)