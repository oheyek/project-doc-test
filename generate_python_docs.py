import os

# Directories and file paths
src_dir = 'src'
rst_file_python = 'source/python.rst'
rst_file_cpp = 'source/cpp.rst'
md_file_python = 'my-project-docs/docs/python.md'
md_file_cpp = 'my-project-docs/docs/cpp.md'

# Generate list of Python modules
python_modules = [f[:-3] for f in os.listdir(src_dir) if f.endswith('.py')]

# Generate python.rst
with open(rst_file_python, 'w') as f:
    f.write('Python\n')
    f.write('=======\n\n')
    for module in python_modules:
        f.write(f'.. automodule:: {module}\n')
        f.write('   :members:\n')
        f.write('   :undoc-members:\n')
        f.write('   :show-inheritance:\n\n')

# Generate python.md
with open(md_file_python, 'w') as f:
    f.write('# Dokumentacja Python\n\n')
    for module in python_modules:
        f.write(f'::: {module}\n')
        f.write('    handler: python\n\n')

# generate list of C++ files
cpp_files = [f for f in os.listdir(src_dir) if f.endswith('.cpp')]

# Generate cpp.rst
with open(rst_file_cpp, 'w') as f:
    f.write('Dokumentacja C++\n')
    f.write('==================\n\n')
    for cpp_file in cpp_files:
        f.write(f'.. doxygenfile:: {cpp_file}\n')
        f.write('   :project: CppProject\n\n')

# Generate cpp.md
with open(md_file_cpp, 'w', encoding='utf-8') as f:
    f.write('# Dokumentacja C++\n\n')
    for cpp_file in cpp_files:
        cpp_path = os.path.join('src', cpp_file)
        f.write(f'## Kod źródłowy: {cpp_file}\n\n')
        f.write('```cpp\n')
        with open(cpp_path, 'r', encoding='utf-8') as cpp_source:
            f.write(cpp_source.read())
        f.write('\n```\n\n')
