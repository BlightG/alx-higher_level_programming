#!/usr/bin/python3
""" creating a rebel int """


class MyInt(int):
    """ a modification of the int class """

    def __eq__(self, other):
        """ a function returninfg true if other and
            self are not equal to eachother

                Args:
                    other: other instance to be compare to self
        """
        return other.__ne__(self)

    def __ne__(self, other):
        """ a function returninfg true if other and
            self are not equal to eachother

                Args:
                    other: other instance to be compare to self
        """
        return other.__eq__(self)
