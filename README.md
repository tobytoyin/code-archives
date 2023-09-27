# python-archives

The main purpose of this archive is to store various Python codes & examples in a reproducible ways: 
1. create a new archive and each archive should be a standalone environment
2. at each archive root, maintain a `README.md` to indicate the root and intend.
3. if an archive is showcasing an architecture which simulates different deployable unit. Use a `README.md` to define the root.

To create a new archive, run: 

```shell
cp -r template <my_archive>
```

We can also use poetry if dependency is important: 

```shell 
poetry new <my_archive>
```


