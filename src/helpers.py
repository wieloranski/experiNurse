#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Searcher:
    """
    Any comment would be useless. ;-)
    """

    def find(self, element, list):
        """
        Finds element in two-dimensional list.
        Returns -1 if not found.
        """

        for column, sublist in enumerate(list):
            try:
                row = sublist.index(element)
            except ValueError:
                continue
            return column, row
        return -1
