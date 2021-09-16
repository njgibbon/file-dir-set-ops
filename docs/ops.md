# Build
```
# Top level dir
# Delete dist/
rm -rf dist
python3 setup.py sdist
twine upload dist/*
```


# Dev
```
python3 file_dir_set_ops/main.py --op diff --paths tests/data/a tests/data/b tests/data/c
```


# Test
```
python3 -m unittest discover tests 
```
