import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    install_requires = [req for req in f.read().split('\n') if req]


setuptools.setup(
    name="naive_translator",
    version="0.0.1",
    author="langzhenning",
    author_email="zhenninglang@163.com",
    description="A naive word by word translator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZhenningLang/naive_translator",
    packages=setuptools.find_packages(),
    python_requires='>=3.2',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'naive_translator = naive_translator.__main__:main',
        ]
    },
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
