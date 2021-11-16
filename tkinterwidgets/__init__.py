import tkinter as tk 

class _Toplevels():
    def __init__(self):
        self.toplevels=[]

    def lift(self):
        for top in self.toplevels:
            top.lift()

    def position(self,event):
        try:
            for top in self.toplevels:
                top.position()
        except:pass

toplevels=_Toplevels()

class TransparentContainer(tk.Toplevel):
    def __init__(self,master,**kwargs):
        self.master=master
        self.opacity=kwargs.pop('opacity',1)
        self.transcolor=kwargs.pop('transcolor','SystemButtonFace')
        bg=kwargs.pop('bg',None)
        if not bg:
            bg=kwargs.pop('background',None)
            if not bg:
                bg=self.transcolor
        super().__init__(self.master,bg=bg,**kwargs)
        self.overrideredirect(True)
        self.attributes('-alpha',self.opacity)
        self.wm_attributes("-transparentcolor",self.transcolor)
        self.withdraw()
        self.bind('<Configure>',self._on_change)
        self.master.bind('<Configure>',toplevels.position)
        self.master.bind('<Map>',self._on_map)
        self.master.bind('<Unmap>',self._on_unmap)
        self.pack_remember=False
        self.base_padding=(0,0)

    def _on_unmap(self,event):
        self.withdraw()

    def _on_map(self,event):
        self.deiconify()
        toplevels.position(None)

    def _on_change(self,event):
        self.dimentions=(event.width,event.height)
        x=self.base_padding[0]+self.dimentions[0]//2
        y=self.base_padding[1]+self.dimentions[1]//2
        self.cover_frame.pack_configure(padx=x,pady=y)

    def position(self):

        def geometry():
            self.x=self.cover_frame.winfo_rootx()
            self.y=self.cover_frame.winfo_rooty()
            self.center_x=self.cover_frame.winfo_width()//2-self.dimentions[0]//2
            self.center_y=self.cover_frame.winfo_height()//2-self.dimentions[1]//2
            self.coords=(self.center_x+self.x,self.center_y+self.y)
            self.geometry(f'+{self.coords[0]}+{self.coords[1]}')

        try:geometry()
        except:pass
        self.master.update_idletasks()
        toplevels.lift()

    def pack(self,**kwargs):
        toplevels.toplevels.append(self)
        if not self.pack_remember:
            self.cover_frame=tk.Frame(self.master)
        else:
            self.cover_frame.pack()
            self.deiconify()
            return
        self.update()
        self.dimentions=(self.winfo_width(),self.winfo_height())
        self.base_padding=(kwargs.pop('padx',0),kwargs.pop('pady',0))
        self.cover_frame.pack(padx=self.base_padding[0],pady=self.base_padding[1],**kwargs)
        self.cover_frame.pack_propagate(False)
        self.pack_remember=False
        self.deiconify()
        toplevels.position(None)

    def config(self,**kwargs):
        opacity=kwargs.pop('opacity',0)
        transcolor=kwargs.pop('transcolor',0)
        if opacity!=0:
            self.opacity=opacity
            self.attributes('-alpha',self.opacity)
        if transcolor!=0:
            self.transcolor=transcolor
            self.wm_attributes("-transparentcolor",self.transcolor)
        super().config(**kwargs)

    def destroy(self):
        self.cover_frame.destroy()
        toplevels.toplevels.remove(self)
        super().destroy()
        self.master.deiconify()
        toplevels.position(None)    

    def pack_forget(self):
        self.cover_frame.pack_forget()
        toplevels.toplevels.remove(self)
        self.pack_remember=True
        self.withdraw()
        try:self.master.deiconify()
        except:pass
        toplevels.position(None)

    configure=config
    