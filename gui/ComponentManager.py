from gui.ComponentContainer import ComponentContainer
from gui.RenderParamWrapper import RenderParamWrapper
from typing import Optional, TypeVar, Literal, Union, Type
from tkinter import Widget
import re

_ComponentType = Union[Type[Widget], Widget]
T = TypeVar("T")


class ComponentManager:
    def __init__(self):
        self._component_container = ComponentContainer()

    @staticmethod
    def create_manager() -> "ComponentManager":
        return ComponentManager()

    @staticmethod
    def _pascal_to_snake(pascal_string: str):
        # 정규 표현식을 사용하여 대문자 문자를 찾고 언더스코어(_)로 대체
        return re.sub(r'(?<!^)(?=[A-Z])', '_', pascal_string).lower()

    @staticmethod
    def _get_component_type(component: _ComponentType):
        type_str = str(component if type(component) is type else type(component))
        return type_str.split("'")[1].split(".")[1 if "ttk" not in type_str else 2]

    @staticmethod
    def _get_method_string(component: _ComponentType) -> str:
        return ComponentManager._pascal_to_snake(
            pascal_string = ComponentManager._get_component_type(
                component = component
            )
        )

    def add_component(self,
                      name: str,
                      component: _ComponentType,
                      with_render: bool = False,
                      render_type: Optional[Literal["grid", "pack"]] = None,
                      render_param: Optional[RenderParamWrapper] = None
                      ):
        # component 파라미터의 타입에 알맞은 상속받은 ComponentContainer 클래스의 add메소드
        getattr(self._component_container, f"add_{self._get_method_string(component)}")(name, component)

        if with_render:
            getattr(component, render_type)(**render_param.get_param_dict())

    def get_component(self, name: str, component_class: Type[T]) -> T:
        # component_class 파라미터의 타입에 알맞은 상속받은 ComponentContainer 클래스의 get메소드
        return getattr(self._component_container, f"get_{self._get_method_string(component_class)}")(name)

    def update_component(self, name: str, component_class: Type[T], **update_params) -> Optional[Exception]:
        component = self.get_component(name = name, component_class = component_class)

        try:
            component.config(**update_params)
            component.update()

        except Exception as E:
            return E


