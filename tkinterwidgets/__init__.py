import tkinter as internal_tk 

class _Toplevels():
    def __init__(self):
        self.toplevels=[]

    def lift(self):
        for top in self.toplevels:
            top.toplevel.lift()

    def position(self,event):
        try:
            for top in self.toplevels:
                top.position()
        except:
            pass

class Label():
    def __init__(self,master,opacity=1,transcolor='SystemButtonFace',**kwargs):
        self.master=master
        self.opacity=opacity
        self.transcolor=transcolor
        self.toplevel=internal_tk.Toplevel(self.master)
        self.toplevel.configure(bg=self.transcolor)
        self.toplevel.overrideredirect(True)
        self.toplevel.attributes('-alpha',self.opacity)
        self.toplevel.wm_attributes("-transparentcolor",self.transcolor)
        self.toplevel.withdraw()
        if 'bg' in kwargs:
            del kwargs['bg']
        self.label=internal_tk.Label(self.toplevel,bg=self.transcolor,**kwargs)
        self.change_kwargs=True
        self.master.bind('<Configure>',toplevels.position)
        self.master.bind('<Map>',self._on_map)
        self.master.bind('<Unmap>',self._on_unmap)

    def _on_unmap(self,event):
        self.toplevel.withdraw()

    def _on_map(self,event):
        self.toplevel.deiconify()
        toplevels.position(None)

    def position(self):
        self.x=self.cover_frame.winfo_rootx()
        self.y=self.cover_frame.winfo_rooty()
        self.center_x=self.cover_frame.winfo_width()//2-self.dimentions[0]//2
        self.center_y=self.cover_frame.winfo_height()//2-self.dimentions[1]//2
        self.coords=(self.center_x+self.x,self.center_y+self.y)
        self.toplevel.geometry(f'+{self.coords[0]}+{self.coords[1]}')
        self.master.update_idletasks()
        toplevels.lift()

    def pack(self,**kwargs):
        toplevels.toplevels.append(self)
        if self.change_kwargs:
            self.pack_kwargs=kwargs.copy()
            self.label.pack(**kwargs)
            self.cover_frame=internal_tk.Frame(self.master)
        self.toplevel.update()
        self.dimentions=(self.toplevel.winfo_width(),self.toplevel.winfo_height())
        if 'padx' in kwargs:
            kwargs['padx']+=self.dimentions[0]//2
        else:
            kwargs['padx']=self.dimentions[0]//2
        if 'pady' in kwargs:
            kwargs['pady']+=self.dimentions[1]//2
        else:
            kwargs['pady']=self.dimentions[1]//2
        self.cover_frame.pack(**kwargs)
        self.cover_frame.pack_propagate(False)
        self.change_kwargs=True
        self.toplevel.deiconify()
        toplevels.position(None)

    def config(self,**kwargs):
        if 'opacity' in kwargs:
            self.opacity=kwargs['opacity']
            self.toplevel.attributes('-alpha',self.opacity)
            del kwargs['opacity']
        if 'transcolor' in kwargs:
            self.transcolor=kwargs['transcolor']
            self.toplevel.wm_attributes("-transparentcolor",self.transcolor)
            del kwargs['transcolor']
        self.label.config(kwargs)
        self.change_kwargs=False
        self.pack(**self.pack_kwargs)

    def destroy(self):
        self.cover_frame.destroy()
        toplevels.toplevels.remove(self)
        self.toplevel.destroy()
        try:
            self.master.deiconify()
        except:
            pass
        toplevels.position(None)

    def pack_forget(self):
        self.cover_frame.destroy()
        toplevels.toplevels.remove(self)
        self.toplevel.withdraw()
        try:
            self.master.deiconify()
        except:
            pass
        toplevels.position(None)

    configure=config

toplevels=_Toplevels()