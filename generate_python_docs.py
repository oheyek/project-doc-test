import os

src_dir = 'src'
rst_file = 'source/python.rst'
md_file = 'my-project-docs/docs/python.md'

modules = [f[:-3] for f in os.listdir(src_dir) if f.endswith('.py')]

# Generate python.rst
with open(rst_file, 'w') as f:
    f.write('Python\n')
    f.write('=======\n\n')
    for module in modules:
        f.write(f'.. automodule:: {module}\n')
        f.write('   :members:\n')
        f.write('   :undoc-members:\n')
        f.write('   :show-inheritance:\n\n')

# Generate python.md
with open(md_file, 'w') as f:
    f.write('# Dokumentacja Python\n\n')
    for module in modules:
        f.write(f'::: {module}\n')
        f.write('    handler: python\n\n')