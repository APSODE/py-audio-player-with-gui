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
                 expand: Optional[bool] = None,
                 x: Optional[int] = None,
                 y: Optional[int] = None,
                 relx: Optional[int] = None,
                 rely: Optional[int] = None,
                 width: Optional[int] = None,
                 height: Optional[int] = None,
                 relwidth: Optional[int] = None,
                 relheight: Optional[int] = None
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

        if x is not None:
            self._x = x

        if y is not None:
            self._y = y

        if relx is not None:
            self._relx = relx

        if rely is not None:
            self._rely = rely

        if width is not None:
            self._width = width

        if height is not None:
            self._height = height

        if relwidth is not None:
            self._relwidth = relwidth

        if relheight is not None:
            self._relheight = relheight

        anchor_field_check = anchor is not None
        pack_field_check = any([field is not None for field in [side, fill, expand]])
        grid_field_check = any([field is not None for field in [row, column]]) and not anchor_field_check
        place_field_check = any([field is not None for field in [x, y, relx, rely, width, height, relwidth, relheight]])

        if [pack_field_check, grid_field_check, place_field_check].count(True) >= 2:
            raise ValueError("grid, pack, place에 사용하는 파라미터는 동시에 활성화 될 수 없습니다.")

    def get_param_dict(self):
        return self._get_all_data_by_dict()

    def _get_all_data_by_dict(self):
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}
