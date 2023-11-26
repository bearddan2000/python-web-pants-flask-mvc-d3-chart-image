pex_binary(
    name="app",
    entry_point="app.py",
    dependencies=[
        ':pysources',
        ':pyresources'
    ]
)

python_requirements()

python_sources(
    name="pysources",
    sources=[
        'app.py',
        'data.py',
    ]
)
resources(
    name='pyresources',
    sources=[
        'templates',
        'static'
    ]
)