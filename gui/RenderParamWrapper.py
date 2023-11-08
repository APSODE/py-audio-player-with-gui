from typing import Literal, Optional


_SIDE_LITERAL = Literal["top", "bottom", "left", "right"]
_ANCHOR_LITERAL = Literal["center", "n", "e", "s", "w", "ne", "nw", "se", "sw"]
_FILL_LITERAL = Literal["none", "x", "y", "both"]


class RenderParamWrapper:
    def __init__(self,
                 row: Optional[int] = None,
                 column: Optional[int] = None,
                 padx: Optional[int] = None,
                 pady: Optional[int] = None,
                 ipadx: Optional[int] = None,
                 ipady: Optional[int] = None,
                 side: Optional[_SIDE_LITERAL] = None,
                 anchor: Optional[_ANCHOR_LITERAL] = None,
                 fill: Optional[_FILL_LITERAL] = None,
                 expand: Optional[bool] = None
                 ):
        if row is not None:
            self._row = row

        if column is not None:
            self._column = column

        if padx is not None:
            self._padx = padx

        if pady is not None:
            self._pady = pady

        if ipadx is not None:
            self._ipadx = ipadx

        if ipady is not None:
            self._ipady = ipady

        if side is not None:
            self._side = side

        if anchor is not None:
            self._anchor = anchor

        if fill is not None:
            self._fill = fill

        if expand is not None:
            self._expand = expand

        pack_field_check = any([field is not None for field in [side, anchor, fill, expand]])
        grid_field_check = any([field is not None for field in [row, column]])

        if pack_field_check and grid_field_check:
            raise ValueError("grid에 사용하는 파라미터와 pack에 사용하는 파라미터는 동시에 활성화 될 수 없습니다.")

    def get_param_dict(self):
        return self._get_all_data_by_dict()

    def _get_all_data_by_dict(self):
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}
