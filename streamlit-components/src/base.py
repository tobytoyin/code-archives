from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass, field
from functools import wraps
from typing import List

import numpy as np
import pandas as pd
import streamlit as st

STACK = deque([])

class BaseComponent(ABC):
    def __init__(self, id: str, component: str, *args, **kwargs) -> None:
        self.id = id
        self._state_condition = None
        super().__init__()
        
        
    def display_condition(self, fn: callable) -> None:
        self._state_condition = fn
    
    @abstractmethod
    def render(self):
        ...
        

class DivComponent(ABC):
    @abstractmethod
    def render(self):
        ...
        
        
def function_render(fn):
    def _decorator(*args, **kwargs):
        comp = Component(None)
        comp.set_function_render(lambda: fn(*args, **kwargs))
        return comp
    return _decorator


class Component(BaseComponent):
    
    def __init__(self, id, component=None, *args, **kwargs) -> None:
        
        super().__init__(id, component, *args, **kwargs)
        if not component:
            return 
        self.callback = lambda: getattr(st, component)(*args, **kwargs)
        
    def set_function_render(self, fn):
        """Allowing a functional procedure that doesn't fit as a streamlit element \ 
           to be render as `Component.render()`
        """
        self.callback = fn
        return self
    
    def render(self):
    
        STACK.append(self.id)      
        if not self._state_condition:
            return self.callback()
        
        if self._state_condition() == True:
            return self.callback()
            
    
    
class WrapperComponent(BaseComponent):
    def __init__(self, id, component, elements: List[Component], *args, **kwargs) -> None:
        # self.component = getattr(st, component)
        self.id = id
        self.component = component
        self.elements = elements
        self.args = args
        self.kwargs = kwargs
        
    def add_after(self, id):
        # add component after certain widget's id
        ...
        
    def add_before(self, id):
        # add component before certain widget's id
        ...
        
    def add_pos(self, idx): 
        # add component at a certain position
        ...
        
    def render(self):

        if not self.elements:
            return 
        
        STACK.append(self.id)
        
        # check if this is callable wrapper?
        if not callable(self.component): 
            context = lambda: self.component
        else: 
            context = self.component
            
        with context(*self.args, **self.kwargs):
            for el in self.elements:
                el.render()
                
    

