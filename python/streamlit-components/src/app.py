from functools import cached_property

import pandas as pd
import streamlit as st

from base import Component, DivComponent, WrapperComponent, function_render


class UI(DivComponent):
    @property
    def header(self):
        return Component("h1", "subheader", "first header")

    @cached_property
    def dataframe(self):
        df = pd.DataFrame({"a": [1, 2, 3]})
        return Component("df", "dataframe", df)
        # return Component("h1", "subheader", "hello")

    @property
    def box1(self):
        return Component("sb1", "selectbox", label="sb1", options=[1, 2, 3])

    @property
    def box2(self):
        return Component("sb2", "selectbox", label="sb2", options=[1, 2, 3])

    @property
    @function_render
    def selectbox(self):
        cols = st.columns(2)

        with cols[0]:
            self.box1.render()

        with cols[1]:
            self.box2.render()
        return

    def render(self):
        return WrapperComponent(
            "container2",
            st.container,
            [self.header, self.dataframe, self.selectbox],
        ).render()


if __name__ == "__main__":
    UI().render()

    # with st.container():
    #     st.subheader("dataframe")
    #     cols = st.columns(2)
    #     with st.container():
    #         with cols[0]:
    #             st.subheader("h1")
    #         with cols[1]:
    #             st.subheader("h2")
    #     st.dataframe(pd.DataFrame({"1": [1]}))

    # container2
    # sh1
    # container1
    # col1
    # col_sh1
    # col2
    # col_sh2
    # df
