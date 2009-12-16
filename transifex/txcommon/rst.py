# From: http://code.activestate.com/recipes/267662/#c2 and
# http://kogs-www.informatik.uni-hamburg.de/~meine/software/scripts/tableindent.py

def toTable(rows, header=True, vdelim=" ", border="=", padding=0, justify="left"):
        """
        Return a list of lists as a Restructured Text Table.

        - rows:    List of lists
        - header:  If True the first row is treated as a table header
        - vdelim:  Vertical delimiter between columns
        - border:  Character for drawing the the horizontal table border, in 
                   the header and footer.
        - padding: Padding nr. of spaces are left around the longest element 
                   in the column.
        - justify: May be 'left', 'center' or 'right'.
        """
        justify = {'center' : str.center,
                   'right'  : str.rjust,
                   'left'   : str.ljust}[justify.lower()]
        result = ""

        # Calculate column widhts (longest item in each col
        # plus "padding" nr of spaces on both sides)
        cols = map(lambda *row: [elem or ' ' for elem in row], *rows)
        colWidths = [max([len(str(item))+2*padding for item in col]) for col in cols]

        # The horizontal border needed by rst
        borderline = vdelim.join([w*border for w in colWidths])+"\n"

        # Outputs table in rst format
        result += borderline
        for row in rows:
            result += vdelim.join([justify(str(item),width) for (item,width) in zip(row,colWidths)])+"\n"
            if header:
                result += borderline
                header = False

        result += borderline
        return result
