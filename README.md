# KivyExampleWithPyinstaller
An example of a simple kivy program and the associated pyinstaller spec file, to build a Windows exe

The specfile has been modifed with the required kivy additons.  The spec file is python code. The variables app_name and win_icon have been added to simplify future edits.
The datas section list the data files to be included in the bundle.  For this simple example this is one .kv file.  The datas tuples list the source files, and the destination directory.

In main.py the kivy console is turned off in the app is frozen.
