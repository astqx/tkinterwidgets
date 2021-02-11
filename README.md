
# Tkinter Custom Widgets

This package contains custom `tkinter` widgets that might be useful.

## Installation

```shell
pip install tkinterwidgets
``` 

## Widgets

* ### Label

  #### Features
  * Transparent background
  * Control opacity

  #### Usage 
  Can be used in the same manner as the default `Label` of `tkinter`, with the following exceptions:
  * Specifying the parent is a compulsory positional argument.
  * Additional optional parameter of `opacity` can be provided to control the opacity of the contents on a scale of `0` to `1` (where `0` implies transparent and `1` implies opaque)

  #### Sample Code
  ```python
  from tkinter import *
  import tkinterwidgets as tkw 

  root=Tk()
  root.config(bg='yellow')

  label=Label(root,text='Default Label')
  label.pack()

  trans_label=tkw.Label(root,text='tkinterwidgets Label',opacity=0.7)
  trans_label.pack(pady=10)

  root.mainloop()
  ```

