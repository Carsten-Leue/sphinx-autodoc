"""My Implementation"""
from typing import Collection

from sphinx_autodoc.api import MyInterfaceClass


class MyClass:  # pylint: disable=too-few-public-methods
    """This is my class and its doc
    
    This is a reference to :class:`~sphinx_autodoc.api.MyInterfaceClass`
    
    """

    delegate: MyInterfaceClass
    """Some delegate"""

    external: Collection
    """Some external reference"""

    def get_delegate(self) -> MyInterfaceClass:
        """Gets the delegate

        Returns:
            the delegate
        """
        return self.delegate

    def get_external(self) -> Collection:
        """Gets the delegate

        Returns:
            the delegate
        """
        return self.external


VARIABLE: MyClass = MyClass()
"""This is my variable and its doc"""
