# python-archives

The main purpose of this archive is to store various Python codes & examples in a reproducible ways:

1. create a new archive and each archive should be a standalone environment
2. at each archive root, maintain a `README.md` to indicate the root and intend.

## Creating New Archive

To create a new archive, run:

```shell
cp -r template <my_archive>
```

We can also use poetry if dependency is important:

```shell
poetry new <my_archive>
```

## How to tell which folder is an Archive Root

An Archive stores an reproducible codes or example, sometime this could be a single pacakge (containing scripts), or an entire architecture (container multiple packages). Folder tree only represents an organisational structure. 

An folder which contains a `README.md` defines the root of archive and the beginning of the context. `README.md` therein should provides a brief summary about what the Archive is about, usages, or its intend.
